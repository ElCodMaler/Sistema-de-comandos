from .drive_folder import FolderN, File
from .tree_n_ario import DriveDirectory
from .tree_binario import Organizer
from errors.commands import ValidacionCommand

class Command:
    """
     + current: the current directory or File.
     + browse: representation of navigation.
    """
    def __init__(self, driver: DriveDirectory):
        self._driver = driver
        self.current: FolderN | File = self._driver.root
        self.browse: str = self.current.getName()+'/'
        self._execute_command: dict[str, any] = {
            'asc': self._asc,
            'desc': self._desc,
            'dir': self._dir,
            'ls': self._ls,
            'exit': exit,
            'help': self._help,
            'cd': self._cd,
            'mkdir': self._mkdir,
            'rmdir': self._rmdir
        }

    def validation(self, command: str):
        """ Validacion del comando ingresado """
        res = ValidacionCommand(command)
        cm = res.command
        if cm:
            if res.entry:
                self._execute_command[cm](res.entry)
                return
            self._execute_command[cm]()
            return

    # ====================== PROTECTED FUNCTIONS ======================
    def _cd(self, name: str) -> bool:
        """ directory navigation """
        directory_ls: list[str] = [] # lista de directorios
        nav_ls = name.split('/') # lista de navegacion
        if len(nav_ls) > 1:
            prev_folder = self.current
            prev_path = self.browse
            res = self._eval_grado(self.current ,nav_ls)
            if res:
                self.current = res
                return True
            self.browse =prev_path
            self.current = prev_folder
            return False
        elif name == '..':
            res = self._search_father()
            if res:
                self.current = res
                return True
            return False
        if not isinstance(self.current,FolderN):
            return False
        for d in self.current.children:
            directory_ls.append(d.getName())
        if name in directory_ls:
            res = self._driver.get(name)
            if res:
                self.browse += res.getName()+"/"
                self.current = res
                return True
        else:
            res = self._driver.root if self._driver.root.getName() == name else None
            if res:
                self.current = res
                self.browse = self.current.getName()+'/'
                return True
        return False
    # ================= PIVOT DIR ==================
    def _eval_grado(self, directory: FolderN | File, directorys: list[str]) -> FolderN | File | None:
        """ pivot to recognize the scale of directories """
        child_list: list[str] = []
        if isinstance(directory, FolderN):
            children = directory.children
            for c in children:
                child_list.append(c.getName())
        if not directorys:
            return directory
        if child_list[0] in directorys:
            res = self._driver.get(child_list[0])
            if res:
                directorys.pop(0)
                self.browse += res.getName()+'/'
                return self._eval_grado(res,directorys)
        
    def _search_father(self):
        """ find the previous directory """
        directory_ls = self.browse.split('/')
        if self._driver.root.getName() == directory_ls[-2]:
            print("you are at the root of the system")
            return None
        res = self._driver.get(directory_ls[-3])
        if isinstance(res, FolderN):
            directory_ls.pop()
            directory_ls.pop()
            self.browse = '/'.join(directory_ls) +'/'
            return res
        return None
    # ==================== end to pivot dir functions ==================

    def _asc(self) -> bool:
        """ ascending impression of folders and files """
        if isinstance(self.current, FolderN):
            res = Organizer(self.current)
            res.print_info_preorder()
            return True
        return False

    def _desc(self):
        """ printing folders and files in descending order """
        if isinstance(self.current, FolderN):
            res = Organizer(self.current)
            res.print_info_postorder()
            return True
        return False

    def _dir(self):
        """ display the contents of the folder """
        if isinstance(self.current, FolderN):
            res = Organizer(self.current)
            res.print_list()
            return True
        return False

    def _help(self):
        """ show available commands """
        print("asc | ascending impression of folders and files")
        print("desc | printing folders and files in descending order")
        print("dir | display the contents of the folder")
        print("ls | detailed list of subfolders")
        print("exit | close the program")
        print("help | show available commands")
        print("cd [directory] or [..] | directory navigation")
        print("mkdir [name_folder] or [name_f1] [name_f2] ..[name_n] | generate one or more folders in the current directory")
        print("rmdir [name_folder] or [name_f1] [name_f2] ..[name_n] | remove one or more empty files")
        print("type [name_file] | show file content")
        return True
    
    def _ls(self):
        """ detailed list of subfolders (ls) """
        if isinstance(self.current, FolderN):
            res = Organizer(self.current)
            res.print_info_preorder()
            return True
        return False

    def _mkdir(self, new_folder:str) -> bool:
        return self._driver.add(self.current.getName(),new_folder)

    def _rmdir(self, delete_folder: str) -> bool:
        return self._driver.delete(delete_folder)