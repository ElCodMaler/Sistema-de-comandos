from tools.TDA.trees.nodos.folder_node import FolderNode
from templates.file import File

#files
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
a3 = File("archivo3.txt","contenido del archivo 3")
a4 = File("archivo4.txt","contenido del archivo 4")

folder = FolderNode('carpeta1')

folder.addChild(a1)
folder.addChild(a2)
folder.addChild(a3)
folder.addChild(a4)

folder.info()

folder.print_content()