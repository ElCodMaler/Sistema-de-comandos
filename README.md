# Sistema de Comandos
Emula un sistema de comandos de un sistema operativo, donde solo
se puede recorrer los ficheros por medio de la terminal...

El objetivo de este programa es de terminos academicos, donde
se pone a prueba la estructura de nodos de arboles, pilas y colas.

## Instalacion

Para que el programa corra se necesita instalar la libreria de **python-dotenv**

```bash
  pip install python-dotenv    
```

## Environment Variables
Otro requisito es ubicarse en la carpeta **.env** y asignar el valor que indicara el tipo de estructura los valores que recibe son: 'PC' or 'Arb'

`STRUCTURE`

## Flujo del programa
En la carpeta **app** estan las funciones de uso en el flujo del programa.

- Los **TDA** que tienen la estructura de nodos.
- en la capta **generar** se crea el sistema usando la estructura seleccionada.
- La carpeta **construir** contiene todos los usos generales del sistema de comandos.

En la carpeta **tools** estan las funciones necesarias para el funcionamiento del programa.

- la carpera **validaciones** donde se usan funciones que se aseguren que el funcionamiento de los comandos este bien implementada.
- La carpeta **guardar** que tiene dos funciones que separan las carpetas de los archivos.
- La carpeta **comandos** donde se les implementa su respectiva funcion a cada comando, asi como su nombre.

En la Carpeta **components** tenemos las plantillas principales de cada objeto, unidades de almacenamiento, carpetas, archivos, incluso comandos.

### DataBase 📁
La base de datos se almacena en un archivo llamado "datos.json", que contiene datos aleatorios de particiones de almacenamiento, archivos y ficheros.