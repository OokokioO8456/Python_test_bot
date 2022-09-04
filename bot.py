from ast import Delete, keyword
from email.policy import default
from itertools import takewhile
from sqlite3 import Timestamp
import discord
from discord.ext import commands
import datetime
import random


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '$$', intents = intents)


#啟動部分

@bot.event
async def on_ready():
    print(">> Bot is online <<")

#指令部分

@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="延遲 - ms", color=0xffdd00)
    embed.add_field(name="Ping", value=f"{round(bot.latency*1000)}ms", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def setup(ctx):
    await ctx.send(f'Setup Finish')

@bot.command()
async def save(ctx, item):
    if item == 'bot.py':
        await ctx.send(f'Saved Finish')

@bot.command()
async def hi(ctx):
    await ctx.send(f'哈囉你好')

#崁入訊息(指令)

@bot.command()
async def info(ctx):
    embed=discord.Embed(title="機器人資訊 - Bot info", color=0x00fffb, timestamp=datetime.datetime.now())
    embed.add_field(name="生日", value="2022/8/26", inline=True)
    embed.add_field(name="製作架構", value="Discord.py / Python", inline=True)
    embed.add_field(name="作者", value="杉杉33#0001", inline=True)
    embed.add_field(name="協作", value="終界龍#5021", inline=True)
    embed.add_field(name="邀請連結", value="https://reurl.cc/O45N4g", inline=True)
    embed.add_field(name="企劃發想", value="杉杉33#0001 , 終界龍#5021", inline=True)
    embed.add_field(name="延遲", value=f"{round(bot.latency*1000)}ms", inline=True)
    embed.add_field(name="版本", value=f"1.12.19", inline=True)
    embed.add_field(name="機器狀態", value="持續更新中", inline=True)
    embed.set_footer(text="美國時間")
    await ctx.send(embed=embed)

@bot.command()
async def help_list(ctx):
    embed=discord.Embed(title="幫助清單 - help list", color=0x00fffb)
    embed.add_field(name="clear", value="清理訊息", inline=True)
    embed.add_field(name="help_list", value="顯示這則訊息", inline=True)
    embed.add_field(name="info", value="機器資訊", inline=True)
    embed.add_field(name="ping", value="查看延遲", inline=True)
    embed.add_field(name="save", value="儲存專案", inline=True)
    embed.add_field(name="say", value="讓機器人代替你說話", inline=True)
    embed.add_field(name="setup", value="設定機器人", inline=True)
    embed.add_field(name="hi", value="讓機器人跟你說嗨", inline=True)
    embed.add_field(name="eat", value="吃個東西", inline=True)
    embed.add_field(name="announcement", value="開發團隊公告", inline=True)
    embed.add_field(name="embed", value="創建崁入訊息", inline=True)
    embed.set_footer(text="指令前綴: $$")
    await ctx.send(embed=embed)

#說出你打的字

@bot.command()
async def say(ctx, *,msg):
    await ctx.message.delete()
    await ctx.send(msg)

#刪除訊息

@bot.command()
async def clear(ctx, num:int):
    await ctx.channel.purge(limit=num+1)

@bot.command()
async def random(ctx):
    embed=discord.Embed(title="錯誤 - Errors", description="後台爆炸了!", color=0xff0000)
    await ctx.send(embed=embed)

@bot.command()
async def eat(ctx, item):
    user = ctx.author.id
    if item == 'apple':
        embed=discord.Embed(title="你吃了一顆蘋果!", description="", color=0xe1ff00)
        await ctx.send(embed=embed)
    if item == 'pen':
        embed=discord.Embed(title="這個東西不能吃欸...", description="", color=0xff0000)
        await ctx.send(embed=embed)
    if item == 'poop':
        embed=discord.Embed(title="你想要去吃屎???", description="", color=0xff0000)
        await ctx.send(embed=embed)
    if item == 'applepen':
        embed=discord.Embed(title="蘋果上面插著一支筆你還敢吃?", description="", color=0xff0000)
        await ctx.send(embed=embed)
    if item == 'pineapplepan':
        embed=discord.Embed(title="鳳梨上面插著一支筆你還敢吃????", description="", color=0xff0000)
        await ctx.send(embed=embed)
    if item == 'pineapple':
        embed=discord.Embed(title="你吃了一個鳳梨!", description="", color=0xe1a800)
        await ctx.send(embed=embed)
        
@bot.command()
async def announcement(ctx):
    embed=discord.Embed(title="機器人開發團隊公告", description="成員加入/離開訊息 [已關閉]", color=0x00fffb)
    embed.set_footer(text="幫助清單: $$help_list")
    await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
    await ctx.send(f'test')

@bot.command()
async def ann(ctx, title, *, content):
      channel_ID = 969599717652721687
      user = ctx.author.id
      channel = ctx.bot.get_channel(channel_ID)
      await channel.send(title + "\n" + content + f"\n- From <@{user}>")
      await ctx.send(f'<@{user}> 公告已成功發送至<#{channel_ID}>!')
      await ctx.message.delete()

@bot.command()
async def embed(ctx, *,msg):
    embed=discord.Embed(title=msg, description="", color=0xe1ff00)
    await ctx.send(embed=embed)


#Token
bot.run('MTAxMjcxOTEwMjk2OTc3ODIyNw.GHp2Gn.dooQh-66FRfPqjSsIW86vqFvp-b0dvr1wRfWeU')

