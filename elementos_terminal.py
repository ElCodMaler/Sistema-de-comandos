import datetime
#clase FICHERO
class Fichero:
    '''
    + id: numero unico del objeto creado
    + nombre: nombre que identifique el objeto fichero
    + extencion: tipo de documento, ejemplo(.doc, .exe, .jpg, etc)
    + peso: numero de cantidad de peso que tiene el fichero
    + datos: el contenido del fichero en especifico
    + fechaModificada: la fecha en que se crea el objeto
    '''
    def __init__(self, id: int, nombre: str, extencion: str, peso: int, datos: str):
        self.id = id
        self.nombre = nombre
        self.peso = peso
        self.extencion = extencion
        self.fecha = datetime.datetime.now()
        self.datos = datos
    #metodos get
    def getId(self) -> int:
        return self.id
    def getNombre(self) -> str:
        return self.nombre
    def getFechaCreada(self) -> datetime:
        return self.fecha
    def getExtencion(self) -> int:
        return self.extencion
    def getPeso(self) -> int:
        return self.peso
    def getDatos(self) -> str:
        return self.datos 
    #metodos set
    #la diferencia de este metodo a los demas es que se actualizara la fecha de acuerdo a alguna modificacion que se
    #realice
    def setFechaModificada(self):
        self.fecha = datetime.datetime.now()
    def setNombre(self, nombre: str):
        self.nombre = nombre
        self.setFechaModificada()
    def setExtencion(self, extencion: str):
        self.extencion = extencion
        self.setFechaModificada()
    def setPeso(self, peso: int):
        self.peso = peso
        self.setFechaModificada()
    def setDatos(self, datos: str):
        self.datos = datos
        self.setFechaModificada()
#clase CARPETA
class Carpeta:
    '''
    + id: numero unico del objeto creado
    + nombre: nombre que identifique el objeto Carpeta
    + listaFicheros: una lista de objetos Fichero que se encuentran dentro de esta carpeta
    + listaCarpetas: una lista de objetos Carpeta que se encuentran dentro de esta carpeta
    + pesoTotal: un numero que represente la cantidad de datos que almacena esta carpeta
    + fechaCreada: la fecha en que se creo el objeto, usando la
    '''
    def __init__(self, id: int, nombre: str, ficheros: list[Fichero] | None, listaCarpetas: list | None, pesoTotal: int):
        self.id = id
        self.nombre = nombre
        self.fechaCreada = datetime.datetime.now()
        self.ficheros = ficheros
        self.listaCarpetas = listaCarpetas
        self.pesoTotal = pesoTotal
    #metodos get
    def getId(self) -> int:
        return self.id
    def getNombre(self) -> str:
        return self.nombre
    def getFechaCreada(self) -> datetime:
        return self.fechaCreada
    def getFicheros(self) -> list[Fichero]:
        return self.ficheros
    def getListaCarpetas(self) -> list:
        return self.listaCarpetas
    def getPesoTotal(self) -> int:
        return self.pesoTotal
    #metodos set
    def setNombre(self, nombre: str):
        self.nombre = nombre  
    def setFicheros(self, fiche: list[Fichero] | Fichero):
        if type(fiche) == Fichero:
            self.ficheros.append(fiche)
        else:
            self.ficheros = fiche
    def setListaCarpetas(self, listaC: list | object):
        if type(listaC) == Carpeta:
            self.ficheros.append(listaC)
        else:
            self.ficheros = listaC
    def setPesoTotal(self, peso: int):
        self.pesoTotal = peso
#clase UNIDAD
class Unidad:
    '''
    + id: numero unico del objeto creado
    + nombre: nombre que identifique el objeto Unidad
    + capacidadTotal: es la capacidad de espacio que puede almacenar el disco
    + espacioDisponible: es la capacidad es el espacio que sobra del disco
    + listaCarpetas: una lista de objetos Carpeta que se encuentran dentro de esta Unidad
    + tipo: es la estructura del dico que almacena datos
    '''
    def __init__(self, id = 0, nombre="C:", capacidadTotal = 600, espacioDisponible = 0, carpetas: list[Carpeta] = [], tipo = "HDD"):
        self.id = id
        self.nombre = nombre
        self.fechaCreada = datetime.datetime.now()
        self.capacidadTotal = capacidadTotal
        self.espacioDisponible = espacioDisponible
        self.carpetas = carpetas
        self.tipo = tipo
    #metodos get
    def getId(self) -> int:
        return self.id
    def getNombre(self) -> str:
        return self.nombre
    def getFechaCreada(self) -> datetime:
        return self.fechaCreada
    def getCapacidadTotal(self) -> int:
        return self.capacidadTotal
    def getEspacioDisponible(self) -> int:
        return self.espacioDisponible
    def getCarpetas(self) -> list[Carpeta]:
        return self.carpetas
    def getTipo(self) -> str:
        return self.tipo
    #metodos set
    def setNombre(self, nombre: str):
        self.nombre = nombre
    def setCapacidadTotal(self, capacidadT: int):
        self.capacidadTotal = capacidadT
    def setEspacioDisponible(self, espacio: int):
        self.espacioDisponible = espacio
    def setCarpetas(self, listaC: list[Carpeta]):
        self.carpetas = listaC
    def setTipo(self, tipo: str):
        self.tipo = tipo