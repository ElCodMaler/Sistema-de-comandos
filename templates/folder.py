from datetime import datetime
from errors.atributos import ValidacionAtributos

#class FOLDER
class Folder:
    '''
    + name: nombre que identifique el objeto Folder
    + weightTotal: un numero que represente la cantidad de datos que almacena esta carpeta
    + date: la fecha en que se creo el objeto
    '''
    def __init__(self, name: str):
        # validaciones
        ValidacionAtributos(name) 
        # Inicializacion de atributos
        self._name = name
        self._weight = 0
        self._date = datetime.now()

    #metodos GET
    def getName(self) -> str:
        return self._name
    
    def getDate(self) -> datetime:
        return self._date
    
    def getWeight(self) -> int:
        return self._weight
    
    #metodos SET
    def setName(self, name: str):
        # validaciones
        ValidacionAtributos(name)
        # Asignacion
        self._name = name  

    #Manejo del peso de una carpeta
    def setWeight(self, weight: int):
        self._weight = weight

    def addWeight(self, valor: int):
        self._weight += valor