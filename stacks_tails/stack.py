from .node.directory_node import NodeD
from templates.file import File
from templates.folder import Folder

class Driver:
    """
    + end: the last node of the linked list
    """
    def __init__(self):
        self._end: NodeD | None =None

    def add(self, valor: str):
        nodo_nuevo = NodeD(valor)
        nodo_nuevo.next = self._end
        self._end = nodo_nuevo

    def addContent(self, father:str, Child: File | Folder):
        if not self._end:
            print('no se puede realizar esta operacion. El Drive esta vacio')
            return
        self._pivot_search_dad(self._end, father,Child)

    def _pivot_search_dad(self, node: NodeD, search_name: str, value: File | Folder):
        if not NodeD:
            return
        if node.name == search_name:
            node.content.add(value)


    def getEnd(self):
        return self._end

    def print_inorden(self):
        self._route_node_list(self._end)
    # pivot print in-orden
    def _route_node_list(self, node: NodeD | None):
        if not node:
            return
        print(node.name)
        node.content.print_inorden()
        self._route_node_list(node.next)