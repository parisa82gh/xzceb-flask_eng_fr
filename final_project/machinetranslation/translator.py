'''
This module is a french to english and enlish to french translator
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an instance of teh IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''
    This function translate an english text to french
    '''
    if english_text == '':
        return ''
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def frenchToEnglish(french_text):
    '''
    This function translate a french text to english
    '''
    if french_text == '':
        return ''
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
