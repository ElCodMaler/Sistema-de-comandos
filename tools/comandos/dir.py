from .lista import Lista_Comandos

#clase Dir
class Dir:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.directorio = ''
    #metodo de validacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 1:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 2:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0]:
                    self.comando = comando
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual):
        #asignamos valores
        subCarpeta = []
        self.directorio = ubicacion_actual
        carpetas = sistema.getCarpetas()
        ubicacion = ubicacion_actual.split('/')
        #encontrar el valor a recorrer
        if ubicacion[-1] == 'C:':
            for c1 in carpetas.obtener_objetos():
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            cantidad = len(subCarpeta)
            print('  sistema disco local C en Windows')
            print('  su numero de serie es WF15EW-62EE\n')
            print(f'  Directorio actual es ({self.directorio})\n')
            carpetas.recorrer()
            print(f'       {cantidad} dirs   {sistema.getEspacioDisponible()} bytes libres\n')
            return ubicacion_actual
        elif self.buscar(carpetas, ubicacion[-1]):
            return ubicacion_actual
        else:
            print('Esta carpeta esta vacia')
            return ubicacion_actual
    #nueva funcion
    def buscar(self, system, entrada):
        if not system.esta_vacia():
            carpetas = system.obtener_objetos()
            subCarpeta = []
            subFicheros = 0
            cantidad_carpetas = 0
            for c in carpetas:
                if c.getNombre() == entrada:
                    if c.getCarpetas():
                        for c1 in c.getCarpetas().obtener_objetos():
                            cantidad_carpetas += 1
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        c.getCarpetas().recorrer()
                        print(f'       {subFicheros} archivos')
                        print(f'       {cantidad_carpetas} dirs   {c.getPesoTotal()} bytes ocupados\n')
                        return True
                    elif c.getFicheros():
                        for c1 in c.getFicheros().obtener_objetos():
                            subFicheros += 1
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        self.showFicheros(c.getFicheros().obtener_objetos())
                        print(f'       {subFicheros} archivos')
                        print(f'       {cantidad_carpetas} dirs   {c.getPesoTotal()} bytes ocupados\n')
                        return True
                    elif c.getCarpetas() and c.getFicheros:
                        for c1 in c.getCarpetas().obtener_objetos():
                            cantidad_carpetas += 1
                        for c1 in c.getFicheros().obtener_objetos():
                            subFicheros += 1
                        print('  sistema disco local C en Windows')
                        print('  su numero de serie es WF15EW-62EE\n')
                        print(f'  Directorio actual es ({self.directorio})\n')
                        c.getCarpetas().recorrer()
                        self.showFicheros(c.getFicheros().obtener_objetos())
                        print(f'       {subFicheros} archivos')
                        print(f'       {cantidad_carpetas} dirs   {c.getPesoTotal()} bytes ocupados\n')
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
    def showFicheros(self, ficheros):
        print('{0:2s}  {1:18s} {2:5s} {3:3s}'.format('id:','nombre:','peso:','datos:'))
        for f in ficheros:
            print('{0:2d} | {1:17s} | {2:0d} | {3:18s}'.format(f.getId(),f.getNombre()+f.getExtencion(),f.getPeso(),f.getDatos()))