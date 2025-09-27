from .node.node_folder_file import FolderN, Folder, File

# Tails, linked list of Folders and Files
class DriveDirectory:
    """
    + head: root of the linked list that will have the first Node
    + tail: last node of the linked list
    """
    def __init__(self):
        self._head: FolderN | None=None
        self._tail: FolderN
    
    # ====================== UTILITIES ======================
    
    def add(self, valor: Folder | File):
        new_node = FolderN(valor)
        if not self._head:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
    
    def get(self, name: str):
        """ get the searched value """
        if not self._head:
            print("❌ empty queue.")
            return None
        
        # Caso 1: El valor está en el frente
        if self._head.value.getName() == name:
            print(f"✅ found value.")
            return self._head.value
        
        # Caso 2: Buscar el valor en medio o final
        current = self._head.next
        
        while current:
            if current.value.getName() == name:
                # Encontrado, eliminar
                print(f"✅ found value.")
                return current.value
            current = current.next
        
        print(f"❌ value '{name}' not found.")
        return None

    def delete(self, name: str):
        """ remove value """
        if not self._head:
            print("❌ empty queue.")
            return False
        
        # Caso 1: El valor está en el frente
        if self._head.value.getName() == name:
            self._empty_queue()
            return True
        
        # Caso 2: Buscar el valor en medio o final
        previus = self._head
        current = self._head.next
        
        while current:
            if current.value.getName() == name:
                # Encontrado, eliminar
                previus.next = current.next
                
                # Si era el último nodo, actualizar final
                if current == self._tail:
                    self._tail = previus
                print(f"✅ removed: {name}")
                return True
            
            previus = current
            current = current.next
        
        print(f"❌ value '{name}' not found.")
        return False
    # pivot delete
    def _empty_queue(self):
        if not self._head:
            return None
        
        data = self._head.value
        self._head = self._head.next
        return data
    
    # ================== PRITIE IMPRESION =================
    def print_inorden(self):
        self._route_node_list(self._head)
    # pivot to impresion
    def _route_node_list(self, node: FolderN | None):
        if not node:
            return
        node.value.info()
        self._route_node_list(node.next)