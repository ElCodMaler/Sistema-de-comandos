from .folder_node import FolderNode, File

#clase nodo Binario
class Node_B:
    """
    + directory: lista enlazada de n cantidad de objetos Unity.
    + izquierda: el pivot izquierdo donde se anexaran los Node_B.
    + derecha: el pivot derecho donde se anexaran los Node_B.
    + altura: la cantidad de profundidad que tendra el arbol Binario.
    """
    def __init__(self, directory: FolderNode | File):
        self.directory = directory
        self.izquierda: Node_B | None = None
        self.derecha: Node_B | None = None
        self.altura = 1