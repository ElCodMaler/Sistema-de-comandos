from stacks_tails.sistema import SistemaArchivos

system = SistemaArchivos()

system.createFolder("Carpeta1")
system.createFile('archivo1.txt')
system.show_current_route()
system.print_list()
