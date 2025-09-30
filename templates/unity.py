from typing import TypeVar, Generic

T = TypeVar('T')

#clase UNITY
class Unity(Generic[T]):
    '''
    + name: nombre que identifique el objeto Unidad
    + storage: es la capacidad de espacio que puede almacenar el disco.
    + drive_folder: instancia del manejador de Carpetas.
    + gap: el espacio que sobra del disco.
    + weight: el peso acumulado en la unidad.
    '''
    def __init__(self, name:str="C:", storage:int= 600):
        self._name = name
        self._storage = storage
        self.drive_folder: T
        self._weight = 0
        self._gap = self._storage - self._weight
        
    #metodos GET
    def getName(self) -> str:
        return self._name
    
    def getStorage(self) -> int:
        return self._storage
    
    def getGap(self) -> int:
        return self._gap
    
    def getWeight(self) -> int:
        return self._weight
    
    #metodos SET
    def setName(self, name: str):
        self._name = name

    def setWeight(self, value: int):
        self._weight += value
        self._gap = self._storage - self._weight

    def setDriverSystem(self, value: T):
        self.drive_folder = value