from .colas import Cola
#clase Nodo
class Nodo:
    """
    + valor: donde se almacenara Un elemento cualquiera De la unidad ya sea Carpeta, Fiachero o Unidad.
    + siguiente: donde se asigna un siguiente objeto de tipo Nodo...
    """
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
#clase Pila
class Pila:
    """
    + tope: es el valor que representa el fin de la lista enlazada.
    """
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo
    
    def vaciar_pila(self):
        while not self.esta_vacia():
            self.eliminar()
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente

            return valor_eliminado
    
    def obtener_objetos(self):
        objetos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            objetos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return objetos
        
    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor
        
    def recorrer(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            print('<Ejecucion Comando Dir>')
            print('{0:2s}  {1:11s} {2:2s} {3:18s}'.format('id:','nombre:','peso:','fecha creada'))
            return self._recorrer_aux(self.tope)

    def _recorrer_aux(self, nodo):
        file = ""
        if nodo is not None:
            carpeta = nodo.valor
            print('{0:2d} | {1:10s} | {2:2d} | {3:18s}'.format(carpeta.getId(),carpeta.getNombre(),carpeta.getPesoTotal(),carpeta.getFechaCreada()))
            self._recorrer_aux(nodo.siguiente)
        return file