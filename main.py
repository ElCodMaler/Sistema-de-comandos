import os
from dotenv import load_dotenv
from system import CommandSystem

# Cargar variables del archivo .env
load_dotenv()
# Acceder a las variables
UNITY = os.getenv('UNITY')
STORAGE = os.getenv('STORAGE')
# asignar la unidad disponible con su peso asignado
if UNITY and STORAGE:
    sys = CommandSystem(UNITY,int(STORAGE))
else:
    sys = CommandSystem()
# INICIO DEL PROGRAMA
sys.start()