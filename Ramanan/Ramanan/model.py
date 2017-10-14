'''
Created on Mar 31, 2017

@author: aneesh.c
'''
import aiml
import dill
from .models import RequestCache
from Ramanan.models import UserCache
brain_file_medical = "/home/aneesh/git/Ramanan/Ramanan/Ramanan/standard.brn"
from textblob import TextBlob
from config import errors
 
def create_cache(CACHE_ID):
    import base64
    try:
        req_cache = RequestCache.objects.get(cache_id=CACHE_ID)
    except RequestCache.DoesNotExist:
        kern_medical = aiml.Kernel()
        kern_medical.bootstrap(brainFile=brain_file_medical)
        kernel_str = dill.dumps(kern_medical)
        kernel_str = base64.b64encode(kernel_str)
        req_cache = RequestCache.objects.create(cache_id=CACHE_ID, cache=[],
                                                user=UserCache.objects
                                                .create(aiml_kernel=kernel_str)
                                                )
    return req_cache
  
  
  
  
def generate_reply(question, kernel, cache_list):
    response = question

    txt_obj = TextBlob(question['messageText'])
 
    try:
        language_detected = txt_obj.detect_language()
    except:
        language_detected = 'en'
     
    if language_detected != 'en':
        try:
            question['messageText'] = str(TextBlob(question['messageText']).translate(to = 'en'))
        except:
            question['messageText'] = 'asas'
    
    kernel_reply = kernel.respond(question['messageText'])
    malayalam_translated =  str(TextBlob(kernel_reply).translate(to = 'ml'))
    response['messageText'] = []
    response['messageText'].append(malayalam_translated)
    return response
    