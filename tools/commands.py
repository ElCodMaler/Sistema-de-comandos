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
        self._driver = drive
        self.actual: FolderNode | File = self._driver.raiz
        self.browse: str = self.actual.getName()+'/'

    def validate(self, command: str):
        cm = command.split(' ')

        if len(cm) == 1:
            if 'asc' == cm[0]:
                return self._asc()
            elif 'desc' == cm[0]:
                return self._desc()
            elif 'dir' == cm[0]:
                return self._dir()
            elif 'exit' == cm[0]:
                return exit()
            elif 'help' == cm[0]:
                return self._help()
        elif len(cm) == 2:
            if 'mkdir' == cm[0]:
                return self._mkdir(cm[1])
            elif 'rmdir' == cm[0]:
                return self._rmdir(cm[1])
            elif 'cd' == cm[0]:
                return self._cd(cm[1])
        return None

    # ====================== FUNCIONES PROTEGIDAS ======================

    # comando ASC (Ascendente)
    def _asc(self) -> bool:
        """ Imprecion ascedente del directorio actual (/asc)"""
        if isinstance(self.actual, FolderNode):
            res = DriveDirectory(self.actual)
            res.imprimir_preorden()
            return True
        return False
    # comando CD
    def _cd(self, name: str) -> bool:
        """ Importante, base de la navegacion entre directorios """
        directory_ls: list[str] = []
        ls = name.split('/')
        if len(ls) > 1:
            print(ls)
            res = self._eval_grado(self.actual ,ls)
            if res:
                self.actual = res
                return True
            return False
        elif name == '..':
            res = self._buscar_padre()
            if res:
                self.actual = res
                return True
            return False
        if not isinstance(self.actual,FolderNode):
            return False
        for d in self.actual.childs:
            directory_ls.append(d.getName())
        if name in directory_ls:
            res = self._driver.get(name)
            if res:
                self.browse += res.getName()+"/"
                self.actual = res
                return True
        return False

    # ======================== ENCODING ==================> ...
    # pivot para verificar si se esta siguiendo el rango de entradas
    def _eval_grado(self, directory: FolderNode | File, directorys: list[str]):
        child_list: list[str] = []
        print(directorys)
        if isinstance(directory, FolderNode):
            childs = directory.childs
            for c in childs:
                child_list.append(c.getName())
        else:
            if len(directorys) == 0:
                return directory
        if len(directorys) == 0:
            return directory
        if directory.getName() == child_list[0]:
            res = self._driver.get(child_list[1])
            if res:
                directorys.pop(0)
                self.browse += directory.getName()+'/'
                self._eval_grado(res,directorys)
    # ======================== ENCODING ==================> ...
        
    def _buscar_padre(self):
        directory_ls = self.browse.split('/')
        if self._driver.raiz.getName() == directory_ls[-2]:
            print("estas en la raiz del sistema...")
            return None
        res = self._driver.get(directory_ls[-3])
        if isinstance(res, FolderNode):
            directory_ls.pop()
            directory_ls.pop()
            self.browse = '/'.join(directory_ls) +'/'
            return res
        return None
        
        
    # comando DESC
    def _desc(self):
        """ Imprecion descendente del directorio actual (/desc)"""
        if isinstance(self.actual, FolderNode):
            res = DriveDirectory(self.actual)
            res.imprimir_postorden()
            return True
        return False
    # comando DIR
    def _dir(self):
        """ ver lista de directorios """
        if isinstance(self.actual, FolderNode):
            res = DriveDirectory(self.actual)
            res.imprimir_inorden()
            return True
        return False
    # comando HELP
    def _help(self):
        print("+ asc: imprecion ascendente desde el directorio actual.")
        print("+ cd: acceso al subfolder proximo al actual..")
        print("+ desc: impresion en orden descendente desde el directorio actual.")
        print("+ dir: impresion de directorios que se encuentran disponibles.")
        print("+ exit: salida del programa de comandos actual.")
        print("+ help: lista de comandos disponibles.")
        print("+ mkdir: generar nuevo folder en el directorio actual.")
        print("+ rmdir: remover un directorio del directorio actual.")
        print("+ type: reconocer el tipo de archivo.")
        return True
    # comando mkdir
    def _mkdir(self, new_folder:str) -> bool:
        return self._driver.add(self.actual.getName(),new_folder)
    # comando rmdir
    def _rmdir(self, delete_folder: str) -> bool:
        return self._driver.delete(delete_folder)