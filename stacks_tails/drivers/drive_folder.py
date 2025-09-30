from typing import Union, Optional
from stacks_tails.tails import Tail
from templates.file import File
from templates.folder import Folder

class FolderN(Folder):
    """
    + name: name that identifies the Folder object.
    + children: instance of the Tail to Files and Folders.
    + weight: the weight that the contents of the folder represent.
    + date_create: creation date of the current object.
    + date_modify: folder modification date.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: Tail[Union['File', 'FolderN']] = Tail()
        self._weight = 0

    # -------- Protected functions --------
    
    def _existing_element(self, name: str):
        current = self.children.getHead()
        while current:
            if current.value.getName() == name:
                return True
            current = current.next
        return False
    
    def _get_list_children(self) -> list[Union['File', 'FolderN']]:
        # inicializar variables
        tail_temp: Tail[Union[File, FolderN]] = Tail()
        children_ls: list[Union['File', 'FolderN']] = []
        # recorrer lista
        while not self.children.is_empty():
            value = self.children.remove()
            tail_temp.add(value)
            children_ls.append(value)
        # Restore the original Stack
        while not tail_temp.is_empty():
            self.children.add(tail_temp.remove())
        return children_ls

    # =============== UTILITIES ===============
    
    def addChild(self, element: Union['File', 'FolderN']):
        """ Add a file or folder to this folder """
        if self._existing_element(element.getName()):
            print('Sorry, this item already exists in this list.')
            return
        self.children.add(element)
        self.update_modify()
        self._weight += element.getWeight()
    
    def deleteChild(self, name: str):
        """ Removes the last element added (LIFO) """
        if self.children.is_empty():
            return
        # inicializar variables
        tail_temp: Tail[Union[File, FolderN]] = Tail()
        # recorrer lista
        while not self.children.is_empty():
            value = self.children.remove()
            if value.getName() == name:
                self._weight -= value.getWeight()
                continue
            else:
                tail_temp.add(value)
        # Restore the original Stack
        while not tail_temp.is_empty():
            self.children.add(tail_temp.remove())
    
    def getChild(self, name: str) -> Optional[Union['File', 'FolderN']]:
        """ Search for an item by name in the folder """
        if self.children.is_empty():
            return
        for child in self._get_list_children():
            if child.getName() == name:
                return child
            
    def print_list_chidren(self):
        for child in self._get_list_children():
            print(child.getName(),end=' ')

    def print_info_children(self):
        for child in self._get_list_children():
            print(str(child))