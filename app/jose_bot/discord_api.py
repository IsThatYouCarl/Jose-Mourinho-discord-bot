from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Hello, I'm the special one")

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user  :
            return 
        command, user_message = None, None

        for text in ['/gpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
                
        if command == '/gpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)