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
    def __init__(self):
        self.comandos = [Comando(1,'cd','Acceder al directorio',['cd',None]),
                         Comando(2,'dir','mostrara todos los directorios a los que se pueden acceder',['dir']),
                         Comando(3,'mkdir','agregar carpeta o subcarpetas desde su ubicacion',[['mkdir',None],['mkdir',None,'\\']]),
                         Comando(4,'asc','mostrar los datos en orden ascendente',['asc']),
                         Comando(5,'desc','mostrar los datos en orden descendete',['desc']),
                         Comando(6,'type','se creara un archivo en el directorio en el que se encuentra y adicional se agregaran el contenido',['type',None,None])]
    #la lista de los comandos
    def cd(self, entrada):
        res = entrada.split(' ')
        
