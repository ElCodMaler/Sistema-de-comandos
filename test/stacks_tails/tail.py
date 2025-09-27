from stacks_tails.tails import DriveDirectory, File, Folder

# generar Carpetas
c1 = Folder('Carpeta1')
c2 = Folder('Carpeta2')
c3 = Folder('Carpeta3')
# generar Files
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
a3 = File("archivo3.txt","contenido del archivo 3")
a4 = File("archivo4.txt","contenido del archivo 4")
a5 = File("archivo5.txt","contenido del archivo 5")
a6 = File("archivo6.txt","contenido del archivo 6")

tails = DriveDirectory()

# agregar al la lista enlazada los valores
tails.add(c1)
tails.add(c2)
tails.add(c3)
tails.add(a1)
tails.add(a2)
tails.add(a3)
tails.add(a4)

#salida de resultados 
tails.print_inorden()

#eliminar
res = tails.delete("archivo3.txt")
if not res:
    print('mal')
else:
    tails.print_inorden()

# encontrar dato
res = tails.get("Carpeta3")

if not res:
    print('mal')
else:
    print("El valor buscado es ",res.getName())
    res.info()