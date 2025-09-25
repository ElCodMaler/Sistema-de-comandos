from templates.unity import Unity
from templates.file import File
from .commands import Command
import json

class Driver:
    """ class that handles system operations """
    def __init__(self, unity: str, storage: int) -> None:
        self._file_json = f"{unity}.json"
        self._db_file = {}
        self._system = Unity(unity,storage)
        self._commands: Command
        self._create_system()
    # ================== UTILS ===============
    def start(self):
        """ System startup """
        cm = self._commands
        while True:
            res = input(f'{cm.browse}')
            if not cm.validation(res):
                print('command not found')
    # ====================== PROTECTED FUNCTIONS ======================
    def _create_system(self):
        """ generate the system """
        self._trasnform_json_dict()
        self._read_doc('',self._db_file)
        self._commands = Command(self._system.drive_folder)

    def _trasnform_json_dict(self):
        """ Find the location of the database and assign it to a variable such as a dictionary """
        with open(f'db/{self._file_json}', 'r', encoding='utf-8') as archivo:
            self._db_file = json.load(archivo)

    def _read_doc(self, father:str, dic: dict):
        """ Recursive function that saves the data from the JSON document to the system """
        for key, value in dic.items():
            if isinstance(value,dict):
                self._system.drive_folder.add(father,key)
                self._read_doc(key,value)
            else:
                self._system.drive_folder.add(father,File(key,value))