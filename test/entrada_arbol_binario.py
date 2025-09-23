from tools.TDA.trees.tree_binario import DriveDirectory, FolderNode, File

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

folder.addChild(a1)
folder.addChild(a2)
folder.addChild(a3)
folder.addChild(a4)
folder.addChild(c1)
folder.addChild(c2)
folder.addChild(c3)
folder.addChild(a5)
# empezamos a usar la funciones de DriveDirectory
sys = DriveDirectory(folder)
sys.imprimir_inorden()
sys.imprimir_postorden()