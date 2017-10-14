'''
Created on Mar 31, 2017

@author: aneesh.c
'''
# -*- coding: utf-8 -*-


# sys.setdefaultencoding() does not exist, here!


from rest_framework import viewsets
from config import *
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
# from model import *
from model import *
import dill
import base64
from textblob import TextBlob
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
# sys.setdefaultencoding('utf8')

@permission_classes((permissions.AllowAny,))
class TestAPI(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        print question
        CACHE_ID = '54'
        if 'user_id' in question:
            CACHE_ID = question['user_id']
        req_cache = create_cache(CACHE_ID)
        if question['messageSource'] == 'userInitiatedReset':
            req_cache.delete()
            question['messageSource'] = 'messageFromBot'
            question['messageText'] = str(TextBlob(welcome_note).translate(to = 'ml'))
            return Response(question)
        kernel = dill.loads(base64.b64decode(req_cache.user.aiml_kernel))
        req_cache.user.aiml_kernel = base64.b64encode(dill.dumps(kernel))
        req_cache.user.save()
        req_cache.save()
        question = generate_reply(question, kernel, req_cache.cache)

        
        return Response(question)
        