#clases validacion de Nodos de listas enlazadas y arboles n-arios
class NodoError(Exception):
    pass
class NodoWarningError(Exception):
    pass

class ValidacionNodo:
    def __init__(self, nodo: object):
        if not nodo:
            raise NodoError("El nodo no puede ser None")
        self.nodo = nodo
#fin