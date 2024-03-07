from tools.elementos_terminal import Carpeta
#clase Nodo
class NodoBi:
    """
    + carpeta: el objeto Carpeta se agrega a los nodos
    + izquierda: el pivot izquierda donde se anexaran los nodoBi
    + derecha: el pivot derecha donde se anexaran los nodoBi
    + altura: la cantidad de profundidad que tendra el arbol Binario
    """
    def __init__(self, carpeta: Carpeta):
        self.carpeta = carpeta
        self.izquierda: NodoBi = None
        self.derecha: NodoBi = None
        self.altura = 1
#clase del sistema de Directorios(ARBOL BINARIO)
class FolderSistem:
    """
    + user: el nodo raiz del sistema de directorios
    """
    def __init__(self, userName: str):
        self.user = NodoBi(Carpeta(0,userName,0))
    #metodo que retornara la longitud del arbol
    def obtener_altura(self, nodo: NodoBi):
        if not nodo:
            return 0
        return nodo.altura
    #metodo que va a balancear el arbol
    def obtener_balance(self, nodo: NodoBi):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)
    #buscamos una carpeta recorriendo el arbol(ERROR)-> NO RETORNA EL NODO BUSCADO
    def buscar_carpeta(self, nombre: str, nodo: NodoBi):
        if not nodo:
            return None
        if nodo.carpeta.getNombre() == nombre and self.buscar_carpeta(nombre, nodo.izquierda):
            return nodo
        
        if nodo.carpeta.getNombre() == nombre and self.buscar_carpeta(nombre, nodo.derecha):
            return nodo
    #recorrer la lista enlazada y retornar la ultima ubicacion de carpetas
    def navegar(self, ruta: str):
        if ruta == self.user:
            return self.user
        partes_ruta = ruta.split('/')
        carpeta_actual = self.user
        for parte in partes_ruta:
            if not parte:
                print('falta asignar el directorio al cual quiere accesar...')
            carpeta_actual = self.buscar_carpeta(parte,carpeta_actual)
            if not carpeta_actual:
                return None
        return carpeta_actual
    #metodo que cambiara el orden en que estan asignados los Nodos en el arbol
    def rotar_derecha(self, z: NodoBi):
        y = z.izquierda
        t3 = y.derecha

        y.derecha = z
        z.izquierda = t3

        z.altura = 1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),self.obtener_altura(y.derecha))

        return y
    #metodo que cambiara el orden en que estan asignados los Nodos en el arbol
    def rotar_izquierda(self, z: NodoBi):
        y = z.derecha
        t2 = y.izquierda

        y.izquierda = z
        z.derecha = t2

        z.altura = 1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),self.obtener_altura(y.derecha))

        return y
    #metodo principal donde se van a insertar las carpetas
    def insertar_Carpeta(self, carpeta: Carpeta):
        self.user = self.insertar_nodo(carpeta, self.user)
    #metodo donde se iran conectando los nodos desde la raiz
    def insertar_nodo(self, carpeta: Carpeta, nodo: NodoBi):
        if not nodo:
            return NodoBi(carpeta)
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
    def in_orden(self, nodo: NodoBi):
        if nodo:
            self.in_orden(nodo.izquierda)
            print(nodo.carpeta.getNombre())
            self.in_orden(nodo.derecha)