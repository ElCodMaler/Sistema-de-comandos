from tools.elementos_terminal import Carpeta
from TDA.sistema_Carpetas import FolderSistem

#ejemplo
#inicio del sistema
fs = FolderSistem('Manolo')
fs.insertar_Carpeta(Carpeta(1,'Carlos',15))
fs.insertar_Carpeta(Carpeta(2,'Maria',7))
fs.insertar_Carpeta(Carpeta(3,'Jose',45))
fs.insertar_Carpeta(Carpeta(4,'Latam',11))
#variables
r = 'Jose'
#INICIO DEL PROGRAMA
print('los datos que estan administrados dentro de la lista enlazada')
fs.in_orden(fs.raiz)
print('----------*-------------')
r = fs.buscar_carpeta(r,fs.raiz)
try:
    print('mostrar el dato buscado:',r.carpeta.getNombre())
except:
    print('el resultado es:',r)

