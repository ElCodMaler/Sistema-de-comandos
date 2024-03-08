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
r = 'Latam'
#salida de resultados
print('Los datos que estan administrados dentro de la lista enlazada')
print()
fs.in_orden(fs.user)
print('-------------  *  --------------')
r = fs.buscar_carpeta(r,fs.user)
try:
    print('mostrar el dato buscado:',r.carpeta.getNombre())
except:
    print('el resultado es:',r)
print('uso del metodo navegar....')
ubicacion = fs.navegar('Manolo')
try:
    print('mostrar el dato buscado:',ubicacion.carpeta.getNombre())
except:
    print('el resultado es:',ubicacion)