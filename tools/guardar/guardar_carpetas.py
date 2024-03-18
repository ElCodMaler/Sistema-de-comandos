class entrada_carpetas:
    """
    + carpetas: almacenara una lista de diccionarios que almacenaran los datos de su respectivo carpeta.
    + datos_carpetas: almacenara una matriz de los datos de las carpetas donde el primer indice representa
    la carpeta y el segundo indice el tipo de dato correspondiente a su respectiva carpeta.
    
    ejemplo: carpeta[0] = carpeta1 --> carpeta[0][0] = id del carpeta1
                                       carpeta[0][1] = nombre del carpeta1
                                       carpeta[0][2] = peso del carpeta1
    """
    def __init__(self, datos: dict):
        self.carpetas = []
        self.datos_carpetas = [[] for l in range(len(datos))]
        self.guardar_carpetas(datos)
        self.guardar_datos_carpetas()
    #metodos get
    def getCarpetas(self):
        return self.carpetas
    
    def getDatosCarpetas(self):
        return self.datos_carpetas
    #cantidad de carpetas que hay
    def cantidad_listas(A: dict):
        res = []
        for l in range(len(A)):
            res.append([])
        return res
    #guardar datos del archivo en una lista
    def guardar_carpetas(self, datos: dict):
        for c in datos.values():
            self.carpetas.append(c)
    #guardar cada uno de los datos
    def guardar_datos_carpetas(self):
        i = 0
        for c in self.carpetas:
            self.datos_carpetas[i].append(c['id'])
            self.datos_carpetas[i].append(c['nombre'])
            self.datos_carpetas[i].append(c['peso'])
            i = 1 + i