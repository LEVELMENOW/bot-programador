from bot.commands import mejora_codigo

def handle_command(command):
    if command.startswith("mejora"):
        archivo = command.split(" ")[1]
        return mejora_codigo(archivo)
    else:
        return "⚠️ Comando no reconocido."
