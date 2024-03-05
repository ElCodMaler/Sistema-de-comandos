from tools.elementos_terminal import Fichero

class Nodo_N:
    def __init__(self, archivo: Fichero):
        self.archivo = archivo
        self.pivot: list[Nodo_N] = []
    #
    def agregar_ficheros(self, nodo: Nodo_N):
        self.ficheros.append(nodo)
    #
    def encontrar_fichero(self, nombre: str):
        for p in self.pivot:
            if p.archivo.getNombre() == nombre:
                return p
            else:
                return None
    #
    def eliminar_fichero(self, nombre: str):
        for p in self.pivot:
            if p.archivo.getNombre() == nombre:
                self.pivot.remove(p)
                return True
        return False
    #
    def recorrido_preorden(self):
        print(self.archivo.getNombre())
        for p in self.pivot:
            p.recorrido_preorden()
    #
    def recorrido_inorden(self):
        if len(self.pivot) > 0:
            self.pivot[0].recorrido_inorden()
        print(self.archivo.getNombre())
        for p in self.pivot[1:]:
            p.recorrido_inorden()
    #
    def recorrido_postorden(self):
        for p in self.pivot:
            p.recorrido_postorden()
        print(self.archivo.getNombre())
class FileSystem:
    def __init__(self):
        self.raiz = Nodo_N(Fichero(1,'Raiz','txt',20,'ENTRADA DE DATOS'))
        
        