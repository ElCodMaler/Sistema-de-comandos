from tools.Sistema import BaseDatos
import json
#INICIALIZANDO VARIABLES
#obteniendo datos del archivo Json
docJ = r'DatosJson\Carpetas.json'
with open(docJ,"r") as info:
    datos = info.read()
#decodificando el archivo Json a un diccionario
dict_datos = json.JSONDecoder().decode(datos)
#INICIO DEL PROGRAMA
b = BaseDatos(dict_datos)
