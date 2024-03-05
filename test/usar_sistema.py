from TDA.sistema_Unidades import Sistema
from tools.elementos_terminal import Unidad
from test.usar_arbol_binario import fs
#ejemplo de su uso
sis = Sistema()
sis.agregar_unidad(Unidad(1,"C:",800,500,None,'SSD'))
sis.agregar_unidad(Unidad(2,"USB:",500,150,None,"T2"))
sis.agregar_unidad(Unidad(3,"U:",300,100,None,"HDD"))
sis.mostrar(sis.pc)
print('guaradar raiz')
sis.asignar_raiz("C:",fs)
print('mostar datos des sistema de ficheros desde el sistema')
nodo = sis.buscar_unidad('C:')
nodo.raiz_fs.in_orden(nodo.raiz_fs.raiz)
