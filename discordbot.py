import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='',intents=discord.Intents.all())

@bot.event
async def on_message():
    await bot.change_presence(status=discord.status.online, activity=discord.Game('강의'))
    print('디스코드 봇이 열렸다!')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 야(ctx):
    await ctx.channel.send('호!')


@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 사랑해(ctx):
    await ctx.channel.send('나도')

bot.run("MTA2MjkyOTcyODY4NTc1MjM1MA.GJxq7b.7e2l2Pw0hUBaHa5L3aZ6IG9BNGMAFJI0uUa4uk")
