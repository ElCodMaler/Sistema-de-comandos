from tools.elementos_terminal import Carpeta
from TDA.sistema_Carpetas import FolderSistem
#INICIO DEL PROGRAMA
#inicio del sistema
fs = FolderSistem()
#asignar carpetas al sistema
fs.insertar_Carpeta(Carpeta(1,'Carlos',15))
fs.insertar_Carpeta(Carpeta(2,'Maria',7))
fs.insertar_Carpeta(Carpeta(3,'Jose',45))
fs.insertar_Carpeta(Carpeta(4,'Luis',11))
fs.insertar_Carpeta(Carpeta(5,'Tulio',23))
fs.insertar_Carpeta(Carpeta(6,'Suli',9))
fs.insertar_Carpeta(Carpeta(7,'Latam',30))
"""
#variables de entrada
r = 'Luis'
ubicacion = 'Carlos/Tulio'
#salida de resultados
print('----------- INICIO ------------')
print('Los datos que estan administrados dentro de la lista enlazada:')
#uso del metodo in_orden
fs.in_orden(fs.raiz)
print('-------------  *  --------------')
#uso del metodo buscar carpeta
r = fs.buscar_carpeta(r,fs.raiz)
print('El valor Raiz es', fs.raiz.carpeta.getNombre())
try:
    print('La carpeta buscada es:',r.carpeta.getNombre())
except:
    print('el resultado es:',r)
print('-------------  *  --------------')
print(f'la ubicacion es ({ubicacion})')
#uso del metodo navegar
ubicacion = fs.navegar(ubicacion)
try:
    print(f'El resultado de la busqueda de la ubicacion es: {ubicacion.carpeta.getNombre()}')
except:
    print('No se encontro la ubicacion')
print('------ FIN DEL PROGRAMA ------')
"""