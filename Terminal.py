#from elementos_terminal import Fichero, Carpeta, Unidad
#from Comandos import Comando
import json
#clase
# class informacion(Fichero, Carpeta, Unidad, Comando):
#     def crearCarpeta(self):
#         self.carpetas = []
#         self.carpetas.append()
#     def crearUnidad(self,)
#obteniendo datos del archivo Json
with open("datos.json","r") as info:
    datos = info.read()
#decodificando el archivo Json a un diccionario
dict_datos = json.JSONDecoder().decode(datos)
#
for i,j in dict_datos.items():
    print(f'{i}')

    for m, n in j.items():
        print(m)

        # for l, p in n.items():
        #     print(l)


        