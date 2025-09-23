class ErrorAtributo(Exception):
    pass
class ValoresAtributosWarningError(Exception):
    pass

#clase ValoresAtributos
class ValidacionAtributos:
    def __init__(self, name: str):
        if not name:
            raise ErrorAtributo("El nombre no puede estar vacio")
        elif len(name) > 255:
            raise ValoresAtributosWarningError("El nombre no puede tener mas de 255 caracteres")
        elif any(char in name for char in r'\/:*?"<>|'):
            raise ValoresAtributosWarningError("El nombre no puede contener los siguientes caracteres: \\ / : * ? \" < > |")
        elif name.strip() == "":
            raise ValoresAtributosWarningError("El nombre no puede estar compuesto solo por espacios en blanco")
        self.name = name
#fin


