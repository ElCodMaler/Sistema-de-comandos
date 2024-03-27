from tools.TDA.pilas_colas.pilas import Pila
from components.elementos_sistema import Carpeta

pila = Pila()
pila.agregar(Carpeta('doc1',12))
pila.agregar(Carpeta('doc2',11))
pila.agregar(Carpeta('doc3',12))
pila.agregar(Carpeta('doc4',11))
pila.agregar(Carpeta('doc5',12))
pila.agregar(Carpeta('doc6',11))

pila.eliminar('doc3')

pila.recorrer()