from Sistema import baseDatos
import json
#INICIALIZANDO VARIABLES
#obteniendo datos del archivo Json
with open("datos.json","r") as info:
    datos = info.read()
#decodificando el archivo Json a un diccionario
dict_datos = json.JSONDecoder().decode(datos)
#INICIO DEL PROGRAMA

print(dict_datos)