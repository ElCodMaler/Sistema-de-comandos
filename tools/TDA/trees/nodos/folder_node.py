from typing import Union
from templates.file import File
from datetime import datetime

# nodo n-ario
class FolderNode:
    """Nodo para carpetas (puede tener hijos)"""
    def __init__(self, name: str) -> None:
        self._name = name
        self.childs: list[Union['FolderNode', File]] = []
        self._date: datetime = datetime.now()
        self._weight: int = 0
    # post init
    def __post_init__(self):
        """Calcula el tamaño total al crear el nodo"""
        self._update_weight()
    # funcion protegida de la clase
    def _update_weight(self):
        """Calcula el tamaño total recursivamente"""
        self._weight = 0
        for hijo in self.childs:
            if isinstance(hijo,File):
                self._weight += hijo.getWeight()
            else:
                self._weight += hijo._weight
    # ---------------- Functions -----------------
    def addChild(self, hijo: Union['FolderNode', File]):
        """Agrega un hijo y actualiza el tamaño"""
        self.childs.append(hijo)
        self._update_weight()
    
    def info(self):
        """Imprecion de la informacion de este nodo"""
        print(f"📁 {self._name} ({len(self.childs)} hijos, {self._weight} bytes)")

    def print_content(self):
        for child in self.childs:
            if isinstance(child,File):
                print(f"📄 {child.getName()} ({child.getWeight()} bytes)  {child.getCreateDate()}")
            else:
                print(f"📁 {child.getName()} ({child.getWeight()} bytes)  {child.getCreateDate()}")

    # -------- Getters ----------
    def getWeight(self) -> int:
        return self._weight
    
    def getName(self) -> str:
        return self._name
    
    def getCreateDate(self) -> datetime:
        return self._date