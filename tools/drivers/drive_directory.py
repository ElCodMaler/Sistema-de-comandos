from typing import Optional
from templates.linked_lists.stacks import Stack
from templates.file import File
from .drive_folder import Folder

class DriveDirectory:
    """
    + root: main directory.
    + current_directory: directory that changes depending on navigation.
    + history: list of directories used.
    """
    def __init__(self, name: str):
        self._root: Folder = Folder(name)
        self._current_directory: Folder = self._root
        self._history: Stack[Folder] = Stack()

    def getElement(self, name: str) -> Optional[Folder | File]:
        """ return the searched element """
        return self._current_directory.getChild(name)
    
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
        new_folder: Folder = Folder(name)
        self._current_directory.addChild(new_folder)
        print(f"Folder '{new_folder.getName()}' created successfully")
    
    def print_info(self) -> None:
        """ Output to console the detailed data of the contents of this Folder """
        self._current_directory.print_info_children()

    def print_list(self):
        """ Console output of the names of the contents of this Folder """
        self._current_directory.print_list_chidren()
    
    def change_directory(self, folder_name: str) -> None:
        """ change the current directory value and update the history """
        if folder_name == "..":
            self.go_back()
            return
        
        element: Optional[File | Folder] = self._current_directory.getChild(folder_name)
        
        if element and isinstance(element, Folder):
            self._history.add(self._current_directory)
            self._current_directory = element
            print(f"Directory changed to: {element.getName()}/")
        else:
            print(f"Error: Folder '{folder_name}' not found.")
    
    def go_back(self) -> None:
        """ Go back to the previous directory """
        if self._history.is_empty():
            print("You are now in the root directory.")
            return
        
        self._current_directory = self._history.remove()
        print(f"Directory changed to: {self._current_directory.getName()}/")

    def deleteElement(self, name: str):
        """ delete file or folder from this folder """
        if self._root.getName() == name:
            print("⚠️ Cannot delete root of DriveDirectory")
        self._current_directory.deleteChild(name)
    
    def show_current_route(self) -> str:
        """ Displays the current full path """
        path: list[str] = [self._current_directory.getName()]
        temp_history: Stack[Folder] = Stack()
        
        # Reconstruir la ruta desde el historial
        while not self._history.is_empty():
            dir_temp: Folder = self._history.remove()
            temp_history.add(dir_temp)
            path.insert(0, dir_temp.getName())
        
        # Restaurar el historial
        while not temp_history.is_empty():
            self._history.add(temp_history.remove())
 
        return "/".join(path)+'/'