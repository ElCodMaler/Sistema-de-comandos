from typing import Optional, List, Union
from stacks_tails.drive_folder import FolderN, File, Stack

class SistemaArchivos:
    """Sistema principal de gestión de archivos y carpetas"""
    
    def __init__(self) -> None:
        self.root: FolderN = FolderN("raiz")
        self._current_directory: FolderN = self.root
        self._history: Stack[FolderN] = Stack()
    
    def createFile(self, name:str, content: str = "") -> None:
        """ Creates a new file in the current directory """
        eval_name = name.split('.')
        if len(eval_name) > 2:
            print("No se puede asignar mas de un punto(.) para el name de un archivo.")
            return
        new_file: File = File(eval_name[0],eval_name[1],content)
        self._current_directory.addChild(new_file)
        print(f"Archivo '{new_file.getName()}' creado exitosamente")
    
    def createFolder(self, name: str) -> None:
        """Crea una nueva carpeta en el directorio actual"""
        carpeta: FolderN = FolderN(name)
        self._current_directory.addChild(carpeta)
        print(f"Carpeta '{name}/' creada exitosamente")
    
    def print_list(self) -> None:
        """Lista el contenido del directorio actual"""
        self._current_directory.print_content()
    
    def change_directory(self, name_folderN: str) -> None:
        """ Change to a folderN within the current directory """
        if name_folderN == "..":
            self.go_back()
            return
        
        element: Optional[Union[File, FolderN]] = self._current_directory.search_element(name_folderN)
        
        if element and isinstance(element, FolderN):
            self._history.add(self._current_directory)
            self._current_directory = element
            print(f"Directorio cambiado a: {element.getName()}/")
        else:
            print(f"Error: Carpeta '{name_folderN}' no encontrada")
    
    def go_back(self) -> None:
        """ Go back to the previous directory """
        if self._history.is_empty():
            print("Ya estás en el directorio raíz")
            return
        
        self._current_directory = self._history.remove()
        print(f"Directorio cambiado a: {self._current_directory.getName()}/")
    
    def delete_last(self) -> None:
        """ Removes the last item added to the current directory """
        element: Optional[Union[File, FolderN]] = self._current_directory.delete_last()
        if element:
            type: str = "<file>" if isinstance(element, File) else "<folder>"
            name: str = element.getName()
            print(f"{type} '{name}' eliminado exitosamente")
        else:
            print("No hay elements para eliminar")
    
    def search(self, name: str) -> None:
        """ Search for an item in the current directory """
        element: Optional[Union[File, FolderN]] = self._current_directory.search_element(name)
        if element:
            type: str = "Archivo" if isinstance(element, File) else "Carpeta"
            print(f"Element encontrado: {type} - {element}")
        else:
            print(f"Element '{name}' no encontrado")
    
    def show_current_route(self) -> None:
        """Muestra la ruta completa actual"""
        ruta: List[str] = [self._current_directory.getName()]
        temp_historial: Stack[FolderN] = Stack()
        
        # Reconstruir la ruta desde el historial
        while not self._history.is_empty():
            dir_temp: FolderN = self._history.remove()
            temp_historial.add(dir_temp)
            ruta.insert(0, dir_temp.getName())
        
        # Restaurar el historial
        while not temp_historial.is_empty():
            self._history.add(temp_historial.remove())
        
        print("Ruta actual: /" + "/".join(ruta))