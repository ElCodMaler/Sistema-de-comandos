from templates.unity import Unity
from templates.file import File
from .commands import Command
import json

#class DRIVER
class Driver:
    def __init__(self, file: str, storage: int) -> None:
        self._file_json = f"{file}.json"
        self._db_file = {}
        self._system = Unity(file,storage)
        self._commands: Command
        self._create_system()
    # ================== UTILS ===============

    def start(self):
        """ Inicio del sistema """
        cm = self._commands
        while True:
            res = input(f'{cm.browse}')
            if not cm.validate(res):
                print('Comando no reconocido')

    # ====================== FUNCIONES PROTEGIDAS ======================
    def _create_system(self):
        """ Se genera el sistemas con todas las entradas"""
        self._trasnform_json_dict()
        self._read_doc('',self._db_file)
        self._commands = Command(self._system.drive_folder)

    def _trasnform_json_dict(self):
        with open(f'db/{self._file_json}', 'r', encoding='utf-8') as archivo:
            self._db_file = json.load(archivo)

    def _read_doc(self, padre:str, dic: dict):
        for key, value in dic.items():
            if isinstance(value,dict):
                self._system.drive_folder.add(padre,key)
                self._read_doc(key,value)
            else:
                self._system.drive_folder.add(padre,File(key,value))