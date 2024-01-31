import datetime
#La clase fichero
class Fichero:
    #constructor del fichero
    def __init__(self,id=0 , nombre="", extencion="", peso=0, datos=""):
        self.id = id
        self.nombre = nombre
        self.peso = peso
        self.extencion = extencion
        self.fechaModificada = datetime.datetime.now()
        self.datos = datos
    #metodos get
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getFechaCreada(self):
        return self.fechaCreada
    def getExtencion(self):
        return self.extencion
    def getPeso(self):
        return self.peso
    #metodos set
    def setId(self, id):
        self.id = id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setFechaCreada(self):
        self.fechaCreada = datetime.datetime.now()
    def setExtencion(self, extencion):
        self.extencion = extencion
    def setPeso(self, peso):
        self.peso = peso
#La clase carpeta
class Carpeta:
    #constructor de la carpeta
    def __init__(self,id = 0 , nombre="", listaFicheros = [], listaCarpetas = [], pesoTotal=0):
        self.id = id
        self.nombre = nombre
        self.fechaCreada = datetime
        self.listaFicheros = listaFicheros
        self.listaCarpetas = listaCarpetas
        self.pesoTotal = pesoTotal
    #metodos get
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getFechaCreada(self):
        return self.fechaCreada
    def getListaFicheros(self):
        return self.listaFicheros
    def getListaCarpetas(self):
        return self.listaCarpetas
    def getPesoTotal(self):
        return self.pesoTotal
    #metodos set
    def setId(self, id):
        self.id = id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setFechaCreada(self):
        self.fechaCreada = datetime.datetime.now()    
    def setListaFicheros(self, listaF):
        self.listaFicheros = listaF
    def setListaCarpetas(self, listaC):
        self.listaCarpetas = listaC
    def setPesoTotal(self, peso):
        self.pesoTotal = peso
#clase unidad
class Unidad:
    #constructor de la unidad
    def __init__(self,id=0 , nombre="C:", capacidadTotal = 400, espacioDisponible = 400, listaCarpetas = [], tipo = "HDD"):
        self.id = id
        self.nombre = nombre
        self.fechaCreada = datetime
        self.capacidadTotal = capacidadTotal
        self.espacioDisponible = espacioDisponible
        self.listaCarpetas = listaCarpetas
        self.tipo = tipo
    #metodos get
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getFechaCreada(self):
        return self.fechaCreada
    def getCapacidadTotal(self):
        return self.capacidadTotal
    def getEspacioDisponible(self):
        return self.espacioDisponible
    def getListaCarpetas(self):
        return self.listaCarpetas
    def getTipo(self):
        return self.tipo
    #metodos set
    def setId(self, id):
        self.id = id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setFechaCreada(self):
        self.fechaCreada = datetime.datetime.now()
    def setCapacidadTotal(self, capacidadT):
        self.capacidadTotal = capacidadT
    def setEspacioDisponible(self, espacio):
        self.espacioDisponible = espacio
    def setListaCarpetas(self, listaC):
        self.listaCarpetas = listaC
    def setTipo(self, tipo):
        self.tipo = tipo