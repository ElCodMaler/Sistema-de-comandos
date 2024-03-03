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
#clase del sistema de Directorios
class FolderSistem:
    #+ raiz: el valor raiz de la serie de folders
    def __init__(self):
        self.raiz = None
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
    def insertar(self, carpeta: Carpeta):
        self.raiz = self.insertar_Carpeta(carpeta, self.raiz)
    #metodo donde se iran conectando los nodos a desde la raiz
    def insertar_Carpeta(self, carpeta: Carpeta, nodo: NodoBi):
        if not nodo:
            return NodoBi(carpeta)
        #ordenando los objetos de izquierda a derecha de acuerdo a su peso
        if carpeta.getPesoTotal() < nodo.carpeta.getPesoTotal():
            nodo.izquierda = self.insertar_Carpeta(carpeta, nodo.izquierda)
        elif carpeta.getPesoTotal() > nodo.carpeta.getPesoTotal():
            nodo.derecha = self.insertar_Carpeta(carpeta, nodo.derecha)
        else:
            return nodo
        #asignando la altura respectiva a cada objeto Carpeta
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),self.obtener_altura(nodo.derecha))
        #usando el metodo para obtener el balance de los nodos en el arbol
        balance = self.obtener_balance(nodo)
        #balanceando el arbol de acuerdo a su peso
        if balance > 1 and carpeta.getPesoTotal() < nodo.izquierda.carpeta.getPesoTotal():
            return self.rotar_derecha(nodo)
        elif balance < -1 and carpeta.getPesoTotal() > nodo.derecha.carpeta.getPesoTotal():
            return self.rotar_izquierda(nodo)
        elif balance > 1 and carpeta.getPesoTotal() > nodo.izquierda.carpeta.getPesoTotal():
            return self.rotar_derecha(nodo)
        elif balance < -1 and carpeta.getPesoTotal() < nodo.derecha.carpeta.getPesoTotal():
            return self.rotar_izquierda(nodo)
        else:
            return nodo
    #metodo que imprime los datos en orden de menor a mayor
    def in_orden(self, nodo: NodoBi):
        if nodo:
            self.in_orden(nodo.izquierda)
            print(nodo.carpeta.getNombre())
            self.in_orden(nodo.derecha)