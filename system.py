import os
from dotenv import load_dotenv
from tools import save
from tools.drivers.drive_command import DriverCommand, DriveDirectory, Unity

class CommandSystem:
    """ The command system """
    def __init__(self, unity: str='C', storage: int=2000):
        db_file = save.trasnform_json_dict(unity)
        # generamos el sistema
        self._system: Unity[DriveDirectory] = Unity(unity,storage)
        self._system.setDriverSystem(DriveDirectory(unity))
        #creamos el sistema
        self._save_to_system(db_file)
        # le asignmaos el sistema de comandos
        self._commands = DriverCommand(self._system)
    # ================== UTILS ===============
    def start(self):
        """ System startup """
        STRUCTURE = os.getenv('STRUCTURE')
        if STRUCTURE == 'linked':
            self.title_linked_list()
        elif STRUCTURE == 'tree':
            self.title_trees()
        while True:
            entry = input(f"\n{self._commands.route()}")
            self._commands.validation(entry)
    # ====================== PROTECTED FUNCTIONS ======================
    def _save_to_system(self, dic: dict[str,dict[str,any] | str]):
        """ Recursive function that saves the data from the JSON document to the system """
        lista_str = [(key, value) for key, value in dic.items() if isinstance(value, str)]
        lista_dict = [(key, value) for key, value in dic.items() if isinstance(value, dict)]
        if lista_str:
            for key, value in lista_str:
                self._system.drive_folder.createFile(key, value)
        if lista_dict:
            for key, value in lista_dict:
                self._system.drive_folder.createFolder(key)
        for key, value in lista_dict:
            self._system.drive_folder.change_directory(key)
            self._save_to_system(value)
        self._system.drive_folder.change_directory('..')

    def title_linked_list(self):
        print('='*50)
        print(' '*5+'WELCOME TO COMMAND SYSTEM OF LINKED LISTS')
        print('='*50)

    def title_trees(self):
        print('='*50)
        print(' '*5+'WELCOME TO COMMAND SYSTEM OF TREES')
        print('='*50)