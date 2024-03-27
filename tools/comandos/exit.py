from .lista import Lista_Comandos

#clase Exit
class Exit:
    """
    + instrucciones: donde se almacenara los datos de entrada del usuario.
    + listaC: donde se tendra instanciado la clase Lista_Comandos, que tiene toda la informacion de los comandos.
    """
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.listaC = Lista_Comandos()
    #metodo de validacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 1:
            return False
        for comando in self.listaC.comandos:
            if comando.getId() == 9:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0]:
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual: str):
        exit()