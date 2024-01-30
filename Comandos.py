#Clase Comnado
class Comando:
    def __init__(self,id = 0, nombre="", descripcion="", requisito=""):
        if(self.id == None):
            self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.requicito = requisito