---
tags:
  - web
---
# Creating Bot
1. Discord developer portal. https://discord.com/developers/applications. Create a new bot and give it a name and permissions
2. Set permissions
   ![[Discord Bot-20241025202045791.webp]]
3. Generate token ![[Discord Bot-20241025202148272.webp]]
4. Installation Tab > Guild Install
   ![[Discord Bot-20241025202317985.webp]]
5. Open the install link
   ![[Discord Bot-20241025202332893.webp]]
### Python Scripting
Boilerplate: Use [[Python dotenv]] to hide the API keys
```py
import asyncio
import discord
from discord.ext import commands
from discord import app_commands

async def main():
    TOKEN = "[YOUR TOKEN HERE]" # Homework: Load from a .env file, since putting tokens in code is bad practice

    # BOT SETUP
    intents = discord.Intents.all()
    intents.message_content = True  # Enable the message content intent
    intents.members = True  # Enable the message content intent
    bot = commands.Bot(command_prefix="!", intents=intents)  # Set a command prefix

    # Event to show bot is ready
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

        await bot.tree.sync()
    
    # Run the bot
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
```