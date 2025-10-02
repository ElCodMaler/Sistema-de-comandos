from .drive_directory import DriveDirectory, File
from errors.commands import ValidacionCommand
from templates.unity import Unity

class DriverCommand:
    """
     + unity: root command system Unity
     + run_command: dictionary of command functions
    """
    def __init__(self, unity: Unity[DriveDirectory]):
        self._unity = unity
        self._run_command: dict[str, any] = {
            'asc': self._asc,
            'desc': self._desc,
            'dir': self._dir,
            'ls': self._ls,
            'exit': exit,
            'help': self._help,
            'cd': self._cd,
            'mkdir': self._mkdir,
            'rmdir': self._rmdir,
            'type': self._type
        }

    def validation(self, command: str):
        """ Validation of the entered command """
        res = ValidacionCommand(command)
        cm = res.command
        if cm:
            if res.entry:
                self._run_command[cm](res.entry)
                return
            self._run_command[cm]()

    def route(self) -> str:
        """ current directory path """
        return self._unity.drive_folder.show_current_route()

    # ====================== PROTECTED FUNCTIONS ======================
    def _asc(self):
        self._unity.drive_folder.print_asc()

    def _desc(self):
        self._unity.drive_folder.print_desc()

    def _cd(self, name_directory: str):
        """ directory navigation """
        self._unity.drive_folder.change_directory(name_directory)

    def _dir(self):
        """ display the contents of the folder """
        self._unity.drive_folder.print_list()

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
        self._unity.drive_folder.print_info()

    def _mkdir(self, folder_name:str | list[str]):
        """ create a folder """
        if isinstance(folder_name, list):
            self._unity.drive_folder.create_multiple_folders(folder_name)
            return
        self._unity.drive_folder.createFolder(folder_name)

    def _rmdir(self, folder_name:str | list[str]):
        """ delete a folder """
        if isinstance(folder_name, list):
            self._unity.drive_folder.delete_multiple_folders(folder_name)
        self._unity.drive_folder.deleteElement(folder_name)

    def _type(self, file_name: str):# ENCODING ...
        """ show file content """
        res = self._unity.drive_folder.getElement(file_name)
        if isinstance(res, File):
            print(res.getContent())
        if res:
            print('This command only works for files')