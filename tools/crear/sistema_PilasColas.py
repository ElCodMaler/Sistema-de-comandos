from components.elementos_sistema import Unidad, Carpeta, Fichero
from tools.validaciones.validar_comandos import ValidarComando
from tools.TDA.pilas_colas.pilas import Pila
from components.usuario import User
import json
import sys

class CrearSistema:
    """
    + lista_ficheros: se almacenara una lista de objetos Fichero, donde tendra almacenado
    cada objeto para almacenarlo.
    """
    def __init__(self, archivos: list[dict], carpetas: list[dict]):
        #variables
        self.lista_ficheros: list[Fichero] = []
        self.lista_carpetas: list[Carpeta] = []
        self.sistema = [Unidad(1,"C:",700,700,Pila(),"SSD"),User()]
        self.command = ValidarComando
        #uso de metodos
        self.sistema[1].generarUsuario()
        self.registro_busqueda = f'{self.sistema[0].getNombre()}/user/{self.sistema[1].getName()}'
        self.guarda_ficheros(archivos)
        self.guarda_carpetas(carpetas)
        self.sistema_carpetas()
        self.iniciar_sistema()
    #usar comandos
    def usarComandos(self, ent: str):
        for nombre, comando in self.command(ent).lista_comandos.items():
            if nombre in ent and comando.existe():
                return comando
        return None
    #buscar
    def encontrar_imagen(self):
        lista = []
        for f in self.lista_ficheros:
            if (f.getExtencion() == '.jpg') or (f.getExtencion() == '.jpeg'):
                lista.append(f)
        return lista
    def encontrar_musica(self):
        lista = []
        for f in self.lista_ficheros:
            if f.getExtencion() == '.mp3':
                lista.append(f)
        return lista
    def encontrar_videos(self):
        lista = []
        for f in self.lista_ficheros:
            if f.getExtencion() in '.mp4':
                lista.append(f)
        return lista
    def encontar_doc(self):
        lista = []
        for f in self.lista_ficheros:
            if f.getExtencion() == '.jpg' or f.getExtencion() == '.jpeg':
                pass
            elif f.getExtencion() == '.mp4':
                pass
            elif f.getExtencion() == '.mp3':
                pass
            else:
                lista.append(f)
        return lista
    #guardar ficheros
    def guarda_ficheros(self, ficheros: list[dict]):
        for fich in ficheros:
            archJson = json.dumps(fich)
            peso = sys.getsizeof(archJson)
            self.lista_ficheros.append(Fichero(fich['id'],fich['nombre'],fich['extencion'],peso,fich['datos']))
    #guardar carpetas
    def guarda_carpetas(self, carpetas: list[dict]):
        for carp in carpetas:
            c = Carpeta(carp['id'],carp['nombre'],carp['peso'])
            if carp['nombre'] == 'Imagenes':
                c.setFichero(self.encontrar_imagen())
            elif carp['nombre'] == 'Musica':
                c.setFichero(self.encontrar_musica())
            elif carp['nombre'] == 'Videos':
                c.setFichero(self.encontrar_videos())
            elif carp['nombre'] == 'Documentos':
                c.setFichero(self.encontar_doc())
            self.lista_carpetas.append(c)
    #conectar las carpetas al sistema
    def sistema_carpetas(self):
        for c in self.lista_carpetas: 
            self.sistema[0].getCarpetas().agregar(c)
    #navegar
    def iniciar_sistema(self):  
        while self.registro_busqueda:
            self.registro_busqueda = self.navegar(self.registro_busqueda)

    def navegar(self, busqueda: str):
        entrada = input(busqueda+'>>')
        accion = self.usarComandos(entrada)
        if accion:
            return accion.ejecutar(self.sistema, self.registro_busqueda)
        else:
            print('error de ejecucion...')
            return None
    #emular comandos

    #mostra
    def showComandos(self, ent: str):
        print('<comandos>')
        print('{0:8s}  {1:7s}'.format('nombre:','comando:'))
        for nombre, comando in self.command(ent).lista_comandos.items():
            print('{0:7s} | {1:7b} '.format(nombre,comando.existe()))
    def showCarpetas(self):
        print('<Archivo Carpetas1>')
        print('{0:2s}  {1:11s} {2:2s}'.format('id:','nombre:','peso:'))
        for p in self.lista_carpetas:
            print('{0:2d} | {1:10s} | {2:2d}'.format(p.getId(),p.getNombre(),p.getPesoTotal()))
    def showFicheros(self):
        print('<Archivo Archivos1>')
        print('{0:2s}  {1:11s} {2:11s} {3:7s} {4:8s}'.format('id:','nombre:','extencion:','peso:','datos'))
        for f in self.lista_ficheros:
            print('{0:2d} | {1:11s} | {2:7s} | {3:2d} | {4:18s}'.format(f.getId(),f.getNombre(),f.getExtencion(),f.getPeso(),f.getDatos()))