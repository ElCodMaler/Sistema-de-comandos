from typing import TypeVar, Generic, Optional
from templates.nodes.node import Node

T = TypeVar('T')

# =========== CLASS STACK ============
class Tail(Generic[T]):
    """
    + head: root of the linked list that will have the first Node
    + tail: last node of the linked list
    """
    def __init__(self) -> None:
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size: int=0

    def is_empty(self) -> bool:
        return not self._head
    
    def add(self, dato: T) -> None:
        """ Adds an element to the top of the stack """
        new_node: Node[T] = Node(dato)
        if not self._head:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1
    
    def remove(self) -> T:
        if self.is_empty():
            print("The Tail is already empty.")
        nodo: T = self._head.value
        self._head = self._head.next
        self._size -= 1
        return nodo        

    def getHead(self):
        return self._head
    
    def getTail(self):
        return self._tail
    
    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Empty tail."
        
        elements: list[str] = []
        current: Optional[Node[T]] = self._head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)