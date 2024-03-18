from components.elementos_sistema import Unidad
from tools.TDA.sistema_Carpetas import FolderSystem
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
        self.folderS: list[FolderSystem] = []
#clase sistema
class System:
    """
    + pc: el nodo raiz del sistema
    """
    def __init__(self):
        self.pc: Nodo = None
    #metodos get
    def getUsuarios(self, unidad: str):
        nodo = self.buscar_unidad(unidad)
        return nodo.folderS
    #se agregaran los nodos
    def agregar_nodo(self, unidad: Unidad, nodo: Nodo):
        if not nodo:
            return Nodo(unidad)
        nodo.connect = self.agregar_nodo(unidad, nodo.connect)
        return nodo
    #metodo que asignara el nodo raiz al atributo PC
    def agregar_unidad(self, unidad: Unidad):
        self.pc = self.agregar_nodo(unidad, self.pc)
    #metodo que asignara la raiz de un arbol
    def asignar_raiz(self, nombre: str, raiz: FolderSystem):
        self.buscar_UR(self.pc, nombre, raiz)
    #metodo que asigna un objeto FolderSistem a la unidad especificada
    def buscar_UR(self, nodo: Nodo, nombre: str, raiz: FolderSystem):
        if nodo:
            if nodo.unidad.getNombre() == nombre:
                nodo.folderS.append(raiz)
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
    def crear_usuario(self, unidad: str, nombre_usuario: str):
        nodo = self.buscar_unidad(unidad)
        if len(nodo.folderS) > 0:
            for user in nodo.folderS:
                if user.user:
                    if user.getUserName() == nombre_usuario:
                        print('ya existe este usuario')
            for fsRaiz in nodo.folderS:
                fsRaiz.setUser(nombre_usuario)
        