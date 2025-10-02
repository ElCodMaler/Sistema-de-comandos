from typing import Optional
from templates.linked_lists.stacks import Stack
from templates.file import File
from .drive_folder import Folder
from .tree_binary import Organizer

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
        # caso 1: vuelta a un directorio anterior
        if folder_name == "..":
            self.go_back()
            return
        # caso 2: volver a la raiz
        if self._root.getName() == folder_name:
            self._current_directory = self._root
            self._history = Stack()
            return
        # caso 3: el directorio buscado es una ruta completa... por lo tanto hay que recorrerla
        route_dorectory = folder_name.split('/')
        if len(route_dorectory) > 1:
            if self._current_directory.getChild(route_dorectory[0]):
                current, history = self._route_directory(self._current_directory, self._history, route_dorectory)
            elif self._root.getName() == route_dorectory.pop(0):
                current, history = self._route_directory(self._root, Stack(),route_dorectory)
            if current and history:
                self._current_directory = current
                self._history = history
                return
            print(f'Error: dont found this route directory {folder_name}')
            return
        # caso 4: el folder se encuentra en el hijo del directorio actual
        element: Optional[File | Folder] = self._current_directory.getChild(folder_name)
        
        if element and isinstance(element, Folder):
            self._history.add(self._current_directory)
            self._current_directory = element
        else:
            print(f"Error: Folder '{folder_name}' not found.")
    # pivot route to directorys
    def _route_directory(self, current: Folder, history: Stack[Folder], route: list[str]) -> tuple[Folder | None,Stack[Folder] | None]:
        if route:
            element: Optional[File | Folder] = current.getChild(route.pop(0))

            if element and isinstance(element, Folder):
                history.add(current)
                current = element
                return self._route_directory(current,history,route)
            else:
                print(f"Error: Folder '{element}' not found.")
                return None, None
        return current, history
    
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
            return
        return self._current_directory.deleteChild(name)

    def print_asc(self):
        res = Organizer(self._current_directory)
        res.print_info_inorder()

    def print_desc(self):
        res = Organizer(self._current_directory)
        res.print_info_postorder()
    
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
    
    def delete_multiple_folders(self, folder_list: list[str]):
        if not folder_list:
            return
        self.deleteElement(folder_list.pop())
        self.delete_multiple_folders(folder_list)

    def create_multiple_folders(self, folder_list: list[str]):
        if not folder_list:
            return
        self.createFolder(folder_list.pop(0))
        self.create_multiple_folders(folder_list)