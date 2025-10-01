from typing import TypeVar, Generic

T = TypeVar('T')

class NodeN(Generic[T]):
    """
    + value: current value of the binary node.
    + content: una lista de valores NodeN
    """
    def __init__(self, value: T):
        self.value = value
        self.content: list[NodeN[T]] = []
    def __str__(self) -> str:
        return str(self.value)