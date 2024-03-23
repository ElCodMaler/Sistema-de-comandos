class Entrada_ficheros:
    """
    + ficheros: almacenara una lista de diccionarios que almacenaran los datos de su respectivo archivo.
    """
    def __init__(self, datos: dict):
        self.ficheros = []
        self.guardar_ficheros(datos)
    #metodos get
    def getFicheros(self):
        return self.ficheros
    #guardar datos del archivo en una lista
    def guardar_ficheros(self, datos: dict):
        for c in datos.values():
            self.ficheros.append(c)