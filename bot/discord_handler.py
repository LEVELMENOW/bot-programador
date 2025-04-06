import discord
import os
from bot.dispatcher import handle_command

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'✅ Conectado como {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.channel.id == CHANNEL_ID:
            response = handle_command(message.content)
            await message.channel.send(response)

def start_discord_bot():
    intents = discord.Intents.default()
    intents.messages = True
    client = BotClient(intents=intents)
    client.run(DISCORD_TOKEN)
