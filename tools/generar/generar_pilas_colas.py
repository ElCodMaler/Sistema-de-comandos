from ..crear.sistema_PilasColas import CrearSistema
import json
import sys

#INICIALIZACION DE VARIABLES
carpetas = []
ficheros = []
datos_carpetas = list
datos_ficheros = list

#lectura del archivo Json
with open("DataBase\Carpetas1.json", 'r') as archivo1:
    archJC = json.load(archivo1)
with open("DataBase\Archivos1.json", 'r') as archivo2:
    archJF = json.load(archivo2)

#guardar datos del archivo en una lista
for c in archJC.values():
    carpetas.append(c)

for f in archJF.values():
    ficheros.append(f)
#creamos el sistema y sus funciones
sis = CrearSistema(ficheros, carpetas)