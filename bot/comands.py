from services.git_service import obtener_contenido_archivo
from services.openai_service import sugerir_mejoras
from utils.logger import setup_logger

logger = setup_logger()

def mejora_codigo(archivo):
    logger.info(f"📂 Analizando archivo: {archivo}")
    contenido = obtener_contenido_archivo(archivo)
    sugerencia = sugerir_mejoras(contenido)
    logger.info(f"💡 Sugerencia de mejora:\n{sugerencia}")
    return sugerencia
