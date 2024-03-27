from .lista import Lista_Comandos

#clase CD
class Cd:
    """
    + instrucciones: donde se almacenara los datos de entrada del usuario.
    + listaC: donde se tendra instanciado la clase Lista_Comandos, que tiene toda la informacion de los comandos.
    + comando: donde se almacenara el objeto Comando correspondiente de este comando.
    + profundidad: donde se guardara el nivel de profundidad de las lista enlazadas.
    """
    def __init__(self, instrucciones: list):
        self.instrucciones = instrucciones
        self.listaC = Lista_Comandos()
        self.comando = None
        self.profundidad = 0
    #metodo de validacion del comando
    def existe(self):
        entrada = self.instrucciones.split(' ')
        if len(entrada) != 2:
            print('Excede la cantidad de datos')
            return False
        for comando in self.listaC.comandos:
            if comando.getId() == 1:
                requicitos = comando.getRequicito()
                if requicitos[0] == entrada[0] and entrada[1]:
                    comando.setRequicito([requicitos[0],entrada[1]])
                    self.comando = comando
                    return True
        return False
    #metodo donde se ejecutara el comando
    def ejecutar(self, sistema, ubicacion_actual: str):
        folder = 'C:'
        carpetas = sistema.getCarpetas()
        ubicacion = ubicacion_actual.split('/')
        self.profundidad = len(ubicacion)
        #funcion ir al directorio anterior
        if self.comando.getRequicito()[1] == "..":
            for directorio in ubicacion:
                if ubicacion[-1] == directorio:
                    break
                if ubicacion[0] == directorio:
                    continue
                folder = folder +'/'+ directorio
            return folder
        #funcion ir al disco local
        elif self.comando.getRequicito()[1] == "/":
            return folder
        #recorrer directorios
        else:
            encontrar = self.buscar(carpetas, self.comando.getRequicito()[1])
            #si la profundidad se redujo con respecto a la cantidad de iteraciones del evento recursivo
            #entonces esta donde debe estar
            if encontrar and self.profundidad == 0:
                return ubicacion_actual +'/'+ encontrar
            else:
                print('no existe ese directorio')
                return ubicacion_actual
    #nueva funcion
    def buscar(self, system, entrada):
        #evaluar si la carpeta actual tiene valores en su lista enlazada de Colas
        if not system.esta_vacia():
            self.profundidad -= 1 #se restara 1 a cada iteracion del evento recursivo de esta funcion
            carpetas = system.obtener_objetos()
            subCarpeta = []
            #encontrar la carpeta buscada
            for c in carpetas:
                if c.getNombre() == entrada:
                    return entrada
                elif type(c.getFicheros()) == list and len(c.getFicheros()) > 0:
                    for fich in c.getFicheros():
                        if fich.getNombre() == entrada:
                            return fich.getNombre() + fich.getExtencion()
            #crear una lista de objetos Cola de esta carpeta
            #asi podemos asegurar cual de las siguientes carpetas esta llena y cual no
            for c1 in carpetas:
                if c1.getCarpetas():
                    subCarpeta.append(c1.getCarpetas())
            #si la lista de subcarpetas esta llena entonces la recorremos
            if len(subCarpeta) > 0:
                for subC in subCarpeta:
                    #asegurase de que la lista este llena y no sea solo el objeto vacio
                    if not subC.esta_vacia():
                        return self.buscar(subC, entrada)
            else:
                return None
        else:
            return None