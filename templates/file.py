from datetime import datetime
from errors.atributs import ValidacionAtributos
from errors.file_extention import ValidacionExtencion

#class FILE
class File:
    '''
    + name: name that identifies the File object
    + ext: file extension
    + content: information that the Archive will have
    + weight: the weight number that the file has (8 bytes per character)
    + date_create: the date the object is created
    '''
    def __init__(self, name: str,extension: str, content: str='', weight: int=0):
        # validaciones
        ValidacionAtributos(name)
        ValidacionExtencion(extension)
        # Inicializacion de atributos
        self._name = name
        self._ext = extension
        self._content = content
        self._weight = weight if weight > 0 else len(content) * 8 #peso en bytes
        self._date_create = datetime.now()
        self._date_modify = datetime.now()

    #metodos GET
    def getName(self) -> str:
        return f'{self._name}.{self._ext}'
    
    def getDateCreate(self) -> datetime:
        return self._date_create
    
    def getWeight(self) -> int:
        return self._weight
    
    def getContent(self) -> str:
        return self._content
    
    # function protected
    def _set_date_modify(self):
        self._date = datetime.now()

    def setContent(self, info: str):
        self._content = self._content+' '+info if self._content else info
        new_weight = len(info) * 8
        self._weight = self._weight+new_weight if self._weight > 0 else new_weight#peso en bytes
        self._set_date_modify()

    def __str__(self) -> str:
        return f'📄 {self.getName()} ({self._weight} bytes) {self._date_create}'