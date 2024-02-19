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
#los comandos
def usarComandos(nombreU, ubicacion):
    lista_comandos = []
    requicito1 = ['dir',nombreU,ubicacion,'asc']
    requicito2 = ['dir',nombreU,ubicacion,'desc']
    lista_comandos.append(Comando(1,'asc','Organiza las carpetas y ficheros de menor a mayor cantidad de espacio ocupado',requicito1))
    lista_comandos.append(Comando(2,'desc','Organiza las carpetas y los ficheros de mayor a menor cantidad de espacio ocupado',requicito2))