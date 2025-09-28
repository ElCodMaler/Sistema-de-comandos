from typing import Union, Optional, List
from stacks_tails.stacks import Stack
from templates.file import File
from templates.folder import Folder

class FolderN(Folder):
    """
    + name: name that identifies the Folder object.
    + children: instance of the Stack to Files and Folders
    + date_create: creation date of the current object.
    + date_modify: folder modification date.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: Stack[Union['File', 'FolderN']] = Stack()

    # post init
    def __post_init__(self):
        """ calculate the size when adding a node """
        self._update_weight()

    # --------------- Protected functions ---------------

    def _update_weight(self):
        """ update weight recursively """
        list_content = self._get_list_content()
        self._weight = 0
        for son in list_content:
            self._weight += son.getWeight()

    def _get_list_content(self) -> List[Union['File', 'FolderN']]:
        """ traverse linked list to return a list of Folders and Files """
        # Create a temporary Stack to avoid losing the original order
        Stack_temp: Stack[Union[File, FolderN]] = Stack()
        elements: List[Union[FolderN,File]] = []
        # Transfer items to temporary Stack and collect information
        while not self.children.is_empty():
            element: Union[File, Folder] = self.children.remove()
            Stack_temp.add(element)
            elements.append(element)
        # Restore the original Stack
        while not Stack_temp.is_empty():
            self.children.add(Stack_temp.remove())
        return elements

    # =============== UTILITIES ===============
    
    def addChild(self, element: Union['File', 'FolderN']):
        """ Add a file or folder to this folder """
        self.children.add(element)
        self.update_modify()
    
    def delete_last(self) -> Optional[Union['File', 'FolderN']]:
        """ Removes the last element added (LIFO) """
        if self.children.is_empty():
            return None
        
        element: Union[File, Folder] = self.children.remove()
        self.update_modify()
        return element
    
    def print_content(self):
        """ print detailed list of the contents of this folder """
        if self.children.is_empty():
            print(f"The Folder '{self._name}' is empty.")
            return
        list_content = self._get_list_content()
        # Display items in reverse order (newest to oldest)
        for element in list_content:
            print(f"   {str(element)}")
    
    def search_element(self, name: str) -> Optional[Union['File', 'FolderN']]:
        """ Search for an item by name in the folder """
        list_content = self._get_list_content()
        for element in list_content:
            if element.getName() == name:
                return element
        return None