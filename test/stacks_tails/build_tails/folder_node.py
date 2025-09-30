from templates.folder import Folder
from templates.file import File

class FolderN(Folder):
    """
    + name: name that identifies the Folder object.
    + children: lista enlazada de colas
    + date_create: creation date of the current object.
    + date_modify: folder modification date.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children = Tail()