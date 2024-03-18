from components.elementos_sistema import Fichero
from tools.TDA.sistema_ficheros import FileSystem
#ejemplo de su uso
#Creacion de archivos
arch = FileSystem()
arch.crear_archivo(Fichero(1,'archivo1','txt',245,'contenido del archivo1...'))
arch.crear_archivo(Fichero(2,'archivo2','doc',135,'contenido del archivo2...'))
arch.crear_archivo(Fichero(3,'archivo3','exce',600,'contenido del archivo3...'))
arch.crear_archivo(Fichero(4,'archivo4','pdf',346,'contenido del archivo4...'))
arch.crear_archivo(Fichero(5,'archivo5','xmlx',220,'contenido del archivo5...'))
arch.crear_archivo(Fichero(6,'archivo6','txt',462,'contenido del archivo6...'))
"""
#INICIO DEL PROGRAMA
#entrada de datos
var1 = 'archivo3'
#buscamos el nodo donde se encuentra los datos buscados
archivo1 = arch.get_raiz().encontrar_fichero(var1)
#salida de resultados
print('----------- INICIO ------------')
print('El archivo', var1)
try:
    print(f'*Del archivo buscado ({var1}), se encontro-> {archivo1.archivo.getNombre()}')
except:
    print('*No se encontro ningun nodo :/')
print('Impresion de resultados en In-orden:')
#impresion de los ficheros administrados
arch.get_raiz().recorrido_inorden()
print('------ FIN DEL PROGRAMA ------')
"""