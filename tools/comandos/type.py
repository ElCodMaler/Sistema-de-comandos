from .lista import Lista_Comandos

#clase Type
class Type:
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.index = Lista_Comandos().comandos[5].getNombre()
    #metodo de calidacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 2:
            return False
        listaC = Lista_Comandos()
        for comando in listaC.comandos:
            if comando.getId() == 7:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1] and entrada[2]:
                    return True
        return False
    #metodo donde se ejecutara el comando(EN PRODUCCION)
    def ejecutar(self, sistema):
        print('ejecucion...')