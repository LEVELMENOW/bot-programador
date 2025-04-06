from utils.logger import setup_logger
from utils.env_loader import load_env
from bot.discord_handler import start_discord_bot
from bot.webhook_listener import start_webhook_listener

logger = setup_logger()
load_env()

if __name__ == "__main__":
    logger.info("🚀 Bot programador iniciado (modo Boss).")
    start_discord_bot()
    start_webhook_listener()
