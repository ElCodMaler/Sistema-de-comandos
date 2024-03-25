class User:
    def __init__(self):
        self.user_name: str
        self.acceso: bool
    #metodos get
    def getName(self) -> str:
        return self.user_name
    
    def getTipo(self) -> bool:
        return self.tipo
    #metodos set
    def setName(self, name: str):
        self.user_name = name
    
    def setAcceso(self, tipo: bool):
        self.acceso = tipo
    #generar usuario
    def generarUsuario(self):
        print('<bienvenido al sistema de comandos>')
        name = input('escriba nombre de Usuario:')
        acces = input('desea acceso de administrado? (S/N):')
        if acces == 'S' or acces == 's':
            self.setAcceso(True)
        elif acces == 'N' or acces == 'N':
            self.setAcceso(False)
        self.setName(name)  