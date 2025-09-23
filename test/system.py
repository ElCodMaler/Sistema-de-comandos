"""
Necesitamos conectar la lista enlazada de nodos N-arios a los nodos binarios,
ya que tienen un orden por alturas, se aprovechara para buscar la profundidad las carpetas
y asi mejorar la estructura del sistema de busqueda de ficheros.
"""
# importamos el arbol binario...
from templates.file import File
from templates.unity import Unity
from tools.TDA.trees.tree_binario import DriveDirectory

#funcion
def evaluar_res(res: DriveDirectory | File | None):
    if not res:
        print(f'No se encontro...')
    elif isinstance(res, DriveDirectory):
        print(f'Se encontro ({res.raiz.directory.getName()})')
        res.imprimir_inorden()
        print()
        res.imprimir_postorden()
        print()
        res.imprimir_preorden()
        print()
    else:
        print(f'se encontro el archivo: {res.getName()}')   

print("Inicio de las  pruebas...")
# generamos varios archivos
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
# Instancia del objeto Unidad
system = Unity("C",1240)
# funciones caracteristicas del objeto
if not system.drive_folder.add('',a1):
    raise ValueError("NO")
if not system.drive_folder.add('','carpeta2'):
    raise ValueError("NO")
if not system.drive_folder.add('','carpeta3'):
    raise ValueError("NO")
if not system.drive_folder.add('','carpeta4'):
    raise ValueError("NO")
if not system.drive_folder.add('carpeta4','subfolderA'):
    raise ValueError("NO")
if not system.drive_folder.add("carpeta2",'subfolderB'):
    raise ValueError("NO")
if not system.drive_folder.add("carpeta2",a2):
    raise ValueError("NO")
if not system.drive_folder.add("subfolderA","subfolderC"):
    raise ValueError("NO")
# pruebas de respuestas
res1 = system.drive_folder.get("carpeta3")
res2 = system.drive_folder.get("archivo2.txt")
res3 = system.drive_folder.get("subfolderA")
res4 = system.drive_folder.get("subfolderC")
# evaluamos respuestas
if not res1:
    print("no encontro la carpeta 3")
if not res2:
    print("no encontro el archivo 2")
if not res3:
    print("no encontro el SubFolderA")
if not res4:
    print("no encontro el SubFolderC")
# impresion de resultados
system.drive_folder.raiz.print_content()
evaluar_res(res1)
evaluar_res(res2)
evaluar_res(res3)
evaluar_res(res4)

if system.drive_folder.delete("carpeta3"):
    print('se elimino la carpeta 3')

res4.imprimir_postorden()

system.drive_folder.raiz.print_content()
print("<==================== END ======================>")