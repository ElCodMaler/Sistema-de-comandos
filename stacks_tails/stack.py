from .node.directory_node import NodeSF, File, FolderN

class DriverSubfolder:
    """
    + end: the last node of the linked list
    """
    def __init__(self):
        self._end: NodeSF | None =None

    def add(self, valor: File | FolderN):
        nodo_nuevo = NodeSF(valor)
        nodo_nuevo.next = self._end
        self._end = nodo_nuevo

    def get(self, name:str) -> File | FolderN | None:
        return self._search_pivot(self._end,name)
    # pivot de busqueda de nodos
    def _search_pivot(self, node:NodeSF | None, name:str):
        if not node:
            return
        if isinstance(node,FolderN):
            children = node.content
            res = children.get(name)
            if res:
                return res
        if node.value.getName() == name:
            return node.value
        self._search_pivot(node.next, name)

    def addContent(self, father:str, Child: File | FolderN):
        if not self._end:
            print('no se puede realizar esta operacion. El Drive esta vacio')
            return
        self._pivot_search_dad(self._end, father,Child)

    def _pivot_search_dad(self, node: NodeSF | None, search_name: str, value: File | FolderN):
        if not node:
            return
        if node.value.getName() == search_name:
            if isinstance(node.value,FolderN):
                node.value.content.add(value)
            else:
                self.add(value)
        self._pivot_search_dad(node.next,search_name,value)

    def getEnd(self):
        return self._end

    def print_inorden(self):
        self._route_node_list(self._end)
    # pivot print in-orden
    def _route_node_list(self, node: NodeSF | None):
        if not node:
            return
        node.value.info
        self._route_node_list(node.next)