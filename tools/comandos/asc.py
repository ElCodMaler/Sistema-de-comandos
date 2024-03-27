from .lista import Lista_Comandos

#clase asc
class Asc:
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
            if comando.getId() == 5:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0]:
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self, sistema, ubicacion_actual):
        #asignamos valores
        res = None
        self.directorio = ubicacion_actual
        carpetas = sistema.getCarpetas()
        ubicacion = ubicacion_actual.split('/')
        #encontrar el valor a recorrer
        if ubicacion[-1] == 'C:':
            res = self.organizarAsc(carpetas)
            print('  sistema disco local C en Windows')
            print('  su numero de serie es WF15EW-62EE\n')
            print(f'  Directorio actual es ({self.directorio})\n')
            print('            recorrido ASC\n')
            self.showCarpetas(res)
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
            for c in carpetas:
                if c.getNombre() == entrada:
                    if c.getCarpetas():
                        res = self.organizarAsc(c.getCarpetas())
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        print('            recorrido ASC\n')
                        self.showCarpetas(res)
                        print()
                        return True
                    elif type(c.getFicheros()) == list and len(c.getFicheros()) > 0:
                        self.showFicheros(c.getFicheros())
                        return True
            for c1 in carpetas:
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            if len(subCarpeta) > 0:
                return self.buscar(subCarpeta[0], entrada)
        else:
            return False
    #organizar carpetas
    def organizarAsc(self, carpeta):
        files = carpeta.obtener_objetos()
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
                menor = files[c]

        return files
    #mostar resultados
    def showCarpetas(self, lista):
        print('{0:2s}  {1:9s}   {2:7s}'.format('id:','nombre:','peso:'))
        for carpeta in lista[::-1]:
            print('{0:2d} | {1:10s}   {2:7d}'.format(carpeta.getId(),carpeta.getNombre(),carpeta.getPesoTotal()))