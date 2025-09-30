from stacks_tails.drivers.drive_folder import FolderN
# generar carpeta
carpeta = FolderN("Carpeta")
# generamos mas carpetas
c1 = FolderN("carpeta1")
c2 = FolderN("carpeta2")
c3 = FolderN("carpeta3")
# agregar carpeta a la carpeta raiz
carpeta.addChild(c1)
carpeta.addChild(c2)
carpeta.addChild(c3)

#imprimir contenido de la carpeta
carpeta.print_content()

res = carpeta.search_element("carpeta2")
if res:
    print(str(res))