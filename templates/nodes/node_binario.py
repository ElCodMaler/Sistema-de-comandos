from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class NodoB(Generic[T]):
    """
    + value: current value of the binary node.
    + left: the left pivot where the Node_B will be attached.
    + right: the right pivot where the Node_B will be attached.
    + height: number of connected nodes.
    """
    def __init__(self, value: T):
        self.value = value
        self.left: Optional['NodoB[T]'] = None
        self.right: Optional['NodoB[T]'] = None
        self.height = 1
    def __str__(self) -> str:
        return str(self.value)