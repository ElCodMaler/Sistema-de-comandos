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
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 2:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 1:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1]:
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self):
        pass
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