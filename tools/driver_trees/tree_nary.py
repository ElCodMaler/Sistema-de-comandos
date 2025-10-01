from .drive_folder import FolderN, File

# n-ary tree
class DriveDirectory:
    """
    + root: main directory.
    + current_directory: directory that changes depending on navigation.
    + history: list of directories used.
    """
    def __init__(self, name_folder: str):
        self._root = FolderN(name_folder)
        self._current_directory: FolderN = self._root
        self._history: list[FolderN] = []

    # ===================== UTILITIES ======================

    def getCurrentDirectory(self):
        return self._current_directory

    def createFile(self, name:str, content: str = "") -> None:
        """ Creates a new file in the current directory """
        eval_name = name.split('.')
        if len(eval_name) != 2:
            print("You cannot assign more than one period (.) to a file name.")
            return
        new_file: File = File(eval_name[0],eval_name[1],content)
        self._current_directory.addChild(new_file)
        print(f"File '{new_file.getName()}' created successfully")
    
    def createFolder(self, name: str) -> None:
        """ Create a new folder in the current directory """
        new_folder: FolderN = FolderN(name)
        self._current_directory.addChild(new_folder)
        print(f"Folder '{new_folder.getName()}' created successfully")

    def deleteElement(self, name: str):
        """ delete file or folder from this folder """
        if self._root.getName() == name:
            print("⚠️ Cannot delete root of DriveDirectory")
        self._current_directory.deleteChild(name)

    def print_info(self) -> None:
        """ Output to console the detailed data of the contents of this Folder """
        self._current_directory.print_info_children()

    def print_list(self):
        """ Console output of the names of the contents of this Folder """
        self._current_directory.print_list_chidren()

    def go_back(self):
        """ Go back to the previous directory """
        if not self._history:
            print("You are now in the root directory.")
            return
        self._current_directory = self._history.pop()

    def _route_directory(self, node: FolderN, route: list[str]):
        """ route of the entered route """
        if route:
            child = node.getChild(route[0])
            if child and isinstance(child,FolderN):
                route.pop(0)
                self._history.append(child)
                self._route_directory(child,route)
            else:
                return False
    
    def change_directory(self, folder_name: str) -> None:
        """ change the current directory value and update the history """
        # ir un directorio anterior
        if folder_name == "..":
            self.go_back()
            return
        # ir a la raiz
        if self._root.getName() == folder_name:
            self._current_directory = self._root
        # ir varios directorios hacia adelante o hacia atras
        route = folder_name.split('/')
        if len(route) > 1:
            if route[0] == self._root.getName():
                self._route_directory(self._root, route)
            elif self._current_directory.getChild(route[0]):
                self._route_directory(self._current_directory, route)

        # ir un directorio hacia adelante
        element = self._current_directory.getChild(folder_name)
        
        if element and isinstance(element, FolderN):
            if self._current_directory != self._root:
                self._history.append(self._current_directory)
            self._current_directory = element
            print(f"Directory changed to: {element.getName()}/")
        else:
            print(f"Error: Folder '{folder_name}' not found.")

    def getRoute(self) -> str:
        """ get the path of the current directory """
        ls = [folder.getName() for folder in self._history]
        ruta: list[str] = [self._current_directory.getName()]
        for r in ls:
            ruta.append(r)
        return '/'.join(ruta) + '/'

    def printTree(self, node: FolderN| None=None, level: int=0):
        """ recursive tree printing """
        if not node:
            node = self._root
        for son in node.children:
            print(f"{" "*level}- {son.getName()}")
            if isinstance(son,FolderN):
                self.printTree(son,level+1)