from stacks_tails.drivers.drive_folder import FolderN, Stack, File
from typing import Union, Optional

# ============= CLASS DRIVE DIRECTORY ============
class DriveDirectory:
    """
    + root: Folder raiz del sistema
    + current_directory: el folder actual
    + history: lista enlazada de Folders
    """
    def __init__(self, name: str) -> None:
        self.root: FolderN = FolderN(name)
        self.current_directory: FolderN = self.root
        self.history: Stack[FolderN] = Stack()
    # ============ UTILITIES ============
    def createFile(self, name:str, content: str = "") -> None:
        """ Creates a new file in the current directory """
        eval_name = name.split('.')
        if len(eval_name) > 2:
            print("No se puede asignar mas de un punto(.) para el name de un archivo.")
            return
        new_file: File = File(eval_name[0],eval_name[1],content)
        self.current_directory.addChild(new_file)
        print(f"Archivo '{new_file.getName()}' creado exitosamente")
    
    def createFolder(self, name: str) -> None:
        """Crea una nueva carpeta en el directorio actual"""
        carpeta: FolderN = FolderN(name)
        self.current_directory.addChild(carpeta)
        print(f"Carpeta '{name}/' creada exitosamente")

    def print_history(self):
        print("historial")
        print(str(self.history))
        print('directorio actual:',self.current_directory.getName())
        print(str(self.current_directory.getName()))
        print('el contenido de la raiz es:')
        print(str(self.current_directory.children))

    def change_directory(self, name_folderN: str) -> None:
        """ Change to a folderN within the current directory """
        if name_folderN == "..":
            self.go_back()
            return
        
        element: Optional[Union[File, FolderN]] = self.current_directory.getElement(name_folderN)
        
        if element and isinstance(element, FolderN):
            self.history.add(self.current_directory)
            self.current_directory = element
            print(f"Directorio cambiado a: {element.getName()}/")
        else:
            print(f"Error: Carpeta '{name_folderN}' no encontrada")

    def go_back(self) -> None:
        """ Go back to the previous directory """
        if self.history.is_empty():
            print("Ya estás en el directorio raíz")
            return
        
        self.current_directory = self.history.remove()
        print(f"Directorio cambiado a: {self.current_directory.getName()}/")

    def route_list(self) -> list[str]:
        """Muestra la ruta completa actual"""
        ruta: list[str] = [self.root.getName()]
        temp_historial: Stack[FolderN] = Stack()
        
        # Reconstruir la ruta desde el historial
        while not self.history.is_empty():
            dir_temp: FolderN = self.history.remove()
            temp_historial.add(dir_temp)
            ruta.insert(0, dir_temp.getName())
        
        # Restaurar el historial
        while not temp_historial.is_empty():
            self.history.add(temp_historial.remove())

        return ruta
    def search(self, name: str) -> None:
        """ Search for an item in the current directory """
        element: Optional[Union[File, FolderN]] = self.current_directory.getElement(name)
        if element:
            type: str = "Archivo" if isinstance(element, File) else "Carpeta"
            print(f"Element encontrado: {type} - {element}")
        else:
            print(f"Element '{name}' no encontrado")
        

# INICIO DEL PROGRAMA
d = DriveDirectory('C')
d.createFolder("carpeta1")
d.createFolder("carpeta2")
d.print_history()
d.change_directory("carpeta1")
d.print_history()