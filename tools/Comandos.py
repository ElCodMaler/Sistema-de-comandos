#Clase Comando
class Comando:
    #constructor
    def __init__(self,id = 0, nombre="", descripcion="", requisito=[]):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.requicito = requisito
    #metodos get
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getDescripcion(self):
        return self.descripcion
    def getRequicito(self):
        return self.requicito
    #metodos set
    def setId(self, id):
        self.id = id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setDescripcion(self, descrip):
        self.descripcion = descrip
    def setRequicito(self, requicito):
        self.requicito = requicito
#clase lista de comandos
class Lista_Comandos:
    def __init__(self) -> None:
        pass
    #la lista de los comandos
    