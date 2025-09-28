#importar carpetas de pruba de la clase Folder
from ..data.folders import c1, c2, c3, c4
#importar subfolder de prueba de la clase Folder
from ..data.folders import sa, sb, sc, sd
#importar archivos de prueba de la clase File
from ..data.files import a1, a2, a3

#asignar valor a las respectivas carpetas
c1.content.add(sa)
c1.content.add(sb)
c1.content.add(a1)

c1.content.print_inorden()

c1.content.add('SubfolderA',a2)

res = c1.content.get('SubfolderA')
res.value.content.print_inorden()