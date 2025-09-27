from datetime import datetime

class Folder:
    '''
    + name: nombre que identifique el objeto fichero (name.exencion_fichero)
    + weight: el numero de peso que tiene el fichero(2 bytes por caracter)
    + content: el contenido del fichero en especifico
    + date: la fecha en que se crea el objeto
    '''
    def __init__(self, name: str):
        self._name: str = name
        self._weight: int = 0
        self._date: datetime = datetime.now()

    def info(self):
        """Imprecion de la informacion de este nodo"""
        print(f"📁 {self._name} ({self._weight} bytes) {self._date}")

    # --------------------- Getters --------------------
    def getName(self) -> str:
        return self._name
    
    def getDate(self) -> datetime:
        return self._date
    
    def getWeight(self) -> int:
        return self._weight