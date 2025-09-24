#clases extenciones de errores
class CommandError(Exception):
    pass

class ValidacionCommand:
    def __init__(self, name: str):
        cm = name.split(' ')
        la = ['asc','cd','desc','dir','exit','help']
        lb = ['mkdir','rmdir']

        if len(cm) == 1:
            for c in la:
                if c in cm:
                    return cm
        elif len(cm) == 2:
            for c in lb:
                if c in cm:
                    return cm
        return None
            