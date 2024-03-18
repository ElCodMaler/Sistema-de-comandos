#en desusuo
"""
from components.elementos_sistema import Fichero, Carpeta, Unidad
import os
#clase donde se almacenan todos los datos del archivo Json
class BaseDatos(Fichero,Carpeta,Unidad):
    '''
    + unidades: lista de objetos Unidad
    + valorJson: es el diccionario que se asignara a esta clase
    '''
    def __init__(self, valorJson: dict):
        self.unidades = [
            Unidad(1,'C:',800,None,None,'SSD'),
            Unidad(2,"USB:",200,None,None,"HDD")
        ]
        self.carpetas = [Carpeta]
        self.ficheros = [Fichero]
        self.valorJson = valorJson
        self.guardarInformacion(valorJson)

    #metodo get
    def getListaUnidades(self) -> list[Unidad]:
        return self.unidades
    
    #metodo que evaluara el tipo de dato
    def buscarCarpeta(self, valor: dict | str) -> bool:
        if type(valor) == dict:
            return True
        return False
    
    #metodo que evalua si un valor string se encuentra dentro de una lista
    def comparador(self, valor: str, Array: list[str]) -> bool:
        if valor in Array:
                return True           
        return False
    
    #metodo que suma los valores de cada fichero
    def sumaFichero(self, dato: dict, peso = 0) -> int:
        for llave in dato:
            if self.buscarCarpeta(dato[llave]):
                self.sumaFichero(dato[llave],peso)
            else:
                peso = self.pesoKb(dato[llave]) + peso
        return peso
    
    #metodo que indicara el la camtidad de informacion del documento json y retornara su valor en cantidad Kb
    def pesoKb(self, ubicacion: str) -> int:
        sizeFileBytes = os.path.getsize(ubicacion)
        return sizeFileBytes / 1024
    
    #metodo que calcula la diferencia de pesos de kiloBytes a MegaBytes
    def diferenciaPesos(self, pesoKb: int, pesoMb: int) -> int:
        return pesoMb - (pesoKb / 1024)
    
    #metodo que evaluara el tipo de extencion de un Fichero
    def extencion(self, name: str):
        tipo = [".txt",".exe",".doc",".html",".jpg",".mp4",".mp3",".pdf",".jpeg"]
        for extencion in tipo:
            if name in extencion:
                return extencion
        return None
    
    #metodo que evaluara el nombre de la unidad(NO SE USA)
    def nombreUnidad(self, dato: dict) -> bool:
        tipo = 'A:B:C:D:E:F:G:H:I:J:K:M:N:O:P:Q:R:S:T:U:V:W:X:Y:Z:USB:'
        if dato in tipo:
            return True
        else:
            return False

    def guardarCarpetas(self, docJ: dict[str, str | int]):
        valores = docJ.keys()
        for doc in valores:
            self.carpetas.append(Carpeta(docJ[doc]["id"],docJ[doc]["nombre"],docJ[doc]["peso"]))

    def guardarFicheros(self, docJ: dict[str, str | int]):
        valores = docJ.keys()
        for arch in valores:
            print(f'valor1 {arch}')
            #self.ficheros.append(Fichero(docJ[arch]["id"] ,docJ[arch]["nombre"] ,docJ[arch]["extencion"] ,docJ[arch]["peso"],docJ[arch]["datos"]))

    def guardarInformacion(self, docJ: dict[str, str | int]):
        escritorio = Carpeta
        self.guardarFicheros(docJ)
        self.guardarCarpetas(docJ)
        for f in self.ficheros:
            extencion = self.extencion(f.getExtencion())
            if extencion == ".jpg" or extencion == ".jpeg":
                for c in self.carpetas:
                    if c.getNombre() == "Fotos":
                        c.setFichero(c,f)
            elif extencion == ".mp3":
                for c in self.carpetas:
                    if c.getNombre() == "musica":
                        c.setFichero(c,f)
            elif extencion == ".mp4":
                for c in self.carpetas:
                    if c.getNombre() == "Videos":
                        c.setFichero(c,f)
            else:
                for c in self.carpetas:
                    if c.getNombre() == "Documentos":
                        c.setFichero(c,f)
                    if c.getNombre() == 'Escritorio':
                        escritorio = c
        for c in self.carpetas:
            if c.getNombre() == 'Escritorio':
                next
            escritorio.setCarpeta(escritorio,c)

    #metodo que retorne una lista de ficheros y una lista de carpetas
    # def listas_contenido(self, elemento: dict[str, dict | str]) -> tuple[list[Carpeta], list[Fichero]]:
    #     carpetas, ficheros = []
    #     for nombre, contenido in elemento:
    #         if self.buscarCarpeta(contenido):
    #             carpetas.append(Carpeta(self.ids[0][-1] + 1,nombre,self.sumaFichero(contenido)))
    #         else:
    #             ficheros.append(Fichero(self.ids[1][-1] + 1,elemento,self.extencion(elemento),self.pesoKb(contenido),contenido))
    #     return carpetas, ficheros
    #metodo que recorre los valores del diccionario y retorna una lista de objetos Carpeta y Fichero que se encuantran
    #en la ubicacion del atributo que se le asigna en el parametro
    # def datosUbicacion(self, dicJ: dict[str, dict | str]):
    #     for elemento, contenido in dicJ.items():
    #         lista = list[Carpeta]
    #         if self.buscarCarpeta(contenido):
    #             lista.append(Carpeta(self.ids[0][-1],elemento,self.sumaFichero(contenido)))
    #             c, f = self.listas_contenido(contenido)
    #             lista[self.ides[0][-1]-1].setCarpeta(c)
    #             lista[self.ides[0][-1]-1].setFichero(f)
    #             self.ides[0].append(self.ides[0][-1] + 1)
    #             self.datosUbicacion(contenido)
    #         else:
    #             return lista[0]
    #metodo que recorrera un dicccionario de acuerdo a sus primeros valores
    # def entrarUnidad(self, dicJ: dict) -> tuple[str, str]:
    #     for unidad in dicJ:
    #         carpeta = self.datosUbicacion(dicJ[unidad])
    #         self.unidades.append(Unidad(self.ids[2][-1] + 1,unidad,700,self.diferenciaPesos(700,self.sumaFichero(dicJ[unidad])),carpeta,'HDD'))
"""