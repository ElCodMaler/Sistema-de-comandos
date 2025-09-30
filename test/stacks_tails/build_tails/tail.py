from typing import Optional
from templates.folder import Folder
from templates.file import File
from templates.nodes.node import Node

class Tail:
    """
    + head: root of the linked list that will have the first Node
    + tail: last node of the linked list
    """
    def __init__(self) -> None:
        self._head: Optional[Node[File | Folder]] = None
        self._tail: Optional[Node[File | Folder]] = None
        self._size: int=0

    def is_empty(self) -> bool:
        return not self._head
    
    def add(self, dato: Folder | File):
        """ Adds an element to the top of the stack """
        new_node = Node(dato)
        if not self._head:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def existing_element(self, name: str):
        if self.is_empty():
            return
        current = self._head
        while current:
            if current.value.getName() == name:
                return True
            current = current.next
        return False

    def get(self, name: str):
        if self.
    
    def remove(self) -> Optional[Node[File | Folder]]:
        if self.is_empty():
            print("La cola ya esta vacia")
            return
        nodo: Node[File | Folder] = self._head
        self._head = self._head.next
        self._size -= 1
        return nodo        

    def getHead(self):
        return self._head.value
    
    def getTail(self):
        return self._tail.value
    
    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Cola vacía"
        
        elements: list[str] = []
        current: Optional[Node[File | Folder]] = self._head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)