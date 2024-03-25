from tools.generar.generar_pilas_colas import carpetas, ficheros, CrearSistema
#agregado de prueba
def buscar(system, entrada):
    if not system.esta_vacia():
        carpetas = system.obtener_objetos()
        subCarpeta = []
        for c in carpetas:
            if c.getNombre() == entrada:
                if not(c.getCarpetas()) and c.getFicheros():
                    for fich in c.getFicheros():
                        print(fich.getNombre())
                    return True
        for c1 in carpetas:
            if c1.getCarpetas():
                subCarpeta.append(c1.getCarpetas())
        return buscar(subCarpeta[0], entrada)
    else:
        return False
#creamos el sistema y sus funciones
sis = CrearSistema(ficheros, carpetas)
carpetas = sis.sistema[0].getCarpetas()
entrada = input('C:/Users/Jose/Imagenes>')
if buscar(carpetas,entrada):
    print('se encontro la carpeta')
else:
    print('no se encontro la carpeta')