from flask import Flask, request, abort
import os
from utils.logger import setup_logger
from bot.dispatcher import handle_command

logger = setup_logger()
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

def start_webhook_listener():
    app = Flask(__name__)

    @app.route("/webhook", methods=["POST"])
    def webhook():
        if request.headers.get('X-Hub-Signature') != WEBHOOK_SECRET:
            abort(403)

        payload = request.json
        logger.info(f"📦 Webhook recibido: {payload}")

        # Lógica básica: reaccionamos a push
        if payload.get("ref") == "refs/heads/main":
            response = handle_command("mejora levelme.py")
            logger.info(f"🤖 Respuesta: {response}")

        return '', 200

    app.run(host="0.0.0.0", port=5000)
