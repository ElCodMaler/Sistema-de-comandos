from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class NodeB(Generic[T]):
    """
    + value: current value of the binary node.
    + left: the left pivot where the NodeB will be attached.
    + right: the right pivot where the NodeB will be attached.
    + height: number of connected nodes.
    """
    def __init__(self, value: T):
        self.value = value
        self.left: Optional['NodeB[T]'] = None
        self.right: Optional['NodeB[T]'] = None
    def __str__(self) -> str:
        return str(self.value)