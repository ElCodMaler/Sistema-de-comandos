#carpeta
class FolderN:
    def __init__(self, name:str):
        self.name = name
        self.content: FolderN | None =None