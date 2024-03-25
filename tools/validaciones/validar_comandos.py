from components.comandos import Lista_Comandos
class ValidarComando:
    def __init__(self, instrucciones: str):
        self.lista_comandos = {Lista_Comandos().comandos[0].getNombre(): Cd(instrucciones),
                               Lista_Comandos().comandos[1].getNombre(): Dir(instrucciones),
                               Lista_Comandos().comandos[2].getNombre(): Mkdir(instrucciones),
                               Lista_Comandos().comandos[3].getNombre(): Asc(instrucciones),
                               Lista_Comandos().comandos[4].getNombre(): Desc(instrucciones),
                               Lista_Comandos().comandos[5].getNombre(): Type(instrucciones)}
#clase CD
class Cd:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.listaC = Lista_Comandos()
        self.comando = None
    #metodo de validacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 2:
            print('Excede la cantidad de datos')
            return False
        for comando in self.listaC.comandos:
            if comando.getId() == 1:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1]:
                    print(f'los requicitos son({requicitos[0]},{entrada[1]})')
                    comando.setRequicito([requicitos[0],entrada[1]])
                    self.comando = comando
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual: str):
        folder = 'C:'
        carpetas = sistema.getCarpetas()
        #funcion ir al directorio anterior
        if self.comando.getRequicito()[1] == "..":
            ubicacion = ubicacion_actual.split('/')
            for directorio in ubicacion:
                if ubicacion[-1] == directorio:
                    break
                if ubicacion[0] == directorio:
                    continue
                folder = folder +'/'+ directorio
            return folder
        #funcion ir al disco local
        elif self.comando.getRequicito()[1] == "/":
            return folder
        else:
            encontrar = self.buscar(carpetas, self.comando.getRequicito()[1])
            if len(encontrar) > 0:
                return ubicacion_actual +'/'+ encontrar
            else:
                print('no existe ese directorio')
                return ubicacion_actual
    #nueva funcion
    def buscar(self, system, entrada):
        if not system.esta_vacia():
            carpetas = system.obtener_objetos()
            subCarpeta = []
            for c in carpetas:
                if c.getNombre() == entrada:
                    return entrada
                elif type(c.getFicheros()) == list and len(c.getFicheros()) > 0:
                    for fich in c.getFicheros():
                        if fich.getNombre() == entrada:
                            return fich.getNombre() + fich.getExtencion()
            for c1 in carpetas:
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            if len(subCarpeta) > 0:
                return self.buscar(subCarpeta[0], entrada)
            else:
                return ''
        else:
            return ''
#clase Dir
class Dir:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
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
        carpetas = sistema.getCarpetas()
        ubicacion = ubicacion_actual.split('/')
        print('la ubicacion es:',ubicacion[-1])
        if ubicacion[-1] == 'C:':
            carpetas.recorrer()
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
            for c in carpetas:
                if c.getNombre() == entrada:
                    if c.getCarpetas():
                        c.getCarpetas().recorrer()
                        return True
                    elif type(c.getFicheros()) == list and len(c.getFicheros()) > 0:
                        for fich in c.getFicheros():
                            print(fich.getNombre())
                        return True
            for c1 in carpetas:
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            if len(subCarpeta) > 0:
                return self.buscar(subCarpeta[0], entrada)
        else:
            return False    
#clase Mkdir
class Mkdir:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 2:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 3:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1]:
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self, sistema):
        print('ejecucion...')

#clase asc
class Asc:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 1:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 4:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0]:
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self, sistema):
        print('ejecucion...')
#clase Desc
class Desc:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.index = Lista_Comandos().comandos[4].getNombre()
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
    def ejecutar(self, sistema):
        print('ejecucion...')
#clase Type
class Type:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.index = Lista_Comandos().comandos[5].getNombre()
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 3:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 6:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1] and entrada[2]:
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self, sistema):
        print('ejecucion...')