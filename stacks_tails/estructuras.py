from typing import Union, Optional, List
from .lista_folder_file import Pila
from datetime import datetime

class File:
    """Clase que representa un archivo"""
    
    def __init__(self, nombre: str, extension: str, contenido: str = "", tamanio: int = 0) -> None:
        self.nombre: str = nombre
        self.extension: str = extension
        self.contenido: str = contenido
        self.tamanio: int = tamanio if tamanio > 0 else len(contenido)
        self.fecha_creacion: datetime = datetime.now()
        self.fecha_modificacion: datetime = datetime.now()
    
    def get_nombre_completo(self) -> str:
        """Retorna el nombre completo con extensión"""
        return f"{self.nombre}.{self.extension}"
    
    def actualizar_modificacion(self) -> None:
        """Actualiza la fecha de modificación"""
        self.fecha_modificacion = datetime.now()
    
    def __str__(self) -> str:
        return f"{self.get_nombre_completo()} ({self.tamanio} bytes)"
    
    def __repr__(self) -> str:
        return f"File('{self.nombre}', '{self.extension}', {self.tamanio})"

class Folder:
    """Clase que representa una carpeta"""
    
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.contenido: Pila[Union['File', 'Folder']] = Pila()
        self.fecha_creacion: datetime = datetime.now()
        self.fecha_modificacion: datetime = datetime.now()
    
    def agregar_elemento(self, elemento: Union['File', 'Folder']) -> None:
        """Agrega un archivo o carpeta a esta carpeta"""
        self.contenido.apilar(elemento)
        self.actualizar_modificacion()
    
    def eliminar_elemento(self) -> Optional[Union['File', 'Folder']]:
        """Elimina el último elemento agregado (LIFO)"""
        if self.contenido.esta_vacia():
            return None
        
        elemento: Union[File, Folder] = self.contenido.desapilar()
        self.actualizar_modificacion()
        return elemento
    
    def listar_contenido(self) -> None:
        """Lista todo el contenido de la carpeta"""
        if self.contenido.esta_vacia():
            print(f"La carpeta '{self.nombre}' está vacía")
            return
        
        # Crear una pila temporal para no perder el orden original
        pila_temp: Pila[Union[File, Folder]] = Pila()
        elementos: List[str] = []
        
        # Transferir elementos a pila temporal y recolectar información
        while not self.contenido.esta_vacia():
            elemento: Union[File, Folder] = self.contenido.desapilar()
            pila_temp.apilar(elemento)
            
            if isinstance(elemento, File):
                elementos.append(f"📄 {elemento}")
            else:
                elementos.append(f"📁 {elemento.nombre}/")
        
        # Restaurar la pila original
        while not pila_temp.esta_vacia():
            self.contenido.apilar(pila_temp.desapilar())
        
        # Mostrar elementos en orden inverso (del más reciente al más antiguo)
        print(f"Contenido de '{self.nombre}/':")
        for i, elemento in enumerate(reversed(elementos), 1):
            print(f"  {i}. {elemento}")
    
    def buscar_elemento(self, nombre: str) -> Optional[Union['File', 'Folder']]:
        """Busca un elemento por nombre en la carpeta"""
        pila_temp: Pila[Union[File, Folder]] = Pila()
        encontrado: Optional[Union[File, Folder]] = None
        
        while not self.contenido.esta_vacia():
            elemento: Union[File, Folder] = self.contenido.desapilar()
            pila_temp.apilar(elemento)
            
            if isinstance(elemento, File):
                if elemento.nombre == nombre:
                    encontrado = elemento
            else:
                if elemento.nombre == nombre:
                    encontrado = elemento
        
        # Restaurar la pila original
        while not pila_temp.esta_vacia():
            self.contenido.apilar(pila_temp.desapilar())
        
        return encontrado
    
    def actualizar_modificacion(self) -> None:
        """Actualiza la fecha de modificación"""
        self.fecha_modificacion = datetime.now()
    
    def __str__(self) -> str:
        return f"{self.nombre}/"
    
    def __repr__(self) -> str:
        return f"Folder('{self.nombre}')"