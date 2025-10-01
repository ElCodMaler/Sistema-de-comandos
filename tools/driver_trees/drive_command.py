from errors.commands import ValidacionCommand
from templates.unity import Unity
from .tree_nary import DriveDirectory
from .tree_binary import Organizer

class DriverCommand:
    """
     + unity: root command system Unity
     + run_command: dictionary of command functions
    """
    def __init__(self, unity: Unity[DriveDirectory]):
        self._unity = unity
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
    # ============== UTILITIES =============

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
        
    def route(self) -> str:
        """ current directory path """
        return self._unity.drive_folder.getRoute()

    # ====================== PROTECTED FUNCTIONS ======================

    def _cd(self, name: str):
        """ directory navigation """
        self._unity.drive_folder.change_directory(name)

    def _asc(self):
        """ ascending impression of folders and files """
        res = Organizer(self._unity.drive_folder.getCurrentDirectory())
        res.print_info_preorder()

    def _desc(self):
        """ printing folders and files in descending order """
        res = Organizer(self._unity.drive_folder.getCurrentDirectory())
        res.print_info_postorder()

    def _dir(self):
        """ display the contents of the folder """
        self._unity.drive_folder.print_list()

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
    
    def _ls(self):
        """ detailed list of subfolders (ls) """
        self._unity.drive_folder.print_info()

    def _mkdir(self, new_folder:str):
        """ create a folder """
        self._unity.drive_folder.createFolder(new_folder)

    def _rmdir(self, delete_folder: str):
        """ delete a folder """
        self._unity.drive_folder.deleteElement(delete_folder)

    def _type(self): # ENCODING ....
        """ show file content """
        pass