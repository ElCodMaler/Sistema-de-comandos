from tools.elementos_terminal import Carpeta
class NodoBi:
    """
    + carpeta: el objeto Carpeta se agrega a los nodos
    + izquierda: el pivot izquierda donde se anexaran los nodoBi
    + derecha: el pivot derecha donde se anexaran los nodoBi
    + altura: la cantidad de profundidad que tendra el arbol Binario
    """
    def __init__(self, carpeta: Carpeta):
        self.carpeta = carpeta
        self.izquierda = None
        self.derecha = None
        self.altura = 1
#clase Folder sistem
class FolderSistem:
    #+ raiz: el valor raiz de la serie de folders
    def __init__(self):
        self.raiz = None
    #metodo que retornara la longitud del arbol
    def obtener_altura(self, nodo: NodoBi):
        if not nodo:
            return 0
        return nodo.altura
    #
    def rotar_derecha(self, z: NodoBi):
        y = z.izquierda
        t3 = y.derecha

        y.derecha = z
        z.izquierda = t3

        z.altura = 1 + max(self.obtener_altura(z.izquierda),self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda),self.obtener_altura(y.derecha))

        return y
    #
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
        if not self.raiz:
            self.raiz = NodoBi(carpeta)
        else:
            self.insertar_Carpeta(carpeta, self.raiz)

    def insertar_Carpeta(self, carpeta: Carpeta, nodo: NodoBi):
        if carpeta.getPesoTotal() < nodo.izquierda.carpeta.getPesoTotal():
            nodo.izquierda = self.insertar_Carpeta(carpeta, nodo.izquierda)
        elif carpeta.getPesoTotal() > nodo.izquierda.carpeta.getPesoTotal():
            nodo.derecha = self.insertar_Carpeta(carpeta, nodo.derecha)
        else:
            return nodo
        
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),self.obtener_altura(nodo.derecha))

        balance = self.obtener


    def in_orden(self, nodo: NodoBi):
        if nodo:
            self.in_orden(nodo.izquierda)
            print(nodo.archivo)
            self.in_orden(nodo.derecha)

#ejemplo 
