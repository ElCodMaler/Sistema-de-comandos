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
sis.mostrar(sis.pc)
print('guaradar raiz')
sis.asignar_raiz("C:",fs)
print('mostar datos del sistema de ficheros desde el sistema')
#se le asigna la el nodo de la unidad de la lista enlazada a una variable
nodoU = sis.buscar_unidad('C:')
print('agregar dato...')
#se asigna una carpeta nueva a la unidad
nodoU.folderS.insertar_Carpeta(Carpeta(5,'Samuel',500))
print(f'las carpetas de la unidad {nodoU}')
#se imprimen los datos en orden de peso total
nodoU.folderS.in_orden(nodoU.folderS.raiz)