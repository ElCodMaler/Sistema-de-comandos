#clases extenciones de errores
class ExtencionError(Exception):
    pass

class ValidacionExtencion:
    def __init__(self, name: str):
        ls = name.split('.')
        ext = name
        if len(ls) == 2:
            ext = ls[1]
        if len(ls) > 2:
            raise ExtencionError('La extencion debe tener solo un (.) que lo separe de la extencion')
        allowed_extensions = {'txt', 'doc', 'docx', 'pdf', 'jpg', 'png', 'exe', 'mp3', 'mp4', 'avi', 'zip', 'rar', 'csv', 'xlsx', 'pptx'}
        if ext not in allowed_extensions:
            raise ExtencionError(f"La extencion '{ext}' no es permitida. Extenciones permitidas: {', '.join(allowed_extensions)}")
        self.ext = ext
#fin