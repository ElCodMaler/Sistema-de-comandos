from tools.generar.generar_pilas_colas import carpetas, ficheros, CrearSistema

def buscar(system, entrada):
    if not system.esta_vacia():
        carpetas = system.obtener_objetos()
        subCarpeta = []
        for c in carpetas:
            if c.getNombre() == entrada:
                return entrada
            elif c.getFicheros():
                for fich in c.getFicheros():
                    if fich.getNombre() == entrada:
                        return entrada
        for c1 in carpetas:
            if c1.getCarpetas():
                subCarpeta.append(c1.getCarpetas())
        if len(subCarpeta) > 0:
            return buscar(subCarpeta[0], entrada)
    else:
        return ''

#creamos el sistema y sus funciones
sis = CrearSistema(ficheros, carpetas)

carpetas = sis.sistema[0].getCarpetas()
entrada = input('C:/Users/Jose/Imagenes>')
res = buscar(carpetas,entrada)
if len(res) > 0:
    print(res)