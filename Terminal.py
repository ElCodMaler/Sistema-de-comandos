from elementos_terminal import Fichero, Carpeta, Unidad
from Comandos import Comando
#clase
class Consola(Fichero, Carpeta, Unidad, Comando):
    def crearCarpeta(self):
        self.carpetas = []
        self.carpetas.append(Fichero(1,'foto sonriendo','.jpg',2500,''))
        self.carpetas.append(Fichero(2,'video de la playa','.mp4',23865,''))
        self.carpetas.append(Fichero(3,'notas de la universidad','.txt',958,'Estructuras del cuerpo y la ciencia que explica su contenido'))
        self.carpetas.append(Fichero(4,'estadisticas de la tasa de valores','.exe',1200,'22% de ganancias en el mercado negro'))
        self.carpetas.append(Fichero(5,'foto de mi gato','.jpg',1200,''))
        self.carpetas.append(Fichero(6,'video de un baile','.mp4',5300,''))
    def crearUnidad(self,)
 


        