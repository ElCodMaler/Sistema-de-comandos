class ValidacionCommand:
    def __init__(self, name: str):
        self.command:str | None = None
        self.entry: str | list[str] | None = None
        cm = name.split(' ')
        l1 = ['asc','ls','desc','dir','exit','help']
        l2 = ['mkdir','rmdir','cd']
        # evaluamos los comandos que requieren un solo campo
        for key in l1:
            if len(cm) == 1 and key in cm:
                self.command = key
        # evaluamos el que requiere uno o mas campos
        for key in l2:
            if len(cm) == 2 and cm[0] == 'cd':
                self.command= cm[0]
                self.entry= cm[1]
            elif len(cm) >= 2 and key in cm:
                cm.pop(0)
                self.command= key
                if len(cm) == 1:
                    self.entry = cm[0]
                else:
                    self.entry = cm
        if not self.command:
            print("Comando no reconocido")