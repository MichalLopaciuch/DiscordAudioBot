from logger import Logger
from intents import INTENTS
from discord.ext import commands

intents = INTENTS
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.command()
async def ping(ctx):
    Logger.log('Sending pong')
    await ctx.send('pong')
