from .nodos.folder_node import FolderNode
from templates.file import File

#clase Arbol N-ario
class DriveSystem:
    """
    + raiz: el primer FolderNode
    """
    def __init__(self, name_folder: str):
        self.raiz = FolderNode(name_folder)

    # ----------- Encontrar nodo (Búsqueda en profundidad) -----------
    
    def get(self, name: str, nodo: FolderNode | None=None) -> FolderNode| File | None:
        if not nodo:
            nodo = self.raiz
        if nodo.getName() == name:
            return nodo
        for hijo in nodo.childs:
            if hijo.getName() == name:
                if isinstance(hijo, FolderNode):
                    return hijo
                return hijo
            if isinstance(hijo, FolderNode):
                resultado = self.get(name, hijo)
                if resultado:
                    return resultado
        return None

    # ----------- Agregar nodo -----------
    def add(self, folder_padre:str='', new_hijo:File | str='') -> bool:
        if new_hijo == '':
            print("el argumento del hijo no puede estar vacio...")
            return False
        if folder_padre == '':
            folder_padre = self.raiz.getName()
        padre = self.get(folder_padre)
        if isinstance(padre,File):
            print(f"⚠️ No se puede asignar un File o Folder a un archivo: {new_hijo}")
        elif isinstance(padre,FolderNode):
            if isinstance(new_hijo,str):
                padre.addChild(FolderNode(new_hijo))
            else:
                padre.addChild(new_hijo)
        return True
    # ----------- Eliminar nodo -----------
    def delete(self, file_name: str):
        if self.raiz.getName() == file_name:
            print("⚠️ No se puede eliminar la raíz del Folder System")
            return False
        return self._eliminar_recursivo(self.raiz, file_name)

    def _eliminar_recursivo(self, nodo: FolderNode, file_name: str):
        for i, hijo in enumerate(nodo.childs):
            if hijo.getName() == file_name:
                nodo.childs.pop(i)  # elimina el hijo (y todos sus descendientes)
                return True
            elif isinstance(hijo, FolderNode):
                if self._eliminar_recursivo(hijo, file_name):
                    return True
        return False
    # ----------- Imprimir árbol (recursivo) -----------
    def imprimir(self, nodo: FolderNode| None=None, level: int=0):
        if not nodo:
            nodo = self.raiz
        
        for hijo in nodo.childs:
            print(f"{" "*level}- {hijo.getName()}")
            if isinstance(hijo,FolderNode):
                self.imprimir(hijo,level+1)