from components.comandos import Comando

#clase lista de comandos
class Lista_Comandos:
    def __init__(self):
        self.comandos = [Comando(1,'cd','Acceso al directorio.',['cd',None]),
                         Comando(2,'dir','Mostrar el contenido del directorio actual.',['dir']),
                         Comando(3,'mkdir','Crear Carpetas o ficheros en el directorio actual.',['mkdir']),
                         Comando(4,'rmdir','Eliminar carpetas vacias',['rmdir']),
                         Comando(5,'asc','Mostrar el contenido del directorio en orden ascendente por pesos.',['asc']),
                         Comando(6,'desc','Mostrar el contenido del directorio en orden descendente por pesos.',['desc']),
                         Comando(7,'type','Mostrar el contenido del archivo con su ubicacion.',['type',None]),
                         Comando(8,'help','Mostrar los comandos disponibles.',['help']),
                         Comando(9,'exit','Cerrar terminal',['exit'])]