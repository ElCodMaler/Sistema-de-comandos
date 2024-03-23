from tools.TDA.arboles.sistema import System
from components.elementos_sistema import Unidad, Carpeta
from test.arboles.usar_sistema_carpetas import fs
from test.arboles.usar_sistema_archivos import arch

#ejemplo de su uso
#INICIALIZAR sistema
sis = System()
#agregar unidades
sis.agregar_unidad(Unidad(1,"C:",800,500,None,'SSD'))
sis.agregar_unidad(Unidad(2,"USB:",500,150,None,"T2"))
sis.agregar_unidad(Unidad(3,"U:",300,100,None,"HDD"))
#mostrar unidades en orden
print('----------- INICIO ------------')
print('Unidades existentes:')
sis.mostrar(sis.pc)
#se le asigna un folder system a la unidad especificada
print('*guaradar raiz...')
sis.asignar_raiz("C:",fs)
#asignamos un usuario al sistema
sis.crear_usuario('C:','Mi persona Gilberto')
#se busca el nodo para ser asignado a una variable
nodoU = sis.buscar_unidad('C:')
#se asigna una carpeta nueva a la unidad
print('<usamos funciones y accedemos a las variables del sistema de carpetas desde el sistema>')
if len(nodoU.folderS) > 0:
    for usuario in nodoU.folderS:
        print(f'el nombre de usuario de la unidad {nodoU.unidad.getNombre()} es: {usuario.getUserName()}')
print('*agregar dato...')
nodoU.folderS[0].insertar_Carpeta(Carpeta(5,'Samuel',500))
#se imprimen los datos en orden de peso total
print(f'Las carpetas de la unidad {nodoU.unidad.getNombre()} son:')
if len(nodoU.folderS) > 0:
    for usuario in nodoU.folderS:
        usuario.in_orden(usuario.getUser())
#asignar sistema de archivos a una carpeta del sistema de carpetas
nodoU.folderS[0].asignarFileSystem('Luis',arch)
print('El nombre de usuario es:',nodoU.folderS[0].getUserName())
print('<usamos funciones y accedemos a las variables del sistema de ficheros desde el sistema>')
print('impresion de los archivos:')
nodoU.folderS[0].getFileSystem('Luis').recorrido_inorden()
print('------ FIN DEL PROGRAMA ------')