#clases extenciones de errores
class ExtencionError(Exception):
    pass

class ValidacionExtencion:
    def __init__(self, ext: str):
        allowed_extensions = {'txt', 'doc', 'docx', 'pdf', 'jpg', 'png', 'exe', 'mp3', 'mp4', 'avi', 'zip', 'rar', 'csv', 'xlsx', 'pptx'}
        if ext not in allowed_extensions:
            print(f"La extencion '{ext}' no es permitida. Extenciones permitidas: {', '.join(allowed_extensions)}")
        self.ext = ext
#fin