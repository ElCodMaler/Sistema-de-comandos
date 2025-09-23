"""
Necesitamos conectar la lista enlazada de nodos N-arios a los nodos binarios,
ya que tienen un orden por alturas, se aprovechara para buscar la profundidad las carpetas
y asi mejorar la estructura del sistema de busqueda de ficheros.
"""
# importamos el arbol binario...
from tools.TDA.trees.tree_binario import DriveDirectory, FolderNode, File

print("Inicio de las  pruebas...")
# generamos varios archivos
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
a3 = File("archivo3.txt","contenido del archivo 3")
a4 = File("archivo4.txt","contenido del archivo 4")
a5 = File("archivo5.txt","contenido del archivo 5")
a6 = File("archivo6.txt","contenido del archivo 6")
a7 = File("archivo7.txt","contenido del archivo 7")
a8 = File("archivo8.txt","contenido del archivo 8")
a9 = File("archivo9.txt","contenido del archivo 9")
a10 = File("archivo10.txt","contenido del archivo 10")
# generamos varios Folders
c1 = FolderNode("carpeta1")
c2 = FolderNode("carpeta2")
c3 = FolderNode("carpeta3")
c4 = FolderNode("carpeta4")
# subfolders
sa = FolderNode("subfolderA")
sb = FolderNode("subfolderB")
sc = FolderNode("subfolderC")
sd = FolderNode("subfolderD")
sE = FolderNode("subfolderE")
sf = FolderNode("subfolderF")
sg = FolderNode("subfolderG")
sh = FolderNode("subfolderH")
si = FolderNode("subfolderI")
sj = FolderNode("subfolderJ")
sk = FolderNode("subfolderK")

# ahora inicializamos el sistema
sys = DriveDirectory(c1)
# insertamos carpetas al nodo binario...
if not sys.add(a1):
    raise ValueError("no se guardo")
if not sys.add(c2):
    raise ValueError("no se guardo")
if not sys.add(c3):
    raise ValueError("no se guardo")
if not sys.add(c4):
    raise ValueError("no se guardo")
if not sys.add(a2):
    raise ValueError("no se guardo")
if not sys.add(a3):
    raise ValueError("no se guardo")
if not sys.add(sa):
    raise ValueError("no se guardo")
if not sys.add(sb):
    raise ValueError("no se guardo")
if not sys.add(a4):
    raise ValueError("no se guardo")
if not sys.add(a5):
    raise ValueError("no se guardo")
if not sys.add(sf):
    raise ValueError("no se guardo")
if not sys.add(a7):
    raise ValueError("no se guardo")

# SALIDAS
print("<==================== SALIDAS ======================>")
sys.imprimir_inorden()
print()
sys.imprimir_preorden()
print()
sys.imprimir_postorden()
print()
sys.imprimir_arbol_visual()
print("<==================== END ======================>")