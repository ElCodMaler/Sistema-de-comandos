from templates.command import SistemaComandos
from typing import List, Any
from datetime import datetime

class SistemaArchivosComandos(SistemaComandos):
    def __init__(self) -> None:
        super().__init__()
        self.archivos: List[str] = []
        self.carpetas: List[str] = ["/home", "/var", "/tmp"]
        self.directorio_actual: str = "/"
        self.historial: List[str] = []
    
    # COMANDOS - Sin anotaciones de tipo problemáticas
    @SistemaComandos.comando("crear", r"crear\s+archivo\s+(.+)")
    def crear_archivo(self, nombre_archivo: str) -> None:
        """Crea un nuevo archivo"""
        self.archivos.append(nombre_archivo)
        print(f"📄 Archivo '{nombre_archivo}' creado en {self.directorio_actual}")
        self._agregar_al_historial(f"crear archivo {nombre_archivo}")
    
    @SistemaComandos.comando("listar", r"listar\s*(\w+)?")
    def listar_elementos(self, tipo: str = "todos") -> None:
        """Lista archivos y/o carpetas"""
        if not tipo or tipo == "todos" or tipo == "archivos":
            if self.archivos:
                print("📂 Archivos:")
                for archivo in self.archivos:
                    print(f"  - {archivo}")
            else:
                print("📂 No hay archivos")
        
        if not tipo or tipo == "todos" or tipo == "carpetas":
            if self.carpetas:
                print("📁 Carpetas:")
                for carpeta in self.carpetas:
                    print(f"  - {carpeta}/")
            else:
                print("📁 No hay carpetas")
    
    @SistemaComandos.comando("eliminar", r"eliminar\s+archivo\s+(.+)")
    def eliminar_archivo(self, nombre_archivo: str) -> None:
        """Elimina un archivo"""
        if nombre_archivo in self.archivos:
            self.archivos.remove(nombre_archivo)
            print(f"🗑️ Archivo '{nombre_archivo}' eliminado")
            self._agregar_al_historial(f"eliminar archivo {nombre_archivo}")
        else:
            print(f"❌ Archivo '{nombre_archivo}' no encontrado")
    
    @SistemaComandos.comando("cd", r"cd\s+(.+)")
    def cambiar_directorio(self, nueva_carpeta: str) -> None:
        """Cambia el directorio actual"""
        if nueva_carpeta in self.carpetas or nueva_carpeta == "/":
            self.directorio_actual = nueva_carpeta
            print(f"📁 Directorio cambiado a: {nueva_carpeta}")
            self._agregar_al_historial(f"cd {nueva_carpeta}")
        else:
            print(f"❌ Carpeta '{nueva_carpeta}' no encontrada")
    
    @SistemaComandos.comando("pwd")
    def mostrar_directorio_actual(self) -> None:
        """Muestra el directorio actual"""
        print(f"📁 Directorio actual: {self.directorio_actual}")
    
    @SistemaComandos.comando("mkdir", r"mkdir\s+(.+)")
    def crear_carpeta(self, nombre_carpeta: str) -> None:
        """Crea una nueva carpeta"""
        self.carpetas.append(nombre_carpeta)
        print(f"📁 Carpeta '{nombre_carpeta}' creada")
        self._agregar_al_historial(f"mkdir {nombre_carpeta}")
    
    @SistemaComandos.comando("ayuda")
    def mostrar_ayuda(self) -> None:
        """Muestra ayuda de comandos"""
        print("🤖 Comandos disponibles:")
        comandos = [
            ("crear archivo <nombre>", "Crea un archivo"),
            ("listar [tipo]", "Lista elementos (archivos/carpetas/todos)"),
            ("eliminar archivo <nombre>", "Elimina un archivo"),
            ("cd <carpeta>", "Cambia de directorio"),
            ("pwd", "Muestra directorio actual"),
            ("mkdir <carpeta>", "Crea una carpeta"),
            ("ayuda", "Muestra esta ayuda"),
            ("salir", "Termina el programa")
        ]
        
        for comando, desc in comandos:
            print(f"  {comando:25} - {desc}")
    
    # Método interno
    def _agregar_al_historial(self, comando: str) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.historial.append(f"[{timestamp}] {comando}")