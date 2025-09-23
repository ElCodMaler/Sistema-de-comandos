from .TDA.trees.nodos.folder_node import FolderNode, File
from .TDA.trees.tree_n_ario import DriveSystem
from .TDA.trees.tree_binario import DriveDirectory
#Clase Comandos
class Command:
    """ 
     + dirver: el DriveSystem general
     + actual: el Directorio o File actual
    """
    def __init__(self, drive: DriveSystem):
        self.driver = drive
        self.actual: FolderNode | File = self.driver.raiz

    # comando ASC (Ascendente)
    def asc(self) -> bool:
        """ Imprecion ascedente del directorio actual (/asc)"""
        if isinstance(self.actual, FolderNode):
            res = DriveDirectory(self.actual)
            res.imprimir_preorden()
            return True
        return False
    # comando CD
    def cd(self, name: str) -> FolderNode | File | None:
        """ Entrada al nuevo directorio desde el directorio actual (/cd NAME_SUBFOLDER) or (/cd NAME_FILE)"""
        return self.driver.get(name)
    # comando DESC
    def desc(self):
        """ Imprecion descendente del directorio actual (/desc)"""
        if isinstance(self.actual, FolderNode):
            res = DriveDirectory(self.actual)
            res.imprimir_postorden()
            return True
        return False
    # comando DIR
    def dir(self):
        """ ver lista de directorios """
        if isinstance(self.actual, FolderNode):
            res = DriveDirectory(self.actual)
            res.imprimir_inorden()
            return True
        return False
    # comando HELP
    def help(self):
        print("+ asc: imprecion ascendente desde el directorio actual.")
        print("+ cd: acceso al subfolder proximo al actual..")
        print("+ desc: impresion en orden descendente desde el directorio actual.")
        print("+ dir: impresion de directorios que se encuentran disponibles.")
        print("+ exit: salida del programa de comandos actual.")
        print("+ help: lista de comandos disponibles.")
        print("+ mkdir: generar nuevo folder en el directorio actual.")
        print("+ rmdir: remover un directorio del directorio actual.")
        print("+ type: reconocer el tipo de archivo.")
    # comando mkdir
    def mkdir(self, new_folder:str) -> bool:
        return self.driver.add(self.actual.getName(),new_folder)
    # comando rmdir
    def rmdir(self, delete_folder: str) -> bool:
        return self.driver.delete(delete_folder)
        