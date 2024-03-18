from tools.validaciones.validar_comandos import ValidarComando
#Inicializacion de variables
res = bool
entrada = str
validarC = ValidarComando
def usarComandos(ent: str) -> bool:
    for nombre, comando in validarC.lista_comandos.items():
        if nombre in ent:
            return comando.existe()
    return False
#INICIO DEL PROGRAMA
#entrada de datos
while True:
    entrada = input('Escribir el comando>')
    validarC = ValidarComando(entrada)
    if usarComandos(entrada):
        print('se ejecuta la accion...')
        break
    else:
        print('no se encuentra el coamndo, escriba denuevo')