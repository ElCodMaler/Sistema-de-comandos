class Entrada_carpetas:
    """
    + carpetas: almacenara una lista de diccionarios que almacenaran los datos de su respectivo carpeta.
    """
    def __init__(self, datos: dict):
        self.carpetas = []
        self.guardar_carpetas(datos)
    #metodos get
    def getCarpetas(self):
        return self.carpetas
    #guardar datos del archivo en una lista
    def guardar_carpetas(self, datos: dict):
        for c in datos.values():
            self.carpetas.append(c)