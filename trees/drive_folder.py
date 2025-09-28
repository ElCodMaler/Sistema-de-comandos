from typing import Union
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
    # post init
    def __post_init__(self):
        """ calculate the size when adding a node """
        self._update_weight()
    # protected function
    def _update_weight(self):
        """ update weight recursively """
        self._weight = 0
        for son in self.children:
            self._weight += son.getWeight()

    # ======================= UTILITIES =======================
    
    def addChild(self, son: Union['FolderN', File]):
        """ add a child to node """
        self.children.append(son)
        self._update_weight()
    
    def info(self):
        """ Detailed printout of the current node data """
        print(f"📁 {self.getName()} ({self.getWeight()} bytes)  {self.getDateCreate()}")

    def print_content(self):
        """ Detailed printout of FolderN content """
        for son in self.children:
            print(str(son))