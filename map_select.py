import nextcord
from nextcord.ext import commands
from random import choice
import os
from dotenv import load_dotenv

class Map(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    supported_games = ["csgo", "cs:go"]
    csgo_active_duty = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust II", "Vertigo", "Ancient"]
    csgo_reserve = ["Train", "Cache", "Grind", "Mocha"]
    csgo_hostage = ["Militia", "Agency", "Office", "Italy", "Assault"]
    
    
    @commands.command()
    async def choose(self, ctx, game, *, mode="all"):
        game = game.lower()
        
        if game not in Map.supported_games:
            return await ctx.send("Esse jogo não é suportado!")
        
        if game in ["csgo", "cs:go"]:
            if mode == "active duty":
                return await ctx.send("Seu mapa é: {}".format(choice(Map.csgo_active_duty)))
            
            elif mode == "reserve":
                return await ctx.send("Seu mapa é: {}".format(choice(Map.csgo_reserve)))
            
            elif mode == "hostage":
                return await ctx.send("Seu mapa é: {}".format(choice(Map.csgo_hostage)))
            
            elif mode == "all":
                all = []
                all.extend(Map.csgo_active_duty)
                all.extend(Map.csgo_reserve)
                all.extend(Map.csgo_hostage)
                return await ctx.send("Seu mapa é: {}".format(choice(all)))
            
            return await ctx.send("Esse modo de jogo não é suportado :(")
        
                
load_dotenv("map_key.env")

MAP_KEY = os.getenv("MAP_KEY")

intents = nextcord.Intents.all()

bot = commands.Bot(prefix=".", intents=intents)

bot.add_cog(Map(bot))

@bot.event
async def on_ready():
    print("Ready! Logged as {}".format(bot.user))
    

bot.run(MAP_KEY)
