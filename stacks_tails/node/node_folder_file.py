from templates.file import File
from templates.folder import Folder

class FolderN: # nodo de Colas (lista de Files and Folders)
    """
    + value: Folder or File value
    + next: the next value in the linked list
    """
    def __init__(self, value: Folder | File):
        self.value = value
        self.next: FolderN | None = None