'''
Created on Mar 31, 2017

@author: aneesh.c
'''
# -*- coding: utf-8 -*-

import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()
from rest_framework import viewsets
from config import *
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
# from model import *
import dill
import base64


@permission_classes((permissions.AllowAny,))
class TestAPI(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        #output_text = {'status': 'Hellow'}
#         CACHE_ID = 'Constant'
#         if 'user_id' in question:
#             CACHE_ID = question['user_id']
#         req_cache = create_cache(CACHE_ID)
#         user_input = question['messageText']
        if question['messageSource'] == 'userInitiatedReset':
#             req_cache.delete()
            question['messageSource'] = 'messageFromBot'
            question['messageText'] = welcome_note
            return Response(question)
#         kernel = dill.loads(base64.b64decode(req_cache.user.aiml_kernel))
#         question = generate_reply(question, kernel, req_cache.cache)
#         if 'entities' in question:
#             req_cache.cache = question['entities']
#             req_cache.user.aiml_kernel = \
#                 base64.b64encode(dill.dumps(kernel))
#             req_cache.user.save()
#             req_cache.save()
# 
#         return Response(question)
        