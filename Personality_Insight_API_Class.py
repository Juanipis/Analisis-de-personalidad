#!/usr/bin/python
# -*- coding: utf-8 -*-
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import matplotlib.pyplot as plt

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
        """
        plt.figure()
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        i = 1
        for value in self.profile['personality']:
            etiquetas = list()
            valores = list()
            
            print('#------------------------------#')
            print(value.get('name'))
            print('percentil: '+ str(value.get('percentile')))
            for list_children in value.get('children'):
                print(list_children.get('name')) #Obtenemos subcategoria
                case = 0
                result = ""
                for letter in list_children.get('name'):
                    if letter == " " and case == 0:
                        result += "\n"
                        case+=1
                    else:
                        result += letter

                etiquetas.append(result)
                valores.append(list_children.get('percentile'))
                print('percentil: ' + str(list_children.get('percentile')))
                print('Significante: ' + str(list_children.get('significant')))
            plt.subplot(2,3,i)
            plt.barh(etiquetas, valores)
            plt.yticks(fontsize='7') 
            plt.title(value.get('name'))
            i+=1
            
        
        plt.show()

        """
        
        return self.profile
        
       
        
        




if __name__ == '__main__':    #Prueba de API
    url = 'https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/1c892422-c133-4527-8b86-4f87bd6a98f5'
    key = 'NUC8AJUbK0JAZUsDIa76wtrqNagwM3LRbOhAxd6ULmnh'
    prueba = PersonalityInsightsAPI(key, url)
    prueba.SetParams()
    archivo = open('./profile_1.txt', encoding='utf8')
    perfil = prueba.Request_analize('text/plain', archivo.read())
    #print(perfil)
    archivo.close()

