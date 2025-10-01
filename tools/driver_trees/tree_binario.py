from .drive_folder import FolderN, File
from templates.nodes.node_binario import NodeB
from typing import Union

# binary tree
class Organizer:
    """ + root: first binary node """
    def __init__(self, directory: FolderN):
        self.root: NodeB[FolderN | File] = NodeB(directory)
        self._entry_tree()

    # ==================== UTILITIS ====================

    def height(self) -> int:
        """ height of the binary tree """
        if not self.root:
            raise ValueError("the tree Binary do not want void")
        return self._calculate_height(self.root)

    def number_nodes(self) -> int:
        """ the number of nodes in the binary tree (Organizer) """
        if not self.root:
            raise ValueError("the tree is empty")
        return self._node_counter(self.root)

    def add(self, value: FolderN | File):
        """ add a file or folder to the binary tree """
        return self._insert_by_priorities(value)
    
    # ===================== PROTECTED FUNCTIONS ======================

    def _entry_tree(self):
        """ insert the entire contents of the folder into the binary tree """
        children = self.root.value.children if not isinstance(self.root.value, File) else None
        if not children:
            print("There is no content in this folder.")
            return
        for directory in children:
            self.add(directory)
    
    def _insert_by_priorities(self, value: FolderN | File) -> bool:
        """ insert keeping the order of priorities: weight → length → alphabetical """
        if not self.root:
            self.root = NodeB(value)
            return True
        actual = self.root
        nuevo_nodo = NodeB(value)
        while True:
            comparacion = self._compare_entrys(value, actual.value)
            if comparacion < 0:  # folder tiene mayor prioridad
                if not actual.left:
                    actual.left = nuevo_nodo
                    return True
                actual = actual.left
            else:  # folder tiene menor o igual prioridad
                if not actual.right:
                    actual.right = nuevo_nodo
                    return True
                actual = actual.right
            
    def _compare_entrys(self, item1: FolderN | File, item2: FolderN | File) -> int:
        """
        Compares two values(Folder/File) based on the following priority system:
        1. Weight (largest first)
        2. Name length (longest first)
        3. Alphabetical/numeric order character by character

        Returns: -1 (item1 first), 0 (equal), 1 (item2 first)
        """
        # Priority 1: weight (heaviest weight first)
        if item1.getWeight() != item2.getWeight():
            return -1 if item1.getWeight() > item2.getWeight() else 1
        # Priority 2: Name length (longest first)
        if len(item1.getName()) != len(item2.getName()):
            return -1 if len(item1.getName()) > len(item2.getName()) else 1
        # Priority 3: Alphabetical/numeric order character by character
        for char1, char2 in zip(item1.getName(), item2.getName()):
            if char1 != char2:
                # Handling digits vs. letters
                if char1.isdigit() and char2.isdigit():
                    return -1 if int(char1) > int(char2) else 1
                elif char1.isdigit():
                    return -1  # Digits take priority over letters.
                elif char2.isdigit():
                    return 1 
                else:
                    return -1 if char1 > char2 else 1
        return 0  # They are equal in all priorities
        
    def _node_counter(self, nodo: NodeB[FolderN | File] | None) -> int:
        """ count all nodes to binary tree """
        if not nodo:
            return 0
        return 1 + self._node_counter(nodo.left) + self._node_counter(nodo.right)
    
    def _calculate_height(self, nodo: NodeB[FolderN | File] | None) -> int:
        """ search height """
        if not nodo:
            return 0
        return 1 + max(self._calculate_height(nodo.left), 
                      self._calculate_height(nodo.right))
        
    # ==================== ROUND ====================
    
    def inorder(self):
        """ in-order traversal: left → root → right """
        if not self.root:
            raise ValueError("the tree is empty")
        return self._inorder_recursive(self.root)
    # in-order recursive pivot
    def _inorder_recursive(self, nodo: NodeB[FolderN | File] | None) -> list[Union[FolderN,File]]:
        if not nodo:
            return []
        return (self._inorder_recursive(nodo.left) + 
                    [nodo.value] + 
                    self._inorder_recursive(nodo.right))
    
    def preorder(self):
        """ pre-order traversal: root → left → right """
        if not self.root:
            raise ValueError("the tree is empty")
        return self._preorder_recursive(self.root)
    # pre-order recursive pivot
    def _preorder_recursive(self, nodo: NodeB[FolderN | File] | None) -> list[Union[FolderN,File]]:
        if not nodo:
            return []
        return ([nodo.value] + 
                    self._preorder_recursive(nodo.left) + 
                    self._preorder_recursive(nodo.right))
    
    def postorden(self) -> list[Union[FolderN,File]]:
        """ post-order traversal: left → right → root """
        if not self.root:
            raise ValueError("the tree is empty")
        return self._postorder_recursive(self.root)
    # post-order recursive pivot
    def _postorder_recursive(self, nodo: NodeB[FolderN | File] | None) -> list[Union[FolderN,File]]:
        if not nodo:
            return []
        return (self._postorder_recursive(nodo.left) + 
                    self._postorder_recursive(nodo.right) + 
                    [nodo.value])
    
    # ==================== PRITING NICE ====================
    
    def print_info_inorder(self) -> None:
        """ print in-order of detailed information """
        directorys = self.inorder()
        for directory in directorys:
            if directory.getName() == self.root.value.getName():
                continue
            directory.info()
    
    def print_info_preorder(self) -> None:
        """ print pre-order of detailed information """
        directorys = self.preorder()
        for directory in directorys:
            if directory.getName() == self.root.value.getName():
                continue
            directory.info()
    
    def print_info_postorder(self) -> None:
        """ print post-order of detailed information """
        directorys = self.postorden()
        for directory in directorys:
            if directory.getName() == self.root.value.getName():
                continue
            directory.info()

    def print_list(self) -> None:
        """ print list from left to right """
        directorys = self.inorder()
        for directory in directorys:
            if directory.getName() == self.root.value.getName():
                continue
            print(directory.getName(),end=' ')
        print()