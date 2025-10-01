import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Acceder a las variables
STRUCTURE = os.getenv('STRUCTURE')
UNITY = os.getenv('UNITY')

# init
sys = None

if STRUCTURE == 'tree':
    import tree_system
    sys = tree_system.CommandSystem()
elif STRUCTURE == 'linked' and not sys:
    import linked_list_system
    sys = linked_list_system.CommandSystem()
else:
    raise ValueError("no se puede continuar con el proyecto sin una estructura definida... " \
    "\n vaya al archivo .env")
# STARS COMMAND SYSTEM
sys.start()