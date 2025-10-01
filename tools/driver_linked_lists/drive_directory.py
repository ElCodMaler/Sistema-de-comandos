from typing import Optional
from templates.linked_lists.stacks import Stack
from .drive_folder import FolderN, File

class DriveDirectory:
    """Sistema principal de gestión de archivos y carpetas"""
    
    def __init__(self, name: str) -> None:
        self.root: FolderN = FolderN(name)
        self._current_directory: FolderN = self.root
        self._history: Stack[FolderN] = Stack()
    
    def createFile(self, name:str, content: str = "") -> None:
        """ Creates a new file in the current directory """
        eval_name = name.split('.')

        if len(eval_name) != 2:
            print("No se puede asignar mas de un punto(.) para el name de un archivo.")
            return
        new_file: File = File(eval_name[0],eval_name[1],content)
        self._current_directory.addChild(new_file)
        print(f"Archivo '{new_file.getName()}' creado exitosamente")
    
    def createFolder(self, name: str) -> None:
        """Crea una nueva carpeta en el directorio actual"""
        carpeta: FolderN = FolderN(name)
        self._current_directory.addChild(carpeta)
        print(f"Carpeta '{carpeta.getName()}' creado exitosamente")
    
    def print_info(self) -> None:
        """Lista el contenido del directorio actual"""
        self._current_directory.print_info_children()

    def print_list(self):
        self._current_directory.print_list_chidren()
    
    def change_directory(self, folder_name: str) -> None:
        """ Change to a folderN within the current directory """
        if folder_name == "..":
            self.go_back()
            return
        
        element: Optional[File | FolderN] = self._current_directory.getChild(folder_name)
        
        if element and isinstance(element, FolderN):
            self._history.add(self._current_directory)
            self._current_directory = element
            print(f"Directorio cambiado a: {element.getName()}/")
        else:
            print(f"Error: Carpeta '{folder_name}' no encontrada")
    
    def go_back(self) -> None:
        """ Go back to the previous directory """
        if self._history.is_empty():
            print("Ya estás en el directorio raíz")
            return
        
        self._current_directory = self._history.remove()
        print(f"Directorio cambiado a: {self._current_directory.getName()}/")

    def deleteElement(self, name: str):
        self._current_directory.deleteChild(name)
    
    def show_current_route(self) -> str:
        """Muestra la ruta completa actual"""
        ruta: list[str] = [self._current_directory.getName()]
        temp_historial: Stack[FolderN] = Stack()
        
        # Reconstruir la ruta desde el historial
        while not self._history.is_empty():
            dir_temp: FolderN = self._history.remove()
            temp_historial.add(dir_temp)
            ruta.insert(0, dir_temp.getName())
        
        # Restaurar el historial
        while not temp_historial.is_empty():
            self._history.add(temp_historial.remove())
 
        return "/".join(ruta)+'/'