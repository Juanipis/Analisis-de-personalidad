#!/usr/bin/python
# -*- coding: utf-8 -*-
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class PersonalityInsightsAPI():
    def __init__(self, APIKEY, url,version='2017-10-13'):
        try:    
            self.authenticator = IAMAuthenticator(APIKEY)
            self.personality_insights = PersonalityInsightsV3(
                version = version,
                authenticator = self.authenticator
                )
            self.personality_insights.set_service_url(url)
            print("Exito, credenciales validas")
        except:
            print("Error, credenciales no validas")
    
    def SetParams(self, content_language = 'es', accept_language = 'es', charset=';utf-8', raw_scores=False, consumption_preferences=False):
        try:
            self.content_language = content_language
            self.accept_language = accept_language
            self.charset = charset
            self.raw_socres = raw_scores
            self.consumption_preferences = consumption_preferences
            print("Parametros añadidos con exito")
        except:
            print("Parametros incorrectos")
        

    def Request_analize(self, content_type, content):
        self.profile = self.personality_insights.profile(
            content,
            'application/json',
            Content_type = content_type+self.charset,
            consumption_preferences = self.consumption_preferences,
            raw_scores = self.raw_socres,
            content_language = self.content_language,
            accept_language = self.accept_language,
            ).get_result()
        
        
        return self.profile
        
       
        
        
