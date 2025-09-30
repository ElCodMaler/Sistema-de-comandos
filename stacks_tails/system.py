from templates.unity import Unity
from templates.file import File
from .drivers.drive_command import DriverCommand, DriveDirectory
from tools import save

class CommandSystem:
    """ class that handles system operations """
    def __init__(self, unity: str, storage: int):
        self._db_file = save.trasnform_json_dict(unity)
        self._system = Unity(unity,storage)
        self._system.drive_folder = DriveDirectory(unity)
        #self._save_info_doc('',self._db_file)
        self._commands = DriverCommand(self._system.drive_folder)
    # ================== UTILS ===============
    def start(self):
        """ System startup """
        while True:
            entry = input(f"\n{self._commands.route()}")
            self._commands.validation(entry)
    # ====================== PROTECTED FUNCTIONS ======================
    def _save_info_doc(self, father:str, dic: dict[str,dict[str,any] | str]):
        """ Recursive function that saves the data from the JSON document to the system """
        for key, value in dic.items():
            if isinstance(value,dict):
                self._system.drive_folder.createFolder(key)
                self._system.drive_folder.change_directory(key)
                self._save_info_doc(key,value)
            else:
                char_ls = key.split('.')
                self._system.drive_folder.add(father,File(char_ls[0],char_ls[1],value))