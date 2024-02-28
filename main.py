from tools.Sistema import baseDatos
import json
#clase donde se usaran los comandos del sistema
class Terminal(baseDatos):
    def __init__(self, archivoJson):
        self.bd = baseDatos(archivoJson)
        self.carpetas = self.bd.getListaCarpetas()
        self.ficheros = self.bd.getListaFicheros()
        self.unidades = self.bd.getListaUnidades()
    #metodo que recorrera todas las carpetas dentro de los objetos carpeta
    def recorrerCarpetas(self, carpeta, ArrayName):
        for c in carpeta.getListaCarpetas():
            if c.getNombre() in ArrayName:
                self.recorrerCarpetas(c, ArrayName)
            elif ArrayName[-1] == c.getNombre():
                return True
            else:
                return False
    #metodo que evalua la ubicacion
    def compararUbicacion(self,  entradaUnidad, entradaUbicar):
        #separar todos los caracteres de la ubicacion por cada barra de separacion, y guardarlos en un array que tendra cada palabra
        evaluarUbic = str(entradaUbicar).split('/')
        #inicia el ciclo de estudio
        #del array unidades se retornara en cada siclo cada objeto clase
        for unidad in self.unidades:
            #se evaluara si hay similitud entre el nombre del objeto unidad y la unidad que se ingreso 
            if entradaUnidad == unidad.getNombre():
                #desde el objeto unidad se creara un ciclo que recorra una lista de onjetos carpeta que se encuentra dentro del mismo objeto unidad
                for carpeta in unidad.getListaCarpetas():
                    #se busca obtener la ubicacion del que se inserte recorriendo las carpetas hasta llegar al punto final...
                    #si no se encuentra la ubicacion durante el recorrido, quiere decir que esa ubicacion no existe
                    for i in len(0,evaluarUbic):
                        #obtenemos el objeto carpeta y evaluamos si existe la primera carpeta...
                        if carpeta.getNombre() == evaluarUbic[i]:
                            if self.recorrerCarpetas(carpeta, evaluarUbic):
                                print('se consiguio su valor')
                            else:
                                print('no se encontro su ubicacion')
                        else:
                            print(f'no se encuentra la carpeta {carpeta.getNombre()}')

            else:
                print('no existe la unidad que usted inserto')


#INICIALIZANDO VARIABLES
#obteniendo datos del archivo Json
with open("datos.json","r") as info:
    datos = info.read()
#decodificando el archivo Json a un diccionario
dict_datos = json.JSONDecoder().decode(datos)
#INICIO DEL PROGRAMA
t = Terminal(dict_datos)
print(t.getListaCarpetas())
t.compararUbicacion('C:','C:/Usuarios/Carlos/documentos/contra.txt')