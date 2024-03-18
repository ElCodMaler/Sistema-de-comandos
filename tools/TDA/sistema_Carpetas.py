from components.elementos_sistema import Carpeta
from tools.TDA.sistema_ficheros import FileSystem
#clase nodo Binario
class Directorio:
    """
    + carpeta: el objeto Carpeta se agrega a los nodos
    + izquierda: el pivot izquierda donde se anexaran los nodoBi
    + derecha: el pivot derecha donde se anexaran los nodoBi
    + altura: la cantidad de profundidad que tendra el arbol Binario
    """
    def __init__(self, carpeta: Carpeta):
        self.carpeta = carpeta
        self.fileS: FileSystem = None
        self.izquierda: Directorio = None
        self.derecha: Directorio = None
        self.altura = 1
#clase usuarios
class User:
    """
    + name: el nombre de usuario
    + raiz: la coneccion directa con la raiz NodoBi
    """
    def __init__(self, name: str):
        self.name = name
        self.raiz: Directorio = None
#clase del sistema de Directorios(ARBOL BINARIO)
class FolderSystem:
    """
    + raiz: el nodo raiz del sistema de directorios
    + user: el nodo usuario del Folder System
    """
    def __init__(self):
        self.raiz: Directorio = None
        self.user: User = None
    #metodos set
    def setUser(self, nombre_usuario: str):
        self.user = User(nombre_usuario)
        self.user.raiz = self.raiz
    
    def asignarFileSystem(self, carpeta: str, sistemaF: FileSystem):
        carpeta_buscada = self.buscar_carpeta(carpeta, self.raiz)
        if carpeta_buscada:
            carpeta_buscada.fileS = sistemaF
            return True
        return False
    #metodos get
    def getFileSystem(self, nombre_carpeta: str):
        nodo = self.buscar_carpeta(nombre_carpeta, self.raiz)
        if nodo.fileS:
            return nodo.fileS.get_raiz()
    
    def getUser(self):
        return self.user.raiz
    
    def getUserName(self):
        return self.user.name
    #metodo que retornara la longitud del arbol
    def obtener_altura(self, nodo: Directorio):
        if not nodo:
            return 0
        return nodo.altura
    #metodo que va a balancear el arbol
    def obtener_balance(self, nodo: Directorio):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)
    #buscamos una carpeta recorriendo el arbol
    def buscar_carpeta(self, nombre: str, nodo: Directorio):
        if nodo:
            if nodo.carpeta.getNombre() == nombre:
                return nodo
            res = self.buscar_carpeta(nombre, nodo.izquierda)
            if res:
                return res
            res = self.buscar_carpeta(nombre, nodo.derecha)
            if res:
                return res
    #metodo que mostrara las opciones disponibles
    def opciones_nav(self, carp: Directorio):
        res = self.buscar_carpeta(carp.carpeta.getNombre(), self.raiz)
        return res.izquierda, res.derecha
    #recorrer la lista enlazada y retornar el nodo con la ubicacion especificada
    def navegar(self, ruta: str):
        buscar = None
        partes_ruta = ruta.split('/')
        carpeta_actual = self.raiz
        for i in range(len(partes_ruta)):
            carpeta_actual = self.buscar_carpeta(partes_ruta[i], carpeta_actual)
            if self.raiz.carpeta.getNombre() == partes_ruta[0] and not(buscar):
                buscar = carpeta_actual.carpeta.getNombre()
            if not(carpeta_actual.izquierda) and not(carpeta_actual.derecha):
                print('no hay datos ni a la izquierda ni a la derecha del nodo',carpeta_actual.carpeta.getNombre())
                return None
            if len(partes_ruta) > i and len(partes_ruta) != i+1:
                if carpeta_actual.izquierda.carpeta.getNombre() == partes_ruta[i+1]:
                    buscar = buscar +'/'+ partes_ruta[i+1]
                elif carpeta_actual.derecha.carpeta.getNombre() == partes_ruta[i+1]:
                    buscar = buscar +'/'+ partes_ruta[i+1]
                else:
                    print('no se encuentra la carpeta en la ubicacion', carpeta_actual.carpeta.getNombre())    
        if buscar == ruta:
            return carpeta_actual
    #metodo que cambiara el orden en que estan asignados los Nodos en el arbol
    def rotar_derecha(self, z: Directorio):
        y = z.izquierda
        t3 = y.derecha

        y.derecha = z
        z.izquierda = t3

        z.altura = 1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),self.obtener_altura(y.derecha))

        return y
    #metodo que cambiara el orden en que estan asignados los Nodos en el arbol
    def rotar_izquierda(self, z: Directorio):
        y = z.derecha
        t2 = y.izquierda

        y.izquierda = z
        z.derecha = t2

        z.altura = 1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),self.obtener_altura(y.derecha))

        return y
    #metodo principal donde se van a insertar las carpetas
    def insertar_Carpeta(self, carpeta: Carpeta):
        self.raiz = self.insertar_nodo(carpeta, self.raiz)
    #metodo donde se iran conectando los nodos desde la raiz
    def insertar_nodo(self, carpeta: Carpeta, nodo: Directorio):
        if not nodo:
            return Directorio(carpeta)
        #ordenando los objetos de izquierda a derecha de acuerdo a su peso
        if carpeta.getPesoTotal() < nodo.carpeta.getPesoTotal():
            nodo.izquierda = self.insertar_nodo(carpeta, nodo.izquierda)
        elif carpeta.getPesoTotal() > nodo.carpeta.getPesoTotal():
            nodo.derecha = self.insertar_nodo(carpeta, nodo.derecha)
        else:
            return nodo
        #asignando la altura respectiva a cada objeto Carpeta
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),self.obtener_altura(nodo.derecha))
        #usando el metodo para obtener el balance de los nodos en el arbol
        balance = self.obtener_balance(nodo)
        #balanceando el arbol de acuerdo a su peso
        if balance > 1 and carpeta.getPesoTotal() < nodo.izquierda.carpeta.getPesoTotal():
            return self.rotar_derecha(nodo)
        if balance < -1 and carpeta.getPesoTotal() > nodo.derecha.carpeta.getPesoTotal():
            return self.rotar_izquierda(nodo)
        if balance > 1 and carpeta.getPesoTotal() > nodo.izquierda.carpeta.getPesoTotal():
            return self.rotar_derecha(nodo)
        if balance < -1 and carpeta.getPesoTotal() < nodo.derecha.carpeta.getPesoTotal():
            return self.rotar_izquierda(nodo)
        return nodo
    #metodo que imprime los datos en orden de menor a mayor peso
    def in_orden(self, nodo: Directorio):
        if nodo:
            self.in_orden(nodo.izquierda)
            print(nodo.carpeta.getNombre())
            self.in_orden(nodo.derecha)