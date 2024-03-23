from ..guardar.guardar_archivos import Entrada_ficheros
from ..guardar.guardar_carpetas import Entrada_carpetas
from ..crear.sistema_Arboles import CrearSistema#necesita un cambio
import json

#Inicializacion de variables
#constantes
cantidad_carpetas = cantidad_archivos = 2

#variables
lista_Fich: list[dict] = [None for doc in range(cantidad_archivos)]
lista_Carp: list[dict] = [None for doc in range(cantidad_carpetas)]
lista_entradasFich: list[list[Entrada_ficheros]] = [[] for doc in range(cantidad_archivos)]
lista_entradasCarp: list[list[Entrada_carpetas]] = [[] for doc in range(cantidad_carpetas)]
archivos = [[] for i in range(cantidad_archivos)]
carpetas = [[] for i in range(cantidad_carpetas)]
#lectura del archivo Json
for i in range(len(lista_Carp)):
    with open(f"DataBase\Carpetas{i+1}.json") as archivo:
        lista_Carp[i] = dict(json.load(archivo))
for i in range(len(lista_Fich)):
    with open(f"DataBase\Archivos{i+1}.json") as archivo:
        lista_Fich[i] = dict(json.load(archivo))
#se guarda la informacion de cada archivo o carpeta
for i in range(len(lista_entradasCarp)):
    for doc in lista_Carp[i].values():
        lista_entradasCarp[i].append(Entrada_carpetas(doc))
for i in range(len(lista_entradasFich)):
    for arch in lista_Fich[i].values():
        lista_entradasFich[i].append(Entrada_ficheros(arch))
#se guardan la informacion de cada archivo o carpeta por secciones
for i in range(len(carpetas)):
    for doc in lista_entradasCarp[i]:
        carpetas[i].append(doc.getCarpetas())
for i in range(len(archivos)):
    for arch in lista_entradasFich[i]:
        archivos[i].append(arch.getFicheros())
#se crea el sistema
#sis = CrearSistema(archivos, carpetas)
#impresion con formato
print('<Archivo Archivos1>')
print('{0:2s}  {1:11s} {2:11s} {3:7s} {4:8s}'.format('id:','nombre:','extencion:','peso:','datos'))
for p in archivos[1]:
    print('{0:2d} | {1:11s} | {2:7s} | {3:2d} | {4:18s}'.format(p[0],p[1],p[2],p[3],p[4]))