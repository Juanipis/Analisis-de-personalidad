# Análisis de personalidad con IBM Personality Insight
_Este en un pequeño programa desarrollado en Python que tiene la funcionalidad de simplificar la experiencia de usuario para usar este servicio de inteligencia artificial diseñado por IBM_

## Comenzando 🚀
* Primero es necesario tener una cuenta en IBM Cloud https://cloud.ibm.com/ 
* Segundo crear un nuevo servicio de Personality Insight en https://cloud.ibm.com/catalog/services/personality-insights 
* Tercero obtener el **API KEY** y URL del servicio

### Pre-requisitos 📋
_Puedes usar el entorno virtual del proyecto o instalar los siguientes paquetes_
* IBM Cloud SDK
```
pip install --upgrade "ibm-watson>=4.5.0" 
```
* Matplotlib
```
pip install matplotlib
```
* Tkinter
```
Ya viene instalado por defecto en Python
```

### Despliegue 📦
* Primero para iniciar el programa ejecute main.py
```
python3 main.py
```
* Segundo escribe tu APIKEY y URL en los cajones de la interfaz grafica
* Tercero escribe el texto a analizar
* Cuarto escoge el idioma del texto y el idioma de salida
* Quinto presiona el botón enviar análisis y listo
* Por último saldrá tu análisis en una ventana nueva de matplotlib

_Tambien puedes cargar un archivo de texto con el boton **Abrir .txt**_

### Muchas gracias, recuerda seguirme en twitter [@Juanipis](https://twitter.com/Juanipis)
