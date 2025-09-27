"""
Necesitamos conectar la lista enlazada de nodos N-arios a los nodos binarios,
ya que tienen un orden por alturas, se aprovechara para buscar la profundidad las carpetas
y asi mejorar la estructura del sistema de busqueda de ficheros.
"""
# importamos el arbol binario...
from trees.tree_binario import Organizer, FolderNode, File

print("Inicio de las  pruebas...")
# crear padre
folder = FolderNode("C")

# generar valores hijo
c1 = FolderNode("carpeta1")
c2 = FolderNode("carpeta2")
c3 = FolderNode("carpeta3")
c4 = FolderNode("carpeta4")
c5 = FolderNode("carpeta5")
c6 = FolderNode("carpeta6")
# generamos varios archivos
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
a3 = File("archivo3.txt","contenido del archivo 3")
a4 = File("archivo4.txt","contenido del archivo 4")
a5 = File("archivo5.txt","contenido del archivo 5")
a6 = File("archivo6.txt","contenido del archivo 6")
# agregamos hijos al padre
folder.addChild(a1)
folder.addChild(a2)
folder.addChild(a3)
folder.addChild(a4)
folder.addChild(c1)
folder.addChild(c2)
folder.addChild(c3)
folder.addChild(a5)
# empezamos a usar la funciones de la clase Organizer
sys = Organizer(folder)

# SALIDAS
print("<==================== SALIDAS ======================>")
print("salida de la funcion inorden")
sys.print_info_inorder()
print("salida de la funcion postorden")
sys.print_info_postorder()
print("salida de la funcion preorden")
sys.print_info_preorder()
print("salida de la funcion list")
sys.print_list()
print("<==================== END ======================>")