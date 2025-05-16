import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

#ejecucion del sistema de comandos
if os.environ.get("STRUCTURE") == 'PC':
    from app.generar.generar_pilas_colas import sis
elif os.environ.get("STRUCTURE") == 'Arb':
    from app.generar.generar_sistema import sis
else:
    from app.generar.generar_pilas_colas import sis

sis.iniciar_sistema()
