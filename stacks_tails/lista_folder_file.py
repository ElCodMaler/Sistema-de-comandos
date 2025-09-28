from typing import TypeVar, Generic, Optional
from .node.folder import Nodo

T = TypeVar('T')

class Pila(Generic[T]):
    """Implementación de pila usando listas enlazadas"""
    
    def __init__(self) -> None:
        self.cima: Optional[Nodo[T]] = None
        self.tamanio: int = 0
    
    def apilar(self, dato: T) -> None:
        """Agrega un elemento a la cima de la pila"""
        nuevo_nodo: Nodo[T] = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.tamanio += 1
    
    def desapilar(self) -> T:
        """Remueve y retorna el elemento de la cima"""
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        
        dato: T = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        return dato
    
    def ver_cima(self) -> Optional[T]:
        """Retorna el elemento de la cima sin removerlo"""
        if self.esta_vacia():
            return None
        return self.cima.dato
    
    def esta_vacia(self) -> bool:
        """Verifica si la pila está vacía"""
        return self.cima is None
    
    def __len__(self) -> int:
        return self.tamanio
    
    def __str__(self) -> str:
        if self.esta_vacia():
            return "Pila vacía"
        
        elementos: list[str] = []
        actual: Optional[Nodo[T]] = self.cima
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos)