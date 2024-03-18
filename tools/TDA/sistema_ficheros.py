from components.elementos_sistema import Fichero
#clase Nodo n-ario
class Nodo_N:
    """
    + archivo: instancia de la clase Fichero
    + pivot: una lista de objetos Nodo_N
    """
    def __init__(self, archivo: Fichero):
        self.archivo = archivo
        self.pivot: list[Nodo_N] = []
    #agregar un nodo_N a la lista enlazada de archivos
    def agregar_ficheros(self, nodo):
        self.pivot.append(nodo)
    #buscar en la lista de nodos hasta encontrar el archivo
    def encontrar_fichero(self, nombre: str):
        for p in self.pivot:
            if p.archivo.getNombre() == nombre:
                return p
            p.encontrar_fichero(nombre)
        return None
    #eliminar un nodo_N de la lista de Nodos_N
    def eliminar_fichero(self, nombre: str):
        for p in self.pivot:
            if p.archivo.getNombre() == nombre:
                self.pivot.remove(p)
                return True
            p.eliminar_fichero(nombre)
        return False
    #impresion de datos en orden ascendente
    def recorrido_preorden(self):
        print(self.archivo.getNombre())
        for p in self.pivot:
            p.recorrido_preorden()
    #impresion de los datos en orden descendente
    def recorrido_inorden(self):
        if len(self.pivot) > 0:
            self.pivot[0].recorrido_inorden()
        print(self.archivo.getNombre())
        for p in self.pivot[1:]:
            p.recorrido_inorden()
    #impresion de los datos en orden aleatorio
    def recorrido_postorden(self):
        for p in self.pivot:
            p.recorrido_postorden()
        print(self.archivo.getNombre())
#clase File System
class FileSystem:
    """
    + raiz: la primera clase Nodo_N
    """
    def __init__(self):
        self.raiz: Nodo_N = None
    #metodo get
    def get_raiz(self):
        return self.raiz
    #crear el archivo
    def crear_archivo(self, archivo: Fichero):
        if not self.raiz:
            self.raiz = Nodo_N(archivo)
        self.agregar_nodo(archivo, self.raiz)
    #buscar en la lista enlazada de nodos hasta asegurarse de que no existe el archivo
    def agregar_nodo(self, archivo: Fichero, nodo: Nodo_N):
        if not nodo.encontrar_fichero(archivo.getNombre()):
            nodo.agregar_ficheros(Nodo_N(archivo))
            