from typing import TypeVar, Generic, Optional
from templates.nodes.node import Node

T = TypeVar('T')

# =========== CLASS STACK ============
class Stack(Generic[T]):
    """
    + top: Value firts Node[T]
    + size: number of Nodes
    """
    def __init__(self) -> None:
        self._top: Optional[Node[T]] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return not self._top
    
    def add(self, dato: T) -> None:
        """ Adds an element to the top of the stack """
        new_node: Node[T] = Node(dato)
        new_node.next = self._top
        self._top = new_node
        self.size += 1
    
    def remove(self) -> T:
        """ Remove and return the top element """
        if self.is_empty():
            raise Exception("the stack is void")
        dato: T = self._top.value
        self._top = self._top.next
        self.size -= 1
        return dato
    
    def getTop(self) -> Optional[Node[T]]:
        """Retorna el elemento de la cima sin removerlo"""
        if self.is_empty():
            return None
        return self._top
    
    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        if not self._top:
            return "Pila vacía"
        
        elements: list[str] = []
        current: Optional[Node[T]] = self._top
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)