#clase Nodo
class Nodo:
    """
    + valor: es el valor que se almacenara en el nodo
    + siguiente: va a ser el siguiente nodo
    """
    def __init__(self, valor):
        self.valor = valor
        self.siguiente: Nodo = None
#clase Cola
class Cola:
    """
    + frente: es el primer nodo
    + fin: el nodo que se encuentra al final de la lista
    """
    def __init__(self):
        self.frente = None
        self.fin: Nodo = None
    #condicion del atributo frente
    def esta_vacia(self):
        return self.frente is None
    #agregar un dato a la lista de colas
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo
    #eliminar los primeros datos almacenados
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor.getNombre()
            self.frente = self.frente.siguiente
        if self.frente is None:
            self.fin = None
        return valor_eliminado
    #se retornara una lista de los valores que tiene la lista enlazada
    def obtener_objetos(self):
        objetos = []
        nodo_actual = self.frente
        while nodo_actual is not None:
            objetos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return objetos
    #retornara el valor que se encuentra enfrente de la lista
    def ver_frente(self):
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor.getNombre()
    #recorrera la lista enlazada imprimiendo los datos
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)
    #un auxiliar del metodo recorrer, que es donde se usa un metodo recursivo que recorre toda la lista
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.getNombre())
            self._recorrer_aux(nodo.siguiente)