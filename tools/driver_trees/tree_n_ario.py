from .drive_folder import FolderN, File

# n-ary tree
class DriveDirectory:
    """
    + root: first FolderN
    """
    def __init__(self, name_folder: str):
        self.root = FolderN(name_folder)
        self.current_directory: FolderN = self.root
        self.history: list[FolderN] = []

    # ===================== UTILITIES ======================

    def createFile(self, name:str, content: str = "") -> None:
        """ Creates a new file in the current directory """
        eval_name = name.split('.')
        if len(eval_name) != 2:
            print("No se puede asignar mas de un punto(.) para el name de un archivo.")
            return
        new_file: File = File(eval_name[0],eval_name[1],content)
        self.current_directory.addChild(new_file)
        print(f"Archivo '{new_file.getName()}' creado exitosamente")
    
    def createFolder(self, name: str) -> None:
        """Crea una nueva carpeta en el directorio actual"""
        carpeta: FolderN = FolderN(name)
        self.current_directory.addChild(carpeta)
        print(f"Carpeta '{carpeta.getName()}' creado exitosamente")

    def deleteElement(self, name: str):
        """ delete file or folder by name """
        if self.root.getName() == name:
            print("⚠️ Cannot delete root of DriveDirectory")
        self.current_directory.deleteChild(name)

    def print_info(self) -> None:
        """Lista el contenido del directorio actual"""
        self.current_directory.print_info_children()

    def print_list(self):
        self.current_directory.print_list_chidren()

    def go_back(self):
        if not self.history:
            print("estas en la raiz")
            return
        self.current_directory = self.history.pop()

    def _route_directory(self, node: FolderN, route: list[str]):
        if route:
            child = node.getChild(route[0])
            if child and isinstance(child,FolderN):
                route.pop(0)
                self.history.append(child)
                self._route_directory(child,route)
            else:
                return False
    
    def change_directory(self, folder_name: str) -> None:
        """ Change to a folderN within the current directory """
        # ir un directorio anterior
        if folder_name == "..":
            self.go_back()
            return
        # ir a la raiz
        if self.root.getName() == folder_name:
            self.current_directory = self.root
        # ir varios directorios hacia adelante o hacia atras
        route = folder_name.split('/')
        if len(route) > 1:
            if route[0] == self.root.getName():
                self._route_directory(self.root, route)
            elif self.current_directory.getChild(route[0]):
                self._route_directory(self.current_directory, route)

        # ir un directorio hacia adelante
        element = self.current_directory.getChild(folder_name)
        
        if element and isinstance(element, FolderN):
            if self.current_directory != self.root:
                self.history.append(self.current_directory)
            self.current_directory = element
            print(f"Directorio cambiado a: {element.getName()}/")
        else:
            print(f"Error: Carpeta '{folder_name}' no encontrada")

    def getRoute(self) -> str:
        ls = [folder.getName() for folder in self.history]
        ruta: list[str] = [self.current_directory.getName()]
        for r in ls:
            ruta.append(r)
        return '/'.join(ruta) + '/'

    def printTree(self, node: FolderN| None=None, level: int=0):
        """ recursive tree printing """
        if not node:
            node = self.root
        for son in node.children:
            print(f"{" "*level}- {son.getName()}")
            if isinstance(son,FolderN):
                self.printTree(son,level+1)