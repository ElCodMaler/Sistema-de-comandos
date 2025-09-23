from ..TDA.trees.system import System, TreeN
#Clase ASC
class Command:
    """  """
    def __init__(self, directory: System | TreeN) -> None:
        if not isinstance(self.directory, System) or not isinstance(self.directory, TreeN):
            raise ValueError("Instancio esta clase ASC con valor incorrecto.")
        self.directory = directory
    #
    def instruccion(self):
        if isinstance(self.directory, System):
            self.directory.imprimir_preorden()
        else:
            self.directory.imprimir()