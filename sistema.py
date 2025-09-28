from typing import Optional, List, Union
from stacks_tails.estructuras import File, Folder
from stacks_tails.lista_folder_file import Pila

class SistemaArchivos:
    """Sistema principal de gestión de archivos y carpetas"""
    
    def __init__(self) -> None:
        self.raiz: Folder = Folder("raiz")
        self.directorio_actual: Folder = self.raiz
        self.historial: Pila[Folder] = Pila()
    
    def crear_archivo(self, nombre: str, extension: str, contenido: str = "") -> None:
        """Crea un nuevo archivo en el directorio actual"""
        archivo: File = File(nombre, extension, contenido, len(contenido))
        self.directorio_actual.agregar_elemento(archivo)
        print(f"Archivo '{archivo.get_nombre_completo()}' creado exitosamente")
    
    def crear_carpeta(self, nombre: str) -> None:
        """Crea una nueva carpeta en el directorio actual"""
        carpeta: Folder = Folder(nombre)
        self.directorio_actual.agregar_elemento(carpeta)
        print(f"Carpeta '{nombre}/' creada exitosamente")
    
    def listar(self) -> None:
        """Lista el contenido del directorio actual"""
        self.directorio_actual.listar_contenido()
    
    def cambiar_directorio(self, nombre_carpeta: str) -> None:
        """Cambia a una carpeta dentro del directorio actual"""
        if nombre_carpeta == "..":
            self.retroceder()
            return
        
        elemento: Optional[Union[File, Folder]] = self.directorio_actual.buscar_elemento(nombre_carpeta)
        
        if elemento and isinstance(elemento, Folder):
            self.historial.apilar(self.directorio_actual)
            self.directorio_actual = elemento
            print(f"Directorio cambiado a: {elemento.nombre}/")
        else:
            print(f"Error: Carpeta '{nombre_carpeta}' no encontrada")
    
    def retroceder(self) -> None:
        """Retrocede al directorio anterior"""
        if self.historial.esta_vacia():
            print("Ya estás en el directorio raíz")
            return
        
        self.directorio_actual = self.historial.desapilar()
        print(f"Directorio cambiado a: {self.directorio_actual.nombre}/")
    
    def eliminar_ultimo(self) -> None:
        """Elimina el último elemento agregado al directorio actual"""
        elemento: Optional[Union[File, Folder]] = self.directorio_actual.eliminar_elemento()
        if elemento:
            tipo: str = "archivo" if isinstance(elemento, File) else "carpeta"
            nombre: str = elemento.get_nombre_completo() if isinstance(elemento, File) else elemento.nombre
            print(f"{tipo.capitalize()} '{nombre}' eliminado exitosamente")
        else:
            print("No hay elementos para eliminar")
    
    def buscar(self, nombre: str) -> None:
        """Busca un elemento en el directorio actual"""
        elemento: Optional[Union[File, Folder]] = self.directorio_actual.buscar_elemento(nombre)
        if elemento:
            tipo: str = "Archivo" if isinstance(elemento, File) else "Carpeta"
            print(f"Elemento encontrado: {tipo} - {elemento}")
        else:
            print(f"Elemento '{nombre}' no encontrado")
    
    def mostrar_ruta_actual(self) -> None:
        """Muestra la ruta completa actual"""
        ruta: List[str] = [self.directorio_actual.nombre]
        temp_historial: Pila[Folder] = Pila()
        
        # Reconstruir la ruta desde el historial
        while not self.historial.esta_vacia():
            dir_temp: Folder = self.historial.desapilar()
            temp_historial.apilar(dir_temp)
            ruta.insert(0, dir_temp.nombre)
        
        # Restaurar el historial
        while not temp_historial.esta_vacia():
            self.historial.apilar(temp_historial.desapilar())
        
        print("Ruta actual: /" + "/".join(ruta))