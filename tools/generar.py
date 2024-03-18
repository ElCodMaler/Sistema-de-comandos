from .guardar.guardar_archivos import entrada_ficheros
from .guardar.guardar_carpetas import entrada_carpetas
from components.elementos_sistema import Carpeta, Fichero, Unidad
from tools.TDA.sistema_Carpetas import FolderSystem
from tools.TDA.sistema_ficheros import FileSystem
from tools.TDA.sistema import System
import json
import sys

#inicializacion de variables
lista_Fich, lista_Carp = [], []
lista_entradasFich, lista_entradasCarp = [], []
archivos, carpetas = [], []
#lectura del archivo Json
for i in range(2):
    with open(f"DataBase\Carpetas{i+1}.json", 'r') as archivo:
        lista_Carp.append(json.load(archivo))
for i in range(3):
    with open(f"DataBase\Archivos{i+1}.json", 'r') as archivo:
        lista_Fich.append(json.load(archivo))
#se guarda la informacion de cada archivo o carpeta
for i in range(3):
    lista_entradasFich.append(entrada_ficheros(lista_Fich[i]))
for i in range(2):
    lista_entradasCarp.append(entrada_carpetas(lista_Carp[i]))
#se guardan la informacion de cada archivo o carpeta por secciones
for i in range(3):
    archivos.append(lista_entradasFich[i].getDatosFicheros())
for i in range(2):
    carpetas.append(lista_entradasCarp[i].getDatosCarpetas())
# se crea el sistema
class crear_sistema:
    def __init__(self, archivos: list, carpetas: list):
        self.sistema_Carpetas = [FolderSystem() for c in range(len(carpetas))]
        self.lista_ficheros: list[Fichero] = []
        self.system = System()
        self.guarda_ficheros(archivos)
        self.guardar_carpetas(carpetas)
        self.crear_unidades()
    #generar usuario
    def user(self) -> str:
        return input('Nombre de Usuario: ')
    #guardar carpetas
    def guardar_carpetas(self, carpetas: list):
        index = 0
        for c in carpetas:
            self.sistema_Carpetas[index].insertar_Carpeta(Carpeta(c[0],c[1],c[2]))
            self.sistema_Carpetas[index].setUser(self.user())
            index = index + 1
            
    #guardar ficheros
    def guarda_ficheros(self, ficheros: list):
        for f in ficheros:
            archJson = json.dumps(f)
            peso = sys.getsizeof(archJson)
            self.lista_ficheros.append(Fichero(f[0],f[1],f[2],peso,f[4]))
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
    #conectar sistema de ficheros con el sistema de carpetas
    def conectar_ficheros_carpetas(self):
        sistema_fich = FileSystem()
        for c in self.sistema_Carpetas:
            if c.buscar_carpeta('Fotos',c.getUser()):
                for f in self.lista_ficheros:
                    if f.getExtencion() in 'jpg' or f.getExtencion() in 'jpeg':
                        sistema_fich.crear_archivo(Fichero())
            if c.buscar_carpeta('Videos',c.getUser()):
                for f in self.lista_ficheros:
                    if f.getExtencion() in 'mp4':
                        sistema_fich.crear_archivo(Fichero())
            if c.buscar_carpeta('Musica',c.getUser()):
                for f in self.lista_ficheros:
                    if f.getExtencion() in 'mp3':
                        sistema_fich.crear_archivo(Fichero())
            if c.buscar_carpeta('Documentos',c.getUser()):
                for f in self.lista_ficheros:
                    sistema_fich.crear_archivo(Fichero())
                        
            