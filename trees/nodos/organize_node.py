from trees.nodos.folder_node import FolderNode, File

# binary node
class Node_B:
    """
    + value: current value of the binary node.
    + left: the left pivot where the Node_B will be attached.
    + right: the right pivot where the Node_B will be attached.
    + height: number of connected nodes.
    """
    def __init__(self, value: FolderNode | File):
        self.value = value
        self.left: Node_B | None = None
        self.right: Node_B | None = None
        self.height = 1