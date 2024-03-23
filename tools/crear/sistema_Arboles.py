from components.elementos_sistema import Carpeta, Fichero, Unidad
from tools.TDA.arboles.sistema_Carpetas import FolderSystem
from tools.TDA.arboles.sistema_ficheros import FileSystem
from tools.TDA.arboles.sistema import System
import json
import sys

#Clase para crear el sistema
class CrearSistema:
    """
    + sistema_carpetas: se almacenaran los FolderSystem existentes
    + sistema_ficheros: se almacenaran los FileSystem existentes
    + system: se almacenara el sistema con todas sus conexiones
    + lista_dicheros: se almacenara una lista de objetos Fichero, donde tendra almacenado
    cada objeto para almacenarlo.
    """
    def __init__(self, archivos: list[list[list]], carpetas: list[list[list]]):
        self.sistema_Carpetas = [FolderSystem() for cantidad in range(len(carpetas))]
        self.sistema_ficheros = [[FileSystem() for cantidad in range(len(carpetas[archC]))] for archC in range(len(carpetas))]
        self.lista_ficheros: list[list[Fichero]] = [[] for archF in range(len(archivos))]
        self.system = System()
        self.guarda_ficheros(archivos)
        self.guardar_carpetas(carpetas)
        self.crear_sistema_ficheros()
        self.crear_unidades()
        #self.asignar_ficheros_carpetas()
        #self.asignar_carpetas_sistema()
    #metodos get
    def getSystem(self):
        return self.system
    #generar usuario
    def user(self) -> str:
        return input('Nombre de Usuario: ')
    #guardar carpetas
    def guardar_carpetas(self, carpetas: list[list[list]]):
        for archJ in range(len(carpetas)):
            for doc in range(len(carpetas[archJ])):
                self.sistema_Carpetas[archJ].insertar_Carpeta(Carpeta(carpetas[archJ][doc][0],carpetas[archJ][doc][1],carpetas[archJ][doc][2]))
            self.sistema_Carpetas[archJ].setUser(self.user())
    #guardar ficheros
    def guarda_ficheros(self, ficheros: list[list[list]]):
        for archJ in range(len(ficheros)):
            for fich in range(len(ficheros[archJ])):
                archJson = json.dumps(ficheros[archJ][fich])
                peso = sys.getsizeof(archJson)
                self.lista_ficheros[archJ].append(Fichero(ficheros[archJ][fich][0],ficheros[archJ][fich][1],ficheros[archJ][fich][2],peso,ficheros[archJ][fich][4]))
    #generar sistema
    def crear_unidades(self):
        self.system.agregar_unidad(Unidad(1,"C:",800,0,None,'SSD'))
        self.system.agregar_unidad(Unidad(2,'Jorge',200,0,None,"USB"))
    #conectar sistema de carpetas con el sistema
    def conectar_sistema(self):
        for i in len(self.sistema_Carpetas):
            if i == 0 or i == 2:
                self.system.asignar_raiz('C:',self.sistema_Carpetas[i])
            else:
                self.system.asignar_raiz('Jorge',self.sistema_Carpetas[i])
    #crear el sistema de ficheros
    def crear_sistema_ficheros(self):
        for arch in range(len(self.sistema_Carpetas)):

            nodoR = self.sistema_Carpetas[arch].getUser()

            if self.sistema_Carpetas[arch].buscar_carpeta('Imagenes',nodoR):
                for fich in self.lista_ficheros[arch]:
                    if fich.getExtencion() == '.jpg' or fich.getExtencion() == '.jpeg':
                        self.sistema_ficheros[arch][0].crear_archivo(fich)
                    else:
                        print('No existen archivos de Imagen en Ach',arch)
            else:
                print('no existe la carpeta Imagenes en:',self.sistema_Carpetas[arch].getUserName())
                                
            if self.sistema_Carpetas[arch].buscar_carpeta('Videos',nodoR):
                for fich in range(len(self.lista_ficheros[arch])):
                    if self.lista_ficheros[arch][fich].getExtencion() == '.mp4':
                        self.sistema_ficheros[arch][1].crear_archivo(self.lista_ficheros[arch][fich])
                    else:
                        print('No existen archivos de Video en Ach',arch)
            else:
                print('no existe la carpeta Videos en:',self.sistema_Carpetas[arch].getUserName())

            if self.sistema_Carpetas[arch].buscar_carpeta('Musica',nodoR):
                for fich in self.lista_ficheros[arch]:
                    if fich.getExtencion() == '.mp3':
                        self.sistema_ficheros[arch][2].crear_archivo(fich)
                    else:
                        print('No existen archivos de Musica en Ach',arch)
            else:
                print('no existe la carpeta Musica en:',self.sistema_Carpetas[arch].getUserName())

            if self.sistema_Carpetas[arch].buscar_carpeta('Documentos',nodoR):
                for fich in self.lista_ficheros[arch]:
                    self.sistema_ficheros[arch][3].crear_archivo(fich)
            else:
                print('no existe carpeta de Documentos en:',self.sistema_Carpetas[arch].getUserName())
                        
                                
    #asignar el sistema de ficheros a cada carpeta
    def asignar_ficheros_carpetas(self):
        for foldS in self.sistema_Carpetas:
            for archJ in self.sistema_ficheros:
                for fileS in archJ:
                    if foldS.buscar_carpeta('Imagenes',foldS.getUser()) and (fileS.get_raiz().archivo.getExtencion() in 'jpg' or fileS.get_raiz().archivo.getExtencion() in 'jpeg'):
                        foldS.asignarFileSystem('Imagenes',fileS)
                    if foldS.buscar_carpeta('Videos',foldS.getUser()) and fileS.get_raiz().archivo.getExtencion() in 'mp4':
                        foldS.asignarFileSystem('Videos',fileS)
                    if foldS.buscar_carpeta('Musica',foldS.getUser()) and fileS.get_raiz().archivo.getExtencion() in 'mp3':
                        foldS.asignarFileSystem('Musica',fileS)
                    foldS.asignarFileSystem('Documentos',fileS)
    #asignar carpetas al sistema
    def asignar_carpetas_sistema(self):
        foldS = self.sistema_Carpetas
        self.system.asignar_raiz('C:',foldS[0])
        self.system.asignar_raiz('Jorge',foldS[1])