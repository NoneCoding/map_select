import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from map_command import Map

load_dotenv("map_key.env")

MAP_KEY = os.getenv("MAP_KEY")

intents = nextcord.Intents.all()

bot = commands.Bot(prefix=".", intents=intents)

bot.add_cog(Map(bot))

@bot.event
async def on_ready():
    print("Ready! Logged as {}".format(bot.user))

bot.run(MAP_KEY)
