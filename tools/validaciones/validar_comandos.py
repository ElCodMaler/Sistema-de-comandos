from ..comandos.lista import Lista_Comandos
from ..comandos.dir import Dir
from ..comandos.cd import Cd
from ..comandos.mkdir import Mkdir
from ..comandos.rmdir import Rmdir
from ..comandos.asc import Asc
from ..comandos.desc import Desc
from ..comandos.type import Type

class ValidarComando:
    def __init__(self, instrucciones: str):
        self.lista_comandos = {Lista_Comandos().comandos[0].getNombre(): Cd(instrucciones),
                               Lista_Comandos().comandos[1].getNombre(): Dir(instrucciones),
                               Lista_Comandos().comandos[2].getNombre(): Mkdir(instrucciones),
                               Lista_Comandos().comandos[3].getNombre(): Rmdir(instrucciones),
                               Lista_Comandos().comandos[4].getNombre(): Asc(instrucciones),
                               Lista_Comandos().comandos[5].getNombre(): Desc(instrucciones),
                               Lista_Comandos().comandos[6].getNombre(): Type(instrucciones)}

