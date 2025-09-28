from sistema import SistemaArchivos

def mostrar_menu() -> None:
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print("SISTEMA DE ARCHIVOS CON PILAS")
    print("="*50)

def obtener_opcion() -> str:
    """Obtiene y retorna la opción del usuario"""
    return input("\nSeleccione una opción: ").strip()

def main() -> None:
    sistema: SistemaArchivos = SistemaArchivos()
    
    while True:
        sistema.mostrar_ruta_actual()
        mostrar_menu()
        print("\nOpciones:")
        print("1. Crear archivo")
        print("2. Crear carpeta")
        print("3. Listar contenido")
        print("4. Cambiar directorio")
        print("5. Retroceder directorio")
        print("6. Eliminar último elemento")
        print("7. Buscar elemento")
        print("8. Salir")
        
        opcion: str = obtener_opcion()
        
        if opcion == "1":
            nombre: str = input("Nombre del archivo: ").strip()
            extension: str = input("Extensión: ").strip()
            contenido: str = input("Contenido: ").strip()
            sistema.crear_archivo(nombre, extension, contenido)
        
        elif opcion == "2":
            nombre: str = input("Nombre de la carpeta: ").strip()
            sistema.crear_carpeta(nombre)
        
        elif opcion == "3":
            sistema.listar()
        
        elif opcion == "4":
            nombre: str = input("Nombre de la carpeta (o '..' para retroceder): ").strip()
            sistema.cambiar_directorio(nombre)
        
        elif opcion == "5":
            sistema.retroceder()
        
        elif opcion == "6":
            sistema.eliminar_ultimo()
        
        elif opcion == "7":
            nombre: str = input("Nombre a buscar: ").strip()
            sistema.buscar(nombre)
        
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

main()