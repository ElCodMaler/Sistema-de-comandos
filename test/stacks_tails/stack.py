from stacks_tails.stack import Driver, File, Folder

# sub folder
sa = Folder("subfolderA")
sb = Folder("subfolderB")
sc = Folder("subfolderC")
sd = Folder("subfolderD")
se = Folder("subfolderE")
sf = Folder("subfolderF")
sg = Folder("subfolderG")
# archivos
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
a3 = File("archivo3.txt","contenido del archivo 3")
a4 = File("archivo4.txt","contenido del archivo 4")
a5 = File("archivo5.txt","contenido del archivo 5")
a6 = File("archivo6.txt","contenido del archivo 6")
# generar sistema de carpetas
system = Driver()

# generar carpetas 
system.add("Carpeta1")
system.add("Carpeta2")
system.add('Carpeta3')
system.add("Carpeta4")
# asignars carpetas o archivos a las carpetas
system.addContent("Carpeta1",sa)
system.addContent("Carpeta1",sb)
system.addContent("Carpeta1",sc)
system.addContent("Carpeta1",a1)
system.addContent("Carpeta1",a2)

system.addContent("Carpeta2",sf)
system.addContent("Carpeta2",se)
system.addContent("Carpeta2",a4)
system.addContent("Carpeta2",a3)

system.addContent("Carpeta3",a5)
system.addContent("Carpeta3",a6)

system.addContent("Carpeta4",sg)

#impresion de resultados
system.print_inorden()

# get value
res = system.get("subfolderA")
if res:
    res.info()
else:
    print("no se encontro el folder.")
