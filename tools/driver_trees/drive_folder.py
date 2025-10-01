from typing import Union, Optional
from templates.file import File
from templates.folder import Folder

# n-ary node
class FolderN(Folder):
    """ 
    + children: list of children (FolderN and File)
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[Union['FolderN', File]] = []

    # ======================= UTILITIES =======================
    
    def addChild(self, son: Union['FolderN', File]):
        """ add a child to node """
        self.children.append(son)
        self._weight += son.getWeight()

    def deleteChild(self, name: str) -> Optional[Union['FolderN', File]]:
        """ Removes the last element added (LIFO) """
        if not self.children:
            print(f"the folder {self._name} is empty..")
        for i, child in enumerate(self.children):
            if child.getName() == name:
                return self.children.pop(i)
        print("folder not found.")
    
    def getChild(self, name: str) -> Optional[Union['FolderN', File]]:
        """ Search for an item by name in the folder """
        if not self.children:
            print(f"the folder {self._name} is empty..")
        for child in self.children:
            if child.getName() == name:
                return child
        print("folder not found.")
            
    def print_list_chidren(self):
        for son in self.children:
            print(son.getName())

    def print_info_children(self):
        """ Detailed printout of FolderN content """
        for son in self.children:
            print(str(son))