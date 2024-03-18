from components.elementos_sistema import Carpeta
from tools.TDA.sistema_Carpetas import FolderSystem
from test.usar_sistema_archivos import arch

#inicio del sistema
fs = FolderSystem()
#asignar carpetas al sistema
fs.insertar_Carpeta(Carpeta(1,'Carlos',15))
fs.insertar_Carpeta(Carpeta(2,'Maria',7))
fs.insertar_Carpeta(Carpeta(3,'Jose',45))
fs.insertar_Carpeta(Carpeta(4,'Luis',11))
fs.insertar_Carpeta(Carpeta(5,'Tulio',23))
fs.insertar_Carpeta(Carpeta(6,'Suli',9))
fs.insertar_Carpeta(Carpeta(7,'Latam',30))
"""
#usar sistema de ficheros desde el sistema de carpetas
fs.setUser('mi usuario')
fs.asignarFileSystem('Luis',arch)
#INICIO DEL PROGRAMA
#variables de entrada
r = 'Luis'
ubicacion = None
flujo = None
#salida de resultados
print('----------- INICIO ------------')
print('Los datos que estan administrados dentro de la lista enlazada:')
#uso del metodo in_orden
fs.in_orden(fs.getUser())
print('-------------  *  --------------')
#uso del metodo buscar carpeta
r = fs.buscar_carpeta(r,fs.raiz)
print('El usuario es:', fs.getUser().carpeta.getNombre())
try:
    print('La carpeta buscada es:',r.carpeta.getNombre())
except:
    print('el resultado es:',r)
print('-------------  *  --------------')
flujo = "y"
ubicacion = fs.raiz
while True:
    #uso del metodo de opciones disponobles
    op1, op2 = fs.opciones_nav(ubicacion)
    try:
        print('opciones disponibles:',op1.carpeta.getNombre())
        print('  {0:17s}'.format(op2.carpeta.getNombre()))
    except:
        print('no se encuentran opciones...')
    buscar = input('Introduzca Ubicacion buscada>')
    print(f'la ubicacion es ({buscar})')
    #uso del metodo navegar
    ubicacion = fs.navegar(buscar)
    try:
        print(f'El resultado de la busqueda de la ubicacion es: {ubicacion.carpeta.getNombre()}')
    except:
        print('No se encontro la ubicacion')
    try:
        print('El sistema de archivos es:',ubicacion.fileS.get_raiz().archivo.getNombre())
    except:
        print('No se hallo ninguna raiz de archivos...')
    flujo = input('desea seguir? (S/N)->>')
    if flujo == 'n' or flujo == 'N':
        break
print('------ FIN DEL PROGRAMA ------')
"""