from typing import Union, Optional
from templates.linked_lists.tails import Tail
from templates.file import File
from templates.folder import Folder

class FolderN(Folder):
    """
    + name: name that identifies the Folder object.
    + children: linked list of Tails that stores Folders and Files
    + weight: the weight that the contents of the folder represent.
    + date_create: creation date of the current object.
    + date_modify: folder modification date.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: Tail[FolderN | File] = Tail()
        self._weight = 0

    # -------- Protected functions --------
    
    def _existing_element(self, name: str) -> bool:
        """ evaluates whether this element exists in the linked list of Tails """
        current = self.children.getHead()
        while current:
            if current.value.getName() == name:
                return True
            current = current.next
        return False
    
    def _get_list_children(self) -> list[Union['File', 'FolderN']]:
        """ list of FolderN and Files """
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
        """ remove item from linked Tail list """
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
        """ return the searched element """
        if self.children.is_empty():
            return
        for child in self._get_list_children():
            if child.getName() == name:
                return child
        print(f"file or folder {name} not found.")
            
    def print_list_chidren(self):
        """ console output of data saved in the linked list of Tails """
        for child in self._get_list_children():
            print(child.getName(),end=' ')

    def print_info_children(self):
        """ console output of the detailed data that is in the linked list of Tails """
        for child in self._get_list_children():
            print(str(child))