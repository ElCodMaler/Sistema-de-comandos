from tools.generar.generar_sistema import carpetas, archivos, CrearSistema
#prueba los datos ingresados
print('<Los archivos antes de ingresarlos al sistema>')
print('  {0:0s}   {1:0s}  {2:10}'.format('id:','nombre:','peso:'))
for archJ in carpetas:
    for doc in archJ:
        print('{0:4d} | {1:10s} | {2:0d}'.format(doc[0],doc[1],doc[2]))
#creamos el sistema
sis = CrearSistema(archivos, carpetas)
print('<Los archivos son>')
for archJ in sis.lista_ficheros:
    for f in archJ:
        print(f.getNombre())
print('<La cantidad de archivos de carpetas es>')
print(sis.sistema_Carpetas)
print('<La cantidad de archivos de ficheros es>')
print(sis.lista_ficheros)


