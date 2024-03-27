from .lista import Lista_Comandos
from components.elementos_sistema import Carpeta
from ..TDA.pilas_colas.colas import Cola

#clase Mkdir
class Mkdir:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.listaC = Lista_Comandos()
        self.comando = None
    #metodo de calidacion del comando
    def existe(self):
        res = []
        entrada = self.instrucciones.split(' ')
        if len(entrada) < 2:
            return False
        for comando in self.listaC.comandos:
            if comando.getId() == 3:
                requicitos = comando.getRequicito()
                for agregar in entrada:
                    res.append(agregar)
                if requicitos[0] == entrada[0]:
                    comando.setRequicito(res)
                    self.comando = comando
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual):
        #asignamos valores
        carpetas = sistema.getCarpetas()
        ubicacion = ubicacion_actual.split('/')
        #buscamos la carpeta a la que se le agregara el dato
        if sistema.getNombre() == ubicacion[-1]:
            for dato in self.comando.getRequicito():
                if self.comando.getRequicito()[0] == dato:
                    continue
                sistema.getCarpetas().agregar(Carpeta(dato,0))
            return ubicacion_actual
        elif self.buscar(carpetas, ubicacion[-1]):
            return ubicacion_actual
        else:
            print('No se encontro el valor buscado')
            return ubicacion_actual
    #nueva funcion
    def buscar(self, system, entrada):
        if not system.esta_vacia():
            carpetas = system.obtener_objetos()
            subCarpeta = []
            for c in carpetas:
                if c.getNombre() == entrada:
                    if c.getCarpetas():
                        for dato in self.comando.getRequicito():
                            if self.comando.getRequicito()[0] == dato:
                                continue
                            c.getCarpetas().agregar(Carpeta(dato,0))
                        return True
                    elif type(c.getFicheros()) == list and len(c.getFicheros()) > 0:
                        return False
                    else:
                        c.setCarpetas(Cola())
                        for dato in self.comando.getRequicito():
                            if self.comando.getRequicito()[0] == dato:
                                continue
                            c.getCarpetas().agregar(Carpeta(dato,0))
                        return True
            for c1 in carpetas:
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            if len(subCarpeta) > 0:
                return self.buscar(subCarpeta[0], entrada)
        else:
            return False