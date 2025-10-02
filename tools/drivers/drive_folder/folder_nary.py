from typing import Union, Optional
from templates.file import File
from templates.folder import Folder as FolderTemplate

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
        self.children: list[Folder | File] = []

    # ======================= UTILITIES =======================
    
    def addChild(self, son: Union['Folder', File]):
        """ add a FolderN or File to this node's list """
        self.children.append(son)
        self._weight += son.getWeight()

    def deleteChild(self, name: str) -> Optional[Union['Folder', File]]:
        """ remove the File or FolderN from the list of this node """
        if not self.children:
            print(f"the folder {self._name} is empty.")
        for i, child in enumerate(self.children):
            if child.getName() == name:
                return self.children.pop(i)
        print("folder not found.")
    
    def getChild(self, name: str) -> Optional[Union['Folder', File]]:
        """ Get File or Folder from the node list """
        if not self.children:
            print(f"the folder {self._name} is empty..")
        for child in self.children:
            if child.getName() == name:
                return child
        print("folder not found.")
            
    def print_list_chidren(self):
        """ console output of the names of the FolderN and files found on this node """
        for son in self.children:
            print(son.getName(), end=' ')

    def print_info_children(self):
        """ console output of detailed information about the FolderN and Files found on this node """
        for son in self.children:
            print(str(son))

    def get_list_children(self) -> list[Union['File', 'Folder']]:
        """ list of Folder and Files """
        return self.children