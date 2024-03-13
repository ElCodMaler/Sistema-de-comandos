from TDA.sistema import Sistema
from tools.elementos_terminal import Unidad, Carpeta
from test.usar_sistema_carpetas import fs
#ejemplo de su uso
#INICIALIZAR sistema
sis = Sistema()
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
sis.crear_ususario('C:','Mi persona Gilberto')
#se busca el nodo para ser asignado a una variable
nodoU = sis.buscar_unidad('C:')
#se asigna una carpeta nueva a la unidad
print('<usamos funciones y accedemos a las variables del sistema de carpetas desde el sistema>')
print(f'el nombre de usuario de la unidad {nodoU.unidad.getNombre()} es: {nodoU.folderS.user.name}')
print('*agregar dato...')
nodoU.folderS.insertar_Carpeta(Carpeta(5,'Samuel',500))
#se imprimen los datos en orden de peso total
print(f'Las carpetas de la unidad {nodoU.unidad.getNombre()} son:')
nodoU.folderS.in_orden(nodoU.folderS.user.raiz)
print('------ FIN DEL PROGRAMA ------')