#!/usr/bin/python
# -*- coding: utf-8 -*-

#Software creado por Juan Pablo Díaz Correa @Juanipisx

import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext as st
from tkinter import ttk
from Personality_Insight_API_Class import PersonalityInsightsAPI
import matplotlib.pyplot as plt
import os

class Aplication_Personality():
    
    
    def __init__(self):
        self.main_window = tk.Tk() #Nueva Ventana
        self._SetWindowPreferences()
        self._SetLabels()
        self._PutLabels()
        self._Set_API_KEY_CANVAS()
        self._Put_API_KEY_CANVAS()
        
        self.main_window.mainloop()
    
    def _SetWindowPreferences(self):
        self.main_window.title("Análisis de personalidad IBM - Personality Insight - Juan Pablo Díaz Correa")
        self.main_window.geometry("1345x550")
        self.main_window.iconbitmap("./Logo-JP.ico")
    

    #------------Labels--------------#
    def _SetLabels(self):
        texto_bienvenida = "Bienvenido al analisis de personalidad \n IBM Personality Insights"
        self.welcom_label = tk.Label(self.main_window,text=texto_bienvenida, font=("Arial", 17))
        
        autor = "Por: Juan Pablo Díaz Correa \n Twitter: @Juanipisx"
        self.autor_label = tk.Label(self.main_window, text=autor, font=("Berlin Sans FB", 12))
    
    def _PutLabels(self):
        self.welcom_label.place(x=250, y=3)
        self.autor_label.place(x=550, y=70)
    

    
    #------------API_KEY_CANVAS--------------#
    
    def _Set_API_KEY_CANVAS(self):
        self.API_KEY_CANVAS = tk.Canvas(self.main_window)
        self.API_KEY_LABEL = tk.Label(self.API_KEY_CANVAS, text="API KEY")
        self.API_KEY_BOX = tk.Entry(self.API_KEY_CANVAS)
        self.API_URL_LABEL = tk.Label(self.API_KEY_CANVAS, text="API URL")
        self.API_URL_BOX = tk.Entry(self.API_KEY_CANVAS)
        self.API_CONNECT_BUTTOM = tk.Button(self.API_KEY_CANVAS, text="Start", command=self._start_connection)
    
    def _Put_API_KEY_CANVAS(self):
        self.API_KEY_CANVAS.place(x=420, y=150)
        self.API_KEY_LABEL.pack()
        self.API_KEY_BOX.pack()
        self.API_URL_LABEL.pack()
        self.API_URL_BOX.pack()
        self.API_CONNECT_BUTTOM.pack()


    #------------ENTRY_BOX--------------#
    def _Set_Scrolled_Box(self):
        self._ENTRY_BOX_CANVAS = tk.Canvas(self.main_window)
        self._ENTRY_BOX_LABEL = tk.Label(self._ENTRY_BOX_CANVAS, text="Escribe el texto a analizar aquí debajo")
        self._ENTRY_BOX = st.ScrolledText(self._ENTRY_BOX_CANVAS, height=20, width=40)

    def _Put_Scrolled_Box(self):
        self._ENTRY_BOX_CANVAS.place(x=50, y=130)
        self._ENTRY_BOX_LABEL.pack()
        self._ENTRY_BOX.pack()

    #------------PARAMS_SET--------------#
    def _Set_Params_IBM(self):
        self._PARAMS_CANVAS = tk.Canvas(self.main_window)
        
        #--------Lenguaje de contenido---#
        self._CONTENT_LANGUAGE_LABEL = tk.Label(self._PARAMS_CANVAS, text="Lenguaje del texto")
        self._CONTENT_LANGUAGE = ttk.Combobox(self._PARAMS_CANVAS, state="readonly")
        self._CONTENT_LANGUAGE["values"] = ["Arabe", "Ingles", "Japones", "Coreano", "Español"]
        
        #--------Lenguaje de salida---#
        self._ACCEPT_LENGUAGE_LABEL = tk.Label(self._PARAMS_CANVAS, text="Lenguaje de salida")
        self._ACCEPT_LENGUAGE = ttk.Combobox(self._PARAMS_CANVAS, state="readonly")
        self._ACCEPT_LENGUAGE["values"] = ["Arabe", "Portugues", "Ingles", "Frances", "Aleman", "Italiano", "Japones", "Coreano", "Chino simplificado", "Español", "Chino tradicional"]
        
        """
        Valores reales para ibm
        Arabe = ar |Portugues de brazil = pt-br| Ingles = en |Frances = fr | Aleman = de  
        Italiano = it  |Japones = ja | Coreano = ko |Chino simplificado = zh-cn
        Español = es | Chino tradicional = zh-tw
        """
        #-------Parametros adicionales-----#
        """
        self._RAW_SOCRES_VALUE = tk.BooleanVar()
        self._RAW_SCORES = tk.Checkbutton(self._PARAMS_CANVAS, text="Raw Scores", variable=self._RAW_SOCRES_VALUE)
        """
        self._CONSUMPTION_PREFERENCES_VALUE = tk.BooleanVar()
        self._CONSUMPTION_PREFERENCES = tk.Checkbutton(self._PARAMS_CANVAS, text="Preferencias de consumo", variable=self._CONSUMPTION_PREFERENCES_VALUE)

    
    def _Put_Params_IBM(self):
        self._PARAMS_CANVAS.place(x=400, y=290)
        self._CONTENT_LANGUAGE_LABEL.pack()
        self._CONTENT_LANGUAGE.pack()
        self._ACCEPT_LENGUAGE_LABEL.pack()
        self._ACCEPT_LENGUAGE.pack()
        #self._RAW_SCORES.pack()
        self._CONSUMPTION_PREFERENCES.pack()

    
    #------------TEXT_BUTTOMS--------------#
    def _Open_txt(self):
        self.archive = filedialog.askopenfilename(title="Abre tu archivo de texto", filetypes=(("Archivos de texto .txt", "*.txt"),))
        with open(self.archive, mode='r', encoding='utf-8') as read_archive:
            self._ENTRY_BOX.insert('1.0', read_archive.read())
    
    

    def _Set_Send_Buttoms(self):
        self._SEND_CANVAS = tk.Canvas(self.main_window)
        self._OPEN_TEXT = tk.Button(self._SEND_CANVAS, text="Abrir .txt", command=self._Open_txt)
        self._SEND_BUTTOM = tk.Button(self._SEND_CANVAS, text="Enviar a analisis", command=self._send_text)
    
    def _Put_Send_Buttoms(self):
        self._SEND_CANVAS.place(x=50, y=500)
        self._OPEN_TEXT.grid(row=0, column=0)
        self._SEND_BUTTOM.grid(row=0, column=1)


    #------------IBM Functions--------------#
    def _start_connection(self):
        
        self._IBM_personality = PersonalityInsightsAPI(APIKEY=str(self.API_KEY_BOX.get()), url=str(self.API_URL_BOX.get()))
        self._Set_Scrolled_Box()
        self._Put_Scrolled_Box()

        self._Set_Send_Buttoms()
        self._Put_Send_Buttoms()

        self._Set_Params_IBM()
        self._Put_Params_IBM()
        self._CONTENT_LANGUAGE.current(4)
        self._ACCEPT_LENGUAGE.current(9)

    def _set_params(self):
        self._diccionario_content_language = {'Arabe'  : 'ar', 
                                              'Ingles' : 'en',
                                              'Japones' : 'ja',
                                              'Coreano' : 'ko',
                                              'Español' : 'es'}
        self._diccionario_accept_language = {'Arabe'  : 'ar', 
                                              'Ingles' : 'en',
                                              'Japones' : 'ja',
                                              'Coreano' : 'ko',
                                              'Español' : 'es',
                                              'Portugues' : 'pt-br',
                                              'Frances' : 'fr',
                                              'Aleman' : 'de',
                                              'Italiano' : 'it',
                                              'Chino simplificado': 'zn-cn',
                                              'Chino tradicional': 'zh-tw'}

        for key,value in self._diccionario_content_language.items(): #Buscamos en el diccionario de lenguajes aceptados
            if key == self._CONTENT_LANGUAGE.get():
                self._content_languague_value = value
                print(value)
        
        for key,value in self._diccionario_accept_language.items(): #Buscamos en el diccionario de lenguajes aceptados
            if key == self._ACCEPT_LENGUAGE.get():
                
                self.__accept_languague_value = value
                print(value)
        
        
        self._IBM_personality.SetParams(content_language = self._content_languague_value, 
                                       accept_language= self.__accept_languague_value,
                                       consumption_preferences= self._CONSUMPTION_PREFERENCES_VALUE.get(),
                                       charset=';utf-8'
                                       )

    def _view_stats(self):
        
        self._Result_box_label = tk.Label(self.main_window, text='Resultado')
        self._Result_box_label.place(x=740, y=130)
        self._Result_box = st.ScrolledText(self.main_window, height=20, width=90)
        self._Result_box.place(x=600, y=150)
        self._Result_box.delete('1.0', tk.END)
        results = ""
        for value in self.profile['personality']:
            results += (value.get('name') + ': ' + 'percentil: '+ str(value.get('percentile')) + '\n'+ '\n')
            for list_children in value.get('children'):
                results += ('     ' +list_children.get('name')+': ' +'percentil: ' + str(list_children.get('percentile')) + '\n')
                results +=('     ' + 'Importancia: ' + str(list_children.get('significant')) + '\n\n')
            
            
            if self._CONSUMPTION_PREFERENCES_VALUE.get():
                for value in self.profile['consumption_preferences']:
                    results += ('\n')
                    results += (value.get('name') + '\n')
                    for value2 in  value.get('consumption_preferences'):
                        results += (value2.get('name') + ' : ' +str(value2.get('score')) + '\n')
        self._Result_box.insert(tk.INSERT, results)
        self._Result_box.configure(state='disabled')
        

              

    def _view_plot(self):
        plt.figure()
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        i = 1
        for value in self.profile['personality']:
            etiquetas = list()
            valores = list()
            for list_children in value.get('children'):
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
            plt.subplot(2,3,i)
            plt.barh(etiquetas, valores)
            plt.yticks(fontsize='7') 
            plt.title(value.get('name'))
            i+=1        
        plt.show()
    
    def _send_text(self):
        self._set_params()
        self.profile = self._IBM_personality.Request_analize(content_type='text/plain', 
                                                            content=self._ENTRY_BOX.get('1.0', tk.END))        
        self._view_stats()
        self._view_plot()
    
        
        

     
if __name__ == '__main__':
    App = Aplication_Personality()