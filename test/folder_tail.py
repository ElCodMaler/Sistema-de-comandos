from typing import Union, Optional
from templates.linked_lists.tails import Tail
from templates.file import File
from .template_folder import FolderTemplate

class Folder(FolderTemplate):
    """
    + name: name that identifies the Folder object.
    + children: linked list of Tails that stores Folders and Files.
    + weight: the weight that the contents of the folder represent.
    + date_create: creation date of the current object.
    + date_modify: folder modification date.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: Tail[Folder | File] = Tail()

    # ======================= UTILITIES =======================
    
    def addChild(self, son: Union['Folder', File]):
        """ add a FolderN or File to this node's list """
        self.children.add(son)
        self._weight += son.getWeight()

    def deleteChild(self, name: str) -> Optional[Union['Folder', File]]:
        """ remove item from linked Tail list """
        if self.children.is_empty():
            return
        # inicializar variables
        tail_temp: Tail[Union[File, Folder]] = Tail()
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
    
    def getChild(self, name: str) -> Optional[Union['Folder', File]]:
        """ Get File or Folder from the node list """
        if self.children.is_empty():
            return
        for child in self._get_list_children():
            if child.getName() == name:
                return child
        print(f"file or folder {name} not found.")
            
    def print_list_chidren(self):
        """ console output of the names of the FolderN and files found on this node """
        for child in self._get_list_children():
            print(child.getName(),end=' ')

    def print_info_children(self):
        """ console output of detailed information about the FolderN and Files found on this node """
        for child in self._get_list_children():
            print(str(child))

    # =========== PROTECTED FUNCTIONS ==========
    def _get_list_children(self) -> list[Union['File', 'Folder']]:
        """ list of FolderN and Files """
        # inicializar variables
        tail_temp: Tail[Union[File, Folder]] = Tail()
        children_ls: list[Union['File', 'Folder']] = []
        # recorrer lista
        while not self.children.is_empty():
            value = self.children.remove()
            tail_temp.add(value)
            children_ls.append(value)
        # Restore the original Stack
        while not tail_temp.is_empty():
            self.children.add(tail_temp.remove())
        return children_ls
    
    def _existing_element(self, name: str) -> bool:
        """ evaluates whether this element exists in the linked list of Tails """
        current = self.children.getHead()
        while current:
            if current.value.getName() == name:
                return True
            current = current.next
        return False