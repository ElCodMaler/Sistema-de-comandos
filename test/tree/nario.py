"""
Necesitamos conectar la lista enlazada de nodos N-arios a los nodos binarios,
ya que tienen un orden por alturas, se aprovechara para buscar la profundidad las carpetas
y asi mejorar la estructura del sistema de busqueda de ficheros.
"""
# importamos el arbol binario...
from trees.tree_n_ario import DriveDirectory, FolderNode, File

#funcion
def evaluar_res(res: FolderNode | File | None):
    if not res:
        print(f'No se encontro...')
    elif isinstance(res, FolderNode):
        print(f'Se encontro ({res.getName()})')
    else:
        print(f'se encontro el archivo: {res.getName()}')   

print("Inicio de las  pruebas...")
# generamos varios archivos
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
# Instancia de la funcion
sn = DriveDirectory("carpeta1")
# funciones caracteristicas del objeto
if not sn.add('',a1):
    raise ValueError("NO")
if not sn.add('','carpeta2'):
    raise ValueError("NO")
if not sn.add('','carpeta3'):
    raise ValueError("NO")
if not sn.add('','carpeta4'):
    raise ValueError("NO")
if not sn.add('carpeta4','subfolderA'):
    raise ValueError("NO")
if not sn.add("carpeta2",'subfolderB'):
    raise ValueError("NO")
if not sn.add("carpeta2",a2):
    raise ValueError("NO")
if not sn.add("subfolderA","subfolderC"):
    raise ValueError("NO")
# pruebas de respuestas
res1 = sn.get("carpeta2")
res2 = sn.get("archivo2.txt")
res3 = sn.get("subfolderA")
res4 = sn.get("subfolderC")
# evaluamos respuestas
evaluar_res(res1)
evaluar_res(res2)
evaluar_res(res3)
evaluar_res(res4)

# impresion de resultados
sn.root.print_content()
print()
if sn.delete("carpeta3"):
    print('se elimino la carpeta 3')
print()
sn.root.print_content()
print("<==================== END ======================>")