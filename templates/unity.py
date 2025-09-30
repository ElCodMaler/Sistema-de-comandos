from trees.tree_n_ario import DriveDirectory as drive_tree
from stacks_tails.drivers.drive_directory import DriveDirectory as drive_stack_tail
#clase UNITY
class Unity:
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
        self.drive_folder: drive_tree | drive_stack_tail
        self._weight = 0
        self._gap = self._storage - self._weight
    # post init
    def __post_init__(self):
        """Calcula el tamaño total al crear el nodo"""
        self._weight = self.drive_folder.root.getWeight()
        
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