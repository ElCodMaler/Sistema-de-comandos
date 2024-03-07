from tools.elementos_terminal import Carpeta
from TDA.sistema_Carpetas import FolderSistem
#INICIO DEL PROGRAMA
#inicio del sistema
fs = FolderSistem('Manolo')
#asignar carpetas al sistema
fs.insertar_Carpeta(Carpeta(1,'Carlos',15))
fs.insertar_Carpeta(Carpeta(2,'Maria',7))
fs.insertar_Carpeta(Carpeta(3,'Jose',45))
fs.insertar_Carpeta(Carpeta(4,'Latam',11))
#variables
r = 'Jose'
#salida de resultados
print('los datos que estan administrados dentro de la lista enlazada')
fs.in_orden(fs.user)
print('----------*-------------')
r = fs.buscar_carpeta(r,fs.user)
try:
    print('mostrar el dato buscado:',r.carpeta.getNombre())
except:
    print('el resultado es:',r)