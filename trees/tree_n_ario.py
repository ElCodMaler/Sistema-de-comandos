from trees.nodos.folder_node import FolderNode, File

# n-ary tree
class DriveDirectory:
    """
    + root: first FolderNode
    """
    def __init__(self, name_folder: str):
        self.root = FolderNode(name_folder)

    # ===================== UTILITIES ======================

    def get(self, name: str, node: FolderNode | None=None) -> FolderNode | File | None:
        """ get a file or folder by its name """
        if not node:
            node = self.root
        if node.getName() == name:
            return node
        for son in node.children:
            if son.getName() == name:
                if isinstance(son, FolderNode):
                    return son
                return son
            if isinstance(son, FolderNode):
                resultado = self.get(name, son)
                if resultado:
                    return resultado
        return None

    def add(self, parent_folder:str='', new_son:File | str='') -> bool:
        """ 
        Add a new file or folder by following these steps:
        + Folder: str
        + File: File object
        """
        if new_son == '':
            print("the son's argument cannot be empty...")
            return False
        if parent_folder == '':
            parent_folder = self.root.getName()
        father = self.get(parent_folder)
        if isinstance(father,File):
            print(f"⚠️ Cannot assign a File or Folder to file: {new_son}")
        elif isinstance(father,FolderNode):
            if isinstance(new_son,str):
                father.addChild(FolderNode(new_son))
            else:
                father.addChild(new_son)
        return True

    def delete(self, name: str):
        """ delete file or folder by name """
        if self.root.getName() == name:
            print("⚠️ Cannot delete root of DriveDirectory")
            return False
        return self._delete_recursive(self.root, name)
    # pivot delete recursive
    def _delete_recursive(self, node: FolderNode, name: str):
        for i, son in enumerate(node.children):
            if son.getName() == name:
                node.children.pop(i)  # elimina el son (y todos sus descendientes)
                return True
            elif isinstance(son, FolderNode):
                if self._delete_recursive(son, name):
                    return True
        return False

    def printTree(self, node: FolderNode| None=None, level: int=0):
        """ recursive tree printing """
        if not node:
            node = self.root
        for son in node.children:
            print(f"{" "*level}- {son.getName()}")
            if isinstance(son,FolderNode):
                self.printTree(son,level+1)