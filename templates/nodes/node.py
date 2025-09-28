from typing import TypeVar, Generic, Optional

T = TypeVar('T')
# ============= CLASS NODE ==========
class Node(Generic[T]):
    """ Base to Node """
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional['Node[T]'] = None
    def __str__(self) -> str:
        return str(self.value)