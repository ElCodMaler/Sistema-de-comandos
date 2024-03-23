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
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 2:
            return False
        for comando in self.listaC.comandos:
            if comando.getId() == 1:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1]:
                    comando.setRequicito([requicitos[0],entrada[1]])
                    self.comando = comando
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self, sistema, ubicacion_actual):
        listaC = sistema[0].getCarpetas().obtener_objetos()
        ubicacion = ubicacion_actual.split('/')
        for carpeta in listaC:
            if ubicacion[-1] == sistema[1].getName():
                if self.comando.getRequicito()[1] == carpeta.getNombre():
                    return ubicacion_actual+'/'+carpeta.getNombre()
            elif ubicacion[-1] == carpeta.getNombre():
                listaF = carpeta.getFicheros()
                for fich in listaF:
                    if self.comando.getRequicito()[1] == fich.getNombre():
                        return ubicacion_actual+'/'+fich.getNombre()     
                print('no se encuentra ningun fichero con ese nombre, favor de registrar bien el nombre')
                return None
#clase Dir
class Dir:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 1:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 2:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0]:
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual):
        listaC = sistema[0].getCarpetas().obtener_objetos()
        ubicacion = ubicacion_actual.split('/')
        if ubicacion[-1] == sistema[1].getName():
            sistema[0].getCarpetas().recorrer()
            return ubicacion_actual
        else:
            for c in listaC:
                if ubicacion[-1] == c.getNombre():
                    for fich in c.getFicheros():
                        print(fich.getNombre())
                    return ubicacion_actual
            print('no se encuentra ningun fichero con ese nombre, favor de registrar bien el nombre')
            return None
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