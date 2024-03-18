class entrada_ficheros:
    """
    + ficheros: almacenara una lista de diccionarios que almacenaran los datos de su respectivo archivo.
    + datos_ficheros: almacenara una matriz de los datos de los archivos donde el primer indice representa
    el archivo y el segundo indice el tipo de dato correspondiente al respectivo archivo.

    ejemplo: fichero[0] = archivo1 --> fichero[0][0] = id del archivo1
                                       fichero[0][1] = nombre del archivo1
                                       fichero[0][2] = extencion del archivo1
                                       fichero[0][3] = peso del archivo1
    """
    def __init__(self, datos: dict):
        self.ficheros = []
        self.datos_ficheros = [[] for l in range(len(datos))]
        self.guardar_ficheros(datos)
        self.guardar_datos_ficheros()
    #metodos get
    def getFicheros(self):
        return self.ficheros
    
    def getDatosFicheros(self):
        return self.datos_ficheros
    #guardar datos del archivo en una lista
    def guardar_ficheros(self, datos: dict):
        for c in datos.values():
            self.ficheros.append(c)
    #guardar cada uno de los datos
    def guardar_datos_ficheros(self):
        i = 0
        for f in self.ficheros:
            self.datos_ficheros[i].append(f['id'])
            self.datos_ficheros[i].append(f['nombre'])
            self.datos_ficheros[i].append(f['extencion'])
            self.datos_ficheros[i].append(f['peso'])
            self.datos_ficheros[i].append(f['datos'])
            i = 1 + i