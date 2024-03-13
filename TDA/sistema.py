from tools.elementos_terminal import Unidad
from TDA.sistema_Carpetas import FolderSistem
#clase nodo
class Nodo:
    """
    + unidad: donde se asignaran los objetos Unidad
    + connect: donde se va a enlazar un nodo con el siguiente nodo
    + folderS: donde se le asignara la raiz de un objeto FolderSisteme
    """
    def __init__(self, unidad: Unidad):
        self.unidad = unidad
        self.connect: Nodo = None
        self.folderS: FolderSistem = None
#clase sistema
class Sistema:
    """
    + pc: el nodo raiz del sistema
    """
    def __init__(self):
        self.pc: Nodo = None
    #se agregaran los nodos
    def agregar(self, unidad: Unidad, nodo: Nodo):
        if not nodo:
            return Nodo(unidad)
        nodo.connect = self.agregar(unidad, nodo.connect)
        return nodo
    #metodo que asignara el nodo raiz al atributo PC
    def agregar_unidad(self, unidad: Unidad):
        self.pc = self.agregar(unidad, self.pc)
    #metodo que asignara la raiz de un arbol
    def asignar_raiz(self, nombre: str, raiz: FolderSistem):
        self.buscar_UR(self.pc, nombre, raiz)
    #metodo que asigna un objeto FolderSistem a la unidad especificada
    def buscar_UR(self, nodo: Nodo, nombre: str, raiz: FolderSistem):
        if nodo:
            if nodo.unidad.getNombre() == nombre and not nodo.folderS:
                nodo.folderS = raiz
            elif nodo.unidad.getNombre() == nombre and nodo.folderS:
                print('error... ya se le asigno un folder sismte a la unidad', nodo.unidad.getNombre())
            self.buscar_UR(nodo.connect, nombre, raiz)
    #metodo que buscara la unidad
    def buscar_unidad(self, nombre: str):
        return self.encontrar_unidad(self.pc, nombre)
    #metodo que retonara el nodo deseado
    def encontrar_unidad(self, nodo: Nodo, nombre: str):
        if not nodo:
            return None
        if nodo.unidad.getNombre() == nombre:
            return nodo
        if self.encontrar_unidad(nodo.connect):
            return self.encontrar_unidad(nodo.connect)
    #mostar
    def mostrar(self, nodo: Nodo):
        if nodo:
            print(nodo.unidad.getNombre())
            self.mostrar(nodo.connect)
    #crear usuario
    def crear_ususario(self, unidad: str, nombre_usuario: str):
        nodo = self.buscar_unidad(unidad)
        nodo.folderS.setUser(nombre_usuario)
