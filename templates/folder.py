from datetime import datetime
from errors.atributs import ValidacionAtributos

class Folder:
    """
    + name: name that identifies the Folder object.
    + weight: the weight that the contents of the folder represent.
    + date_create: creation date of the current object.
    + date_modify: folder modification date.
    """
    def __init__(self, name: str):
        # validates
        ValidacionAtributos(name)
        # inits
        self._name = name
        self._weight: int = 0
        self._date_create = datetime.now()
        self._date_modify = datetime.now()

    # ========= GETTERS ========

    def getName(self) -> str:
        return self._name
    
    def getWeight(self) -> int:
        return self._weight
    
    def update_modify(self):
        """Actualiza la fecha de modificación"""
        self._date_modify = datetime.now()
    
    def __str__(self) -> str:
        return f"📁 {self._name} ({self._weight} bytes) {self._date_create}"