import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Acceder a las variables
STRUCTURE = os.getenv('STRUCTURE')

if STRUCTURE == 'tree':
    from .folder_nary import Folder
elif STRUCTURE == 'linked':
    from .folder_tail import Folder
else:
    raise ValueError("no se puede continuar con el proyecto sin una estructura definida... " \
    "\n vaya al archivo .env")

__all__=['Folder']