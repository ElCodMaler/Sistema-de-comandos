from templates.unity import Unity
from templates.file import File
from tools import save
from .commands import Command

class TreeDriver:
    """ class that handles system operations """
    def __init__(self, unity: str, storage: int):
        self._db_file = save.trasnform_json_dict(unity)
        self._system = Unity(unity,storage)
        self._save_info_doc('',self._db_file)
        self._commands = Command(self._system.drive_folder)
    # ================== UTILS ===============
    def start(self):
        """ System startup """
        cm = self._commands
        while True:
            res = input(f'{cm.browse}')
            if not cm.validation(res):
                print('command not found')
    # ====================== PROTECTED FUNCTIONS ======================
    def _save_info_doc(self, father:str, dic: dict):
        """ Recursive function that saves the data from the JSON document to the system """
        for key, value in dic.items():
            if isinstance(value,dict):
                self._system.drive_folder.add(father,key)
                self._save_info_doc(key,value)
            else:
                self._system.drive_folder.add(father,File(key,value))