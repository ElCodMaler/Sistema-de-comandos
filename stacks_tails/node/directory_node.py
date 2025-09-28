from .folder import FolderN
from templates.file import File

class NodeSF: # nodo de Pilas (lista de subfolders)
    """
    + value: FolderN or File
    + next: the next value in the linked list
    """
    def __init__(self, value: FolderN | File):
        self.value = value
        self.next: NodeSF | None = None