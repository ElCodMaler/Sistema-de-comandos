from components.elementos_sistema import Unidad, Carpeta, Fichero
from tools.validaciones.validar_comandos import ValidarComando
from tools.TDA.pilas_colas.pilas import Pila
from tools.TDA.pilas_colas.colas import Cola
from components.usuario import User
import json
import sys

class CrearSistema:
    """
    + lista_ficheros: se almacenara una lista de objetos Fichero, donde tendra almacenado
    cada objeto para almacenarlo.
    """
    def __init__(self, archivos: list[dict], carpetas: list[list[dict]]):
        #variables
        self.lista_ficheros: list[Fichero] = []
        self.lista_carpetas: list[list[Carpeta]] = [[None for doc in arch] for arch in carpetas]
        self.sistema = [Unidad(1,"C:",700,700,Pila(),"SSD"),[User(),User(),User()]]
        self.command = ValidarComando
        #uso de metodos
        self.guarda_ficheros(archivos)
        self.guarda_carpetas(carpetas)
        self.sistema_carpetas()
        self.registro_busqueda = f'{self.sistema[0].getNombre()}'
        self.iniciar_sistema()
    #usar comandos
    def usarComandos(self, ent: str):
        for nombre, comando in self.command(ent).lista_comandos.items():
            if nombre in ent and comando.existe():
                print('el comando existe')
                return comando
        print('no existe el comando')
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
    def guarda_carpetas(self, carpetas: list[list[dict]]):
        for arch in range(len(carpetas)):
            for carp in range(len(carpetas[arch])):
                c = Carpeta(carpetas[arch][carp]['id'],carpetas[arch][carp]['nombre'],carpetas[arch][carp]['peso'])
                if carpetas[arch][carp]['nombre'] == 'Imagenes':
                    c.setFichero(self.encontrar_imagen())
                elif carpetas[arch][carp]['nombre'] == 'Musica':
                    c.setFichero(self.encontrar_musica())
                elif carpetas[arch][carp]['nombre'] == 'Videos':
                    c.setFichero(self.encontrar_videos())
                elif carpetas[arch][carp]['nombre'] == 'Documentos':
                    c.setFichero(self.encontar_doc())
                self.lista_carpetas[arch][carp] = c
    #conectar las carpetas al sistema
    def sistema_carpetas(self):
        i = 0
        for c1 in self.lista_carpetas[1]:
            if c1.getNombre() == 'Users':
                c1.setCarpetas(Cola())
                for c2 in self.lista_carpetas[2]:
                    #asignar usuarios
                    self.sistema[1][i].setName(c2.getNombre())
                    self.sistema[1][i].setAcceso(False)
                    if c2.getNombre() == 'Jose':
                        self.sistema[1][i].setAcceso(True)
                        c2.setCarpetas(Cola())
                        for c3 in self.lista_carpetas[0]:
                            #asignar subcarpetas
                            c2.getCarpetas().agregar(c3)
                    i = i + 1
                    #asignar subCarpetas
                    c1.getCarpetas().agregar(c2)
            #asignar carpetas principales del disco local C:
            self.sistema[0].getCarpetas().agregar(c1)

    #navegar
    def iniciar_sistema(self):  
        while self.registro_busqueda:
            self.registro_busqueda = self.navegar(self.registro_busqueda)
            print(self.registro_busqueda)

    def navegar(self, busqueda: str):
        entrada = input(busqueda+'>>')
        accion = self.usarComandos(entrada)
        if accion:
            return accion.ejecutar(self.sistema[0], self.registro_busqueda)
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
        i = 1
        for arch in self.lista_carpetas:
            print(f'<Archivo Carpetas{i}>')
            print('{0:2s}  {1:11s} {2:2s}'.format('id:','nombre:','peso:'))
            for c in arch:
                print('{0:2d} | {1:10s} | {2:2d}'.format(c.getId(),c.getNombre(),c.getPesoTotal()))
            i = i + 1
    def showFicheros(self):
        print('<Archivo Archivos1>')
        print('{0:2s}  {1:11s} {2:11s} {3:7s} {4:8s}'.format('id:','nombre:','extencion:','peso:','datos'))
        for f in self.lista_ficheros:
            print('{0:2d} | {1:11s} | {2:7s} | {3:2d} | {4:18s}'.format(f.getId(),f.getNombre(),f.getExtencion(),f.getPeso(),f.getDatos()))