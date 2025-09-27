from ..tails import DriveDirectory

class NodeD: # nodo de Pilas (lista de DriveDirectorys)
    """
    + value: DriveDirectory
    + next: the next value in the linked list
    """
    def __init__(self, name: str):
        self.name = name
        self.content = DriveDirectory()
        self.next: NodeD | None = None