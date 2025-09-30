from .drive_directory import DriveDirectory
from errors.commands import ValidacionCommand
#from templates.unity import Unity

class DriverCommand:
    """
     + current: the current directory or File.
     + browse: representation of navigation.
    """
    def __init__(self, driver: DriveDirectory):
        self._driver = driver
        self._execute_command: dict[str, any] = {
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

    def route(self) -> str:
        return self._driver.show_current_route()

    # ====================== PROTECTED FUNCTIONS ======================
    def _cd(self, name: str):
        """ directory navigation """
        self._driver.change_directory(name)

    def _dir(self):
        """ display the contents of the folder """
        self._driver.print_list()

    def _help(self):
        """ show available commands """
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
        self._driver.print_info()

    def _mkdir(self, folder_name:str):
        self._driver.createFolder(folder_name)

    def _rmdir(self, folder_name:str):
        self._driver.deleteElement(folder_name)