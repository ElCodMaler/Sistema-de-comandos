from elementos_terminal import Fichero, Carpeta, Unidad
from Comandos import Comando
import json
#clase introducir Datos
class introducirDatos(Carpeta, Fichero, Unidad):
    #contructor
    def __init__(self, valorJson):
        self.unidades = []
        self.carpetas = []
        self.ficheros = []
        self.idCarpeta = 1
        self.idFichero = 1
        self.idUnidad = 1
        self.peso = 0
        self.valorJson = valorJson
        self.listaUnidades = self.crearUnidades(valorJson)
        self.leerJson(valorJson)
    #metodo que evaluara la informacion del valor del Atributo
    def evaluarAtributos(self, valor):
        bandera = True
        if type(valor) == str:
            bandera = False
        return bandera
    #metodo que almacenara las unidades
    def crearUnidades(self, valorJ):
        unidad1 = []
        for llave in valorJ:
            unidad1.append(llave)
        return unidad1
    #metodo que evalua si dos valores son iguales
    def comparador(self, valor, Array):
        bandera = False
        for a in Array:
            if valor == a:
                bandera = True
        return bandera
    #metodo que recorre los valores de los diccionarios o Arrays
    def listaDatos(self, valor):
        carpeta1 = []
        fichero1 = []
        for llave in valor:
            if self.evaluarAtributos(llave):
                carpeta1.append(str(llave))
            else:
                fichero1.append(str(llave))
        return carpeta1, fichero1
    #metodo que suma los valores de cada fichero
    def sumaFichero(self, dato, peso):
        for llave, valor in dato.items():
            if self.evaluarAtributos(valor):
                self.sumaFichero(valor,peso)
            else:
                peso = self.pesoKb(valor) + peso
        return peso
    #metodo calcular peso en kb
    def pesoKb(self, dato):
        pesoBits = len(dato)
        return pesoBits * 1024 ** 2
    #metodo evaluar extencion
    def extencion(self, name):
        tipo = [".txt",".exe",".doc",".html",".jpg",".mp4",".mp3",".pdf"]
        bandera = False
        for extencion in tipo:
            if extencion in name:
                bandera = True
        return bandera
    #metodo que almacenara los datos del json en un Array de cada tipo de clase
    def leerJson(self, valorJson):
        for llave, valor in valorJson.items():
            if self.evaluarAtributos(valor):
                #print(f' la carpeta {llave} contiene: {len(valor)} archivos')
                listaC, listaF = self.listaDatos(valor)
                peso = self.sumaFichero(valor,self.peso)
                self.carpetas.append(Carpeta(1, str(llave), listaF, listaC, peso))
                #self.idCarpeta = self.idCarpeta + 1
                self.leerJson(valor)
            elif self.comparador(llave, self.listaUnidades):
                listaC, listaF = self.listaDatos(valor)
                self.unidades.append(Unidad(self.idUnidad, str(llave), 400, 400, listaC))
                self.idUnidad = self.idUnidad + 1
            else:
                #print(f'{llave} es un archivo')
                extencion = self.extencion(llave)
                peso = self.pesoKb(valor)
                self.ficheros.append(Fichero(self.idFichero, str(llave), extencion, peso, valor))
                self.idFichero = self.idFichero + 1
#INICIALIZANDO VARIABLES
#obteniendo datos del archivo Json
with open("datos.json","r") as info:
    datos = info.read()
#decodificando el archivo Json a un diccionario
dict_datos = json.JSONDecoder().decode(datos)
#INICIO DEL PROGRAMA
introducirDatos(dict_datos)