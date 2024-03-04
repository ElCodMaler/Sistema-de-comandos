from tools.elementos_terminal import Fichero

class Nodo_N:
    def __init__(self, archivo: Fichero):
        self.archivo = archivo
        self.ficheros = []
    #
    def agregar_ficheros(self, archivo: Fichero):
        self.ficheros.append(archivo)
    #
    def encontrar_fichero(self, archivo: Fichero):
        for fichero in self.ficheros:
            if 