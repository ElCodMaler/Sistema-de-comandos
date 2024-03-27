import datetime

#clase FICHERO
class Fichero:
    id = 0
    '''
    + id: numero unico del objeto creado
    + nombre: nombre que identifique el objeto fichero
    + extencion: tipo de documento, ejemplo(.doc, .exe, .jpg, etc)
    + peso: numero de cantidad de peso que tiene el fichero
    + datos: el contenido del fichero en especifico
    + fechaModificada: la fecha en que se crea el objeto
    '''
    def __init__(self, nombre: str, extencion: str, peso: int, datos: str):
        Fichero.id += 1
        self.id = Fichero.id
        self.nombre = nombre
        self.peso = peso
        self.extencion = extencion
        self.fecha = datetime.datetime.now()
        self.datos = datos

    #metodos GET
    def getId(self) -> int:
        return self.id
    
    def getNombre(self) -> str:
        return self.nombre
    
    def getFechaCreada(self) -> datetime.datetime:
        return self.fecha
    
    def getExtencion(self) -> str:
        return self.extencion
    
    def getPeso(self) -> int:
        return self.peso
    
    def getDatos(self) -> str:
        return self.datos 
    #metodos SET
    def setNombre(self, nombre: str):
        self.nombre = nombre
        self.setFechaModificada()
    #la diferencia de este metodo a los demas es que se actualizara la fecha de acuerdo a alguna modificacion que se
    #realice
    def setFechaModificada(self):
        self.fecha = datetime.datetime.now()

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
    id = 0
    '''
    + id: numero unico del objeto creado
    + nombre: nombre que identifique el objeto Carpeta
    + listaFicheros: una lista de objetos Fichero que se encuentran dentro de esta carpeta
    + listaCarpetas: una lista de objetos Carpeta que se encuentran dentro de esta carpeta
    + pesoTotal: un numero que represente la cantidad de datos que almacena esta carpeta
    + fechaCreada: la fecha en que se creo el objeto, usando la
    '''
    def __init__(self, nombre: str, pesoTotal: int):
        Carpeta.id += 1
        self.id = Carpeta.id
        self.nombre = nombre
        self.fechaCreada = datetime.datetime.now()
        self.ficheros = Fichero
        self.carpetas = None
        self.pesoTotal = pesoTotal

    #metodos GET
    def getId(self) -> int:
        return self.id

    def getNombre(self) -> str:
        return self.nombre
    
    def getFechaCreada(self) -> datetime:
        return self.fechaCreada
    
    def getFicheros(self) -> list[Fichero]:
        return self.ficheros
    
    def getCarpetas(self):
        return self.carpetas
    
    def getPesoTotal(self) -> int:
        return self.pesoTotal
    
    #metodos SET
    def setNombre(self, nombre: str):
        self.nombre = nombre  

    def setFichero(self, fiche: list[Fichero] | Fichero):
        if type(fiche) == list:
            for f in fiche:
                self.pesoTotal += f.getPeso()
            self.ficheros = fiche
        else:
            self.ficheros.append(fiche)

    def setCarpetas(self, carp):
        self.carpetas = carp

    def setPesoTotal(self, peso: int):
        self.pesoTotal = peso

    def sumarPesoTotal(self, valor):
        self.pesoTotal += valor
        
#clase UNIDAD
class Unidad:
    id = 0
    '''
    + id: numero unico del objeto creado
    + nombre: nombre que identifique el objeto Unidad
    + capacidadTotal: es la capacidad de espacio que puede almacenar el disco
    + espacioDisponible: es la capacidad es el espacio que sobra del disco
    + listaCarpetas: una lista de objetos Carpeta que se encuentran dentro de esta Unidad
    + tipo: es la estructura del dico que almacena datos
    '''
    def __init__(self, nombre="C:", capacidadTotal = 600, carpetas = None, tipo = "HDD"):
        Unidad.id += 1
        self.id = Unidad.id
        self.nombre = nombre
        self.fechaCreada = datetime.datetime.now()
        self.capacidadTotal = capacidadTotal
        self.pesoTotal = 0
        self.espacioDisponible = self.capacidadTotal - self.pesoTotal
        self.carpetas = carpetas
        self.tipo = tipo

    #metodos GET
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
    
    def getCarpetas(self):
        return self.carpetas
    
    def getTipo(self) -> str:
        return self.tipo
    
    #metodos SET
    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setCarpetas(self, carpetas):
        self.carpetas = carpetas

    def setTipo(self, tipo: str):
        self.tipo = tipo

    def actualizar_espacioDisponible(self, valor):
        self.pesoTotal += valor
        self.espacioDisponible = self.capacidadTotal - self.pesoTotal