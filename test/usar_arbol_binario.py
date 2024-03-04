from tools.elementos_terminal import Carpeta
from arboles.sistema_Carpetas import FolderSistem

#ejemplo 
fs = FolderSistem()
fs.insertar(Carpeta(1,'Carlos',15))
fs.insertar(Carpeta(2,'Maria',7))
fs.insertar(Carpeta(3,'Jose',45))
fs.insertar(Carpeta(4,'Latam',11))
n = 'pi'
r = bool
#inicio del programa
fs.in_orden(fs.raiz)
print()
r = fs.buscar_carpeta(n,fs.raiz)
print(f'La carpeta {n} es: {r}')