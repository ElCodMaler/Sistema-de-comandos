from .lista import Lista_Comandos
from components.elementos_sistema import Carpeta

#clase asc
class Desc:
    """
    + instrucciones: donde se almacenara los datos de entrada del usuario.
    + directorio: es la direccion actual.
    """
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.directorio = ''
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 1:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 6:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0]:
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual):
        #asignamos valores
        res = None
        self.directorio = ubicacion_actual
        carpetas = sistema.getCarpetas()
        ubicacion = ubicacion_actual.split('/')
        #encontrar el valor a recorrer
        if ubicacion[-1] == 'C:':
            res = self.organizarDesc(carpetas.obtener_objetos())
            print('  sistema disco local C en Windows')
            print('  su numero de serie es WF15EW-62EE\n')
            print(f'  Directorio actual es ({self.directorio})\n')
            print('            recorrido DESC\n')
            self.showDatos(res)
            return ubicacion_actual
        elif self.buscar(carpetas, ubicacion[-1]):
            return ubicacion_actual
        else:
            print('Esta carpeta esta vacia')
            return ubicacion_actual
    #recorrido de las listas enlazadas
    def buscar(self, system, entrada):
        if not system.esta_vacia():
            carpetas = system.obtener_objetos()
            subCarpeta = []
            res = None
            lista = None
            for c in carpetas:
                if c.getNombre() == entrada:
                    if c.getCarpetas():
                        res = self.organizarDesc(c.getCarpetas().obtener_objetos())
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        print('            recorrido DESC\n')
                        self.showDatos(res)
                        print()
                        return True
                    elif c.getFicheros():
                        res = self.organizarDesc(c.getFicheros().obtener_objetos())
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        print('            recorrido DESC\n')
                        self.showDatos(res)
                        print()
                        return True
                    elif c.getCarpetas() and c.getFicheros:
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        print('            recorrido DESC\n')
                        lista = c.getCarpetas().obtener_objetos()
                        for f in c.getFicheros().obtener_objetos():
                            lista.append(f)
                        res = self.organizarDesc(list)
                        self.showDatos(res)
                        print()
                        return True
                    else:
                        return False
            for c1 in carpetas:
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            if len(subCarpeta) > 0:
                return self.buscar(subCarpeta[0], entrada)
        else:
            return False
    #organizar carpetas
    def organizarDesc(self, files):
        menor = files[0]
        for c in range(len(files)):
            if len(files)-1 == c+1:
                break
            op = files[c].getPesoTotal() - files[c+1].getPesoTotal()
            if op < 0:
                files[c] = files[c+1]
                files[c+1] = menor
                menor = files[c+1]  
            else:
                menor = files[c+1]

        return files
    #mostar resultados
    def showDatos(self, lista):
        print('{0:2s}  {1:12s}  {2:0s}'.format('id:','nombre:','peso:'))
        for obj in lista:
            if type(obj) == Carpeta:
                print('{0:2d} | {1:11s}  {2:5d}'.format(obj.getId(),obj.getNombre(),obj.getPesoTotal()))
            else:
                print('{0:2d} | {1:11s}  {2:5d}'.format(obj.getId(),obj.getNombre(),obj.getPeso()))