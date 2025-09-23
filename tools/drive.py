from .TDA.trees.system import System
from templates.unity import Unity
from templates.file import File
from templates.folder import Folder
import json
#class DRIVER
class Driver:
    def __init__(self, file: str) -> None:
        self.file_json = f"{file}.json"
        self.db_file = {}
        self.system = System(Unity(file,3000))
    #
    def createSystem(self):
        self._trasnform_json_dict()
        self._enter_data()

    def _trasnform_json_dict(self):
        with open(f'db/{self.file_json}', 'r', encoding='utf-8') as archivo:
            self.db_file = json.load(archivo)

    def _enter_data(self):
        if not self.db_file:
            raise ValueError("No se pueden ingresar los datos, el valor esta vacio")

    def _recorrido_file(self, padre:str, hijo, counter: int=0):
        folders = []
        for key, value in self.db_file:
            if isinstance(value,dict):
                self.system.add(padre,Folder(key))
                folders.append(value)
            elif isinstance(value,str):
                self.system.add(File(key,value))
        for fol in folders:
            for key, value in fol:
                if isinstance(value,dict):
                    self.system.raiz.directory.add(Folder)

        

            

           


        
    