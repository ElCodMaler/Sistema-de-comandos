from .nodos.directory_node import Node_B, FolderNode, File
from typing import Union

# arbol Binario
class DriveDirectory:
    """ + raiz: El primer nodo Binario """
    def __init__(self, directory: FolderNode):
        self.raiz = Node_B(directory)
        self._entry_tree()

    # ==================== UTILIDADES ====================

    def altura(self) -> int:
        """Calcula la altura del árbol"""
        if not self.raiz:
            raise ValueError("El arbol binario esta vacio...")
        return self._calcular_altura(self.raiz)

    def cantidad_nodos(self) -> int:
        """Cuenta la cantidad total de nodos"""
        if not self.raiz:
            raise ValueError("El arbol binario esta vacio...")
        return self._contar_nodos(self.raiz)

    def add(self, value: FolderNode | File):
        """Asignar una File o Folder al Nodo Binario"""
        if not value:
            raise ValueError("Siempre debe haber un valor")
        return self._insertar_por_prioridades(value)
    
    # ===================== FUNCIONES PROTEGIDAS ======================

    def _entry_tree(self):
        childs = self.raiz.directory.childs if isinstance(self.raiz.directory, FolderNode) else None
        if not childs:
            raise ValueError("No puede recorrerse un File.")
        for directory in childs:
            self.add(directory)
    
    def _insertar_por_prioridades(self, value: FolderNode | File) -> bool:
        """Inserta manteniendo el orden de prioridades: peso → longitud → alfabético"""
        if not self.raiz:
            self.raiz = Node_B(value)
            return True
        actual = self.raiz
        nuevo_nodo = Node_B(value)
        while True:
            comparacion = self._comparar_valores(value, actual.directory)
            if comparacion < 0:  # folder tiene mayor prioridad
                if not actual.izquierda:
                    actual.izquierda = nuevo_nodo
                    return True
                actual = actual.izquierda
            else:  # folder tiene menor o igual prioridad
                if not actual.derecha:
                    actual.derecha = nuevo_nodo
                    return True
                actual = actual.derecha
            

    def _comparar_valores(self, item1: FolderNode | File, item2: FolderNode | File) -> int:
        """
        Compara dos folders según el sistema de prioridades:
        1. Peso (mayor primero)
        2. Longitud del nombre (más larga primero)
        3. Orden alfabético/númerico carácter por carácter
        
        Devuelve: -1 (folder1 primero), 0 (iguales), 1 (folder2 primero)
        """
        # Prioridad 1: peso (mayor peso primero)
        if item1.getWeight() != item2.getWeight():
            return -1 if item1.getWeight() > item2.getWeight() else 1
        
        # Prioridad 2: Longitud del nombre (más largo primero)
        if len(item1.getName()) != len(item2.getName()):
            return -1 if len(item1.getName()) > len(item2.getName()) else 1
        
        # Prioridad 3: Orden alfabético/númerico carácter por carácter
        for char1, char2 in zip(item1.getName(), item2.getName()):
            if char1 != char2:
                # Manejar dígitos vs letras
                if char1.isdigit() and char2.isdigit():
                    return -1 if int(char1) > int(char2) else 1
                elif char1.isdigit():
                    return -1  # Dígitos tienen prioridad sobre letras
                elif char2.isdigit():
                    return 1   # Dígitos tienen prioridad sobre letras
                else:
                    return -1 if char1 > char2 else 1
        
        return 0  # Son iguales en todas las prioridades
        
    def _contar_nodos(self, nodo: Node_B | None) -> int:
        if not nodo:
            return 0
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)
    
    def _calcular_altura(self, nodo: Node_B | None) -> int:
        if not nodo:
            return 0
        return 1 + max(self._calcular_altura(nodo.izquierda), 
                      self._calcular_altura(nodo.derecha))
        
    # ==================== RECORRIDOS ====================
    
    def inorden(self):
        """Recorrido inorden: izquierda → raíz → derecha"""
        if not self.raiz:
            raise ValueError("El arbol binario esta vacio...")
        return self._inorden_recursivo(self.raiz)
    
    def _inorden_recursivo(self, nodo: Node_B | None) -> list[Union[FolderNode,File]]:
        if not nodo:
            return []
        return (self._inorden_recursivo(nodo.izquierda) + 
                    [nodo.directory] + 
                    self._inorden_recursivo(nodo.derecha))
    
    def preorden(self):
        """Recorrido preorden: raíz → izquierda → derecha"""
        if not self.raiz:
            raise ValueError("El arbol binario esta vacio...")
        return self._preorden_recursivo(self.raiz)
    
    def _preorden_recursivo(self, nodo: Node_B | None) -> list[Union[FolderNode,File]]:
        if not nodo:
            return []
        return ([nodo.directory] + 
                    self._preorden_recursivo(nodo.izquierda) + 
                    self._preorden_recursivo(nodo.derecha))
    
    def postorden(self) -> list[Union[FolderNode,File]]:
        """Recorrido postorden: izquierda → derecha → raíz"""
        if not self.raiz:
            raise ValueError("El arbol binario esta vacio...")
        return self._postorden_recursivo(self.raiz)
    
    def _postorden_recursivo(self, nodo: Node_B | None) -> list[Union[FolderNode,File]]:
        if not nodo:
            return []
        return (self._postorden_recursivo(nodo.izquierda) + 
                    self._postorden_recursivo(nodo.derecha) + 
                    [nodo.directory])
    
    # ==================== IMPRESIÓN BONITA ====================
    
    def imprimir_inorden(self) -> None:
        """Imprime el recorrido inorden de forma legible"""
        print("🌳 RECORRIDO INORDEN:")
        print("(Izquierdo → Raíz → Derecho)")
        print("=" * 50)
        directorys = self.inorden()
        for directory in directorys:
            directory.info()
    
    def imprimir_preorden(self) -> None:
        """Imprime el recorrido preorden de forma legible"""
        print("🌳 RECORRIDO PREORDEN:")
        print("(Raíz → Izquierdo → Derecho)")
        print("=" * 50)
        directorys = self.preorden()
        for directory in directorys:
            directory.info()
    
    def imprimir_postorden(self) -> None:
        """Imprime el recorrido postorden de forma legible"""
        print("🌳 RECORRIDO POSTORDEN:")
        print("(Izquierdo → Derecho → Raíz)")
        print("=" * 50)
        directorys = self.postorden()
        for directory in directorys:
            directory.info()
    