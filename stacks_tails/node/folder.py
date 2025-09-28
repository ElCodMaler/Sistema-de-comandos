from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Nodo(Generic[T]):
    """Clase base para nodos de listas enlazadas"""
    
    def __init__(self, dato: T) -> None:
        self.dato: T = dato
        self.siguiente: Optional['Nodo[T]'] = None

    def __str__(self) -> str:
        return str(self.dato)