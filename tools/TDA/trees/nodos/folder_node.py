from typing import Union
from templates.file import File
from datetime import datetime

# n-ary node
class FolderNode:
    """ 
    + children: list of children (FolderNode and File)
    """
    def __init__(self, name: str) -> None:
        self._name = name
        self.children: list[Union['FolderNode', File]] = []
        self._date: datetime = datetime.now()
        self._weight: int = 0
    # post init
    def __post_init__(self):
        """ calculate the size when adding a node """
        self._update_weight()
    # protected function
    def _update_weight(self):
        """ update weight recursively """
        self._weight = 0
        for son in self.children:
            if isinstance(son,File):
                self._weight += son.getWeight()
            else:
                self._weight += son._weight
    # ======================= UTILITIES =======================
    def addChild(self, son: Union['FolderNode', File]):
        """ add a child to node """
        self.children.append(son)
        self._update_weight()
    
    def info(self):
        """ Detailed printout of the current node data """
        print(f"📁 {self.getName()} ({self.getWeight()} bytes)  {self.getCreateDate()}")

    def print_content(self):
        """ Detailed printout of FolderNode content """
        for son in self.children:
            if isinstance(son,File):
                print(f"📄 {son.getName()} ({son.getWeight()} bytes)  {son.getCreateDate()}")
            else:
                print(f"📁 {son.getName()} ({son.getWeight()} bytes)  {son.getCreateDate()}")

    # -------- Getters ----------
    def getWeight(self) -> int:
        return self._weight
    
    def getName(self) -> str:
        return self._name
    
    def getCreateDate(self) -> datetime:
        return self._date