import json
#INICIALIZACION DE VARIABLES
carpetas = []
datos_carpetas = [[],[],[],[],[]]
#lectura del archivo Json
with open("DataBase\Carpetas.json", 'r') as archivo:
    dic_datos = json.load(archivo)
#guardar datos del archivo en una lista
for c in dic_datos.values():
    carpetas.append(c)
#se guardan los datos especificos desde otra lista de 5 dimenciones
i = 0
for c in carpetas:
    datos_carpetas[i].append(c['id'])
    datos_carpetas[i].append(c['nombre'])
    datos_carpetas[i].append(c['peso'])
    i = 1 + i
#impresion con formato
print('{0:2s}  {1:11s} {2:2s}'.format('id:','nombre:','peso:'))
for p in datos_carpetas:
    print('{0:2d} | {1:10s} | {2:2d}'.format(p[0],p[1],p[2]))
