from datetime import datetime
from errors.atributos import ValidacionAtributos
from errors.file_extention import ValidacionExtencion

#class FILE
class File:
    '''
    + name: nombre que identifique el objeto fichero (name.exencion_fichero)
    + weight: el numero de peso que tiene el fichero(2 bytes por caracter)
    + content: el contenido del fichero en especifico
    + date: la fecha en que se crea el objeto
    '''
    def __init__(self, name: str, content: str):
        # validaciones
        ValidacionAtributos(name)
        ValidacionExtencion(name)
        # Inicializacion de atributos
        self._name: str = name
        self._weight: int = 0
        self._date: datetime = datetime.now()
        self._content: str=''
        self.setContent(content)

    def info(self):
        """Imprecion de la informacion de este nodo"""
        print(f"📄 {self._name} ({self._weight} bytes) {self._date}")

    #metodos GET
    def getName(self) -> str:
        return self._name
    
    def getCreateDate(self) -> datetime:
        return self._date
    
    def getWeight(self) -> int:
        return self._weight
    
    def getContent(self) -> str:
        return self._content
    #metodos SET
    def setName(self, name: str):
        # validaciones
        ValidacionAtributos(name)  # Reutilizando la clase de validaciones
        ValidacionExtencion(name)
        # Asignacion
        self._name = name
        self._setDate()
    #la diferencia de este metodo a los demas es que se actualizara la fecha de acuerdo a alguna modificacion que se
    #realice
    def _setDate(self):
        self._date = datetime.now()

    def setContent(self, content: str):
        self._content = content
        self._weight = len(content) * 2
        self._setDate()