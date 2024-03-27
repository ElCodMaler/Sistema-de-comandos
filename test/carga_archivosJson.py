import json
import sys
from components.elementos_sistema import Carpeta
#INICIALIZACION DE VARIABLES
carpetas = []
datos_carpetas = list
def cantidad_listas(A: dict):
    res = []
    for l in range(len(A)):
        res.append([])
    return res
#lectura del archivo Json
with open("DataBase\Carpetas1.json", 'r') as archivo:
    dic_datos = json.load(archivo)
#guardar datos del archivo en una lista
for c in dic_datos.values():
    carpetas.append(c)
#se guardan los datos especificos desde otra lista de 5 dimenciones
datos_carpetas: list[Carpeta] = []
for c in carpetas:
    archJson = json.dumps(c)
    peso = sys.getsizeof(archJson)
    datos_carpetas.append(Carpeta(c['nombre'],peso))
#impresion con formato
print('{0:2s}  {1:11s} {2:2s}'.format('id:','nombre:','peso:'))
for p in datos_carpetas:
    print('{0:2d} | {1:10s} | {2:2d}'.format(p.getId(),p.getNombre(),p.getPesoTotal()))
print('la longitud del diccionario es:', len(dic_datos))
print('<ahora trasnformamos el dato a tipo json>')
p = json.dumps(carpetas[0])
print('El peso en Bytes es:',sys.getsizeof(p))