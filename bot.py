import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('MTAxMjcxOTEwMjk2OTc3ODIyNw.GZq58d.74yZ_buKbSZreH77tJtD6ivmS0UobVvkVmSZ9A')
