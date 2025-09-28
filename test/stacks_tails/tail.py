from stacks_tails.tails import DriveDirectory, File

# generar Files
a1 = File("archivo1.txt","contenido del archivo 1")
a2 = File("archivo2.txt","contenido del archivo 2")
a3 = File("archivo3.txt","contenido del archivo 3")
a4 = File("archivo4.txt","contenido del archivo 4")
a5 = File("archivo5.txt","contenido del archivo 5")
a6 = File("archivo6.txt","contenido del archivo 6")

tails = DriveDirectory()

# agregar al la lista enlazada los valores
tails.add('',"Carpeta1")
tails.add('',"Carpeta2")
tails.add('',"Carpeta3")
tails.add('Carpeta1',a1)
tails.add('Carpeta2',a2)
tails.add('Carpeta2',a3)
tails.add('Carpeta3',a4)

tails.print_inorden()

print(f'<{'='*10} END CODE {'='*10}>')