from tools.TDA.pilas_colas.colas import Cola
from components.elementos_sistema import Carpeta

cola = Cola()
cola.agregar(Carpeta('doc1',12))
cola.agregar(Carpeta('doc2',11))
cola.agregar(Carpeta('doc3',12))
cola.agregar(Carpeta('doc4',11))
cola.agregar(Carpeta('doc5',12))

cola.eliminar('doc3')

cola.recorrer()
