from ..crear.sistema_PilasColas import CrearSistema
import json

#INICIALIZACION DE VARIABLES
#constantes
cantidad = 3
#variables
archJC = []
carpetas = [[] for i in range(cantidad)]
ficheros = []
datos_carpetas = list
datos_ficheros = list

#lectura del archivo Json
for i in range(cantidad):
    with open(f"DataBase\Carpetas{i+1}.json", 'r') as archivo1:
        archJC.append(json.load(archivo1))

with open("DataBase\Archivos1.json", 'r') as archivo2:
    archJF = json.load(archivo2)

#guardar datos del archivo en una lista
for arch in range(cantidad):
    for c in archJC[arch].values():
        carpetas[arch].append(c)

for f in archJF.values():
    ficheros.append(f)

#creamos el sistema y sus funciones
sis = CrearSistema(ficheros, carpetas)