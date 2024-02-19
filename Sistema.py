from elementos_terminal import Fichero, Carpeta, Unidad
#clase donde se almacenan todos los datos del archivo Json
class baseDatos(Fichero,Carpeta,Unidad):
    '''
    + unidades: lista de objetos Unidad
    + ids: es un lista que identificara cada objeto
    + valorJson: es el diccionario que se asignara a esta clase
    '''
    def __init__(self, valorJson: dict):
        self.unidades = []
        self.ids = [[1],[1],[1]]
        self.valorJson = valorJson
        self.entrarUnidad(valorJson)
    #metodo get
    def getListaUnidades(self) -> list[Unidad]:
        return self.unidades
    #metodo que evaluara el tipo de dato
    def evaluarAtributos(self, valor: dict | str) -> bool:
        bandera = True
        if type(valor) == str:
            bandera = False
        return bandera
    #metodo que evalua si un valor se encuentra dentro de una lista
    def comparador(self, valor: str, Array: list[str]) -> bool:
        bandera = False
        if valor in Array:
                bandera = True           
        return bandera
    #metodo que suma los valores de cada fichero
    def sumaFichero(self, dato: dict, peso = 0) -> int:
        for llave in dato:
            if self.evaluarAtributos(dato[llave]):
                self.sumaFichero(dato[llave],peso)
            else:
                peso = self.pesoKb(dato[llave]) + peso
        return peso
    #metodo que contara la cantidad de caracteres del fichero, lo que representara el peso en bits, para luego
    #hacer las trasformacion de bits a Kilo Bytes
    def pesoKb(self, dato: str) -> int:
        pesoBits = len(dato)
        return (pesoBits * 1024) ** 2
    #metodo que calcula la diferencia de pesos de kiloBytes a MegaBytes
    def diferenciaPesos(self, pesoKb: int, pesoMb: int) -> int:
        return pesoMb - (pesoKb / 1024)
    #metodo que evaluara el tipo de extencion de un Fichero
    def extencion(self, name: str) -> str:
        tipo = [".txt",".exe",".doc",".html",".jpg",".mp4",".mp3",".pdf"]
        dato = ''
        for extencion in tipo:
            if extencion in name:
                dato = extencion
            else:
                dato = "None"
        return dato
    #metodo que evaluara el nombre de la unidad
    def nombreUnidad(self, dato: dict) -> bool:
        tipo = 'A:B:C:D:E:F:G:H:I:J:K:M:N:O:P:Q:R:S:T:U:V:W:X:Y:Z:USB:'
        if dato in tipo:
            return True
        else:
            return False
    #metodo que recorre los valores del diccionario y retorna una lista de objetos Carpeta y Fichero que se encuantran
    #en la ubicacion del atributo que se le asigna en el parametro
    def datosUbicacion(self, dicJ: dict[str, dict | str]) -> tuple[list[Carpeta] ,list[Fichero]] | list[Carpeta]:
        carpetas = []
        ficheros = []
        for llave, valor in dicJ.items(): 
            if self.evaluarAtributos(valor):
                c, f = self.datosUbicacion(valor)
                carpetas.append(Carpeta(self.ids[0][-1] + 1,llave,f,c,self.sumaFichero(valor)))
            else:
                ficheros.append(Fichero(self.datos[1][-1] + 1,llave,self.extencion(llave),self.pesoKb(valor),valor))
        if carpetas == []:
            return ficheros
        elif ficheros == []:
            return carpetas
        else:
            return carpetas, ficheros
    #metodo que recorrera un dicccionario de acuerdo a sus primeros valores
    def entrarUnidad(self, dicJ: dict):
        for llave in dicJ:
            c = self.datosUbicacion(dicJ[llave])
            self.unidades.append(Unidad(self.datos[2][-1] + 1,llave,700,self.diferenciaPesos(700,self.sumaFichero(dicJ[llave])),c,'HDD'))