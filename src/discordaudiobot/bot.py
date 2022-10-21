from discord import FFmpegPCMAudio
from downloader import Downloader
from discord.ext import commands
from intents import INTENTS
from guild import Guild

guilds = list()
bot = commands.Bot(
    command_prefix='?',
    intents=INTENTS)


@bot.command()
async def usage(ctx):
    await ctx.send(
        f'Usage:\n'
        f'{bot.command_prefix}play <link> - plays provided link\n'
        f'(wip){bot.command_prefix}skip - skips current audio\n'
        f'{bot.command_prefix}disconnect - disconnects from server and clears queue\n'
        f'{bot.command_prefix}queue - shows current queue\n')


@bot.command()
async def play(ctx, *, search: str) -> None:
    if not ctx.voice_client:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect(self_deaf=True)
        else:
            await ctx.send('join any voice channel first')

    if ctx.guild.id not in [guild.id for guild in guilds]:
        guilds.append(Guild(ctx.guild.id))

    guild = guilds[[_guild.id for _guild in guilds].index(ctx.guild.id)]
    guild.add_to_queue(search)

    # TODO: fix downloading
    audio_source = Downloader.download(search)
    if audio_source is not None:
        await ctx.send(f'{search} has been added to the queue')
        await ctx.voice_client.play(FFmpegPCMAudio(
            audio_source.get('entries')[0].get('original_url')))
    else:
        await ctx.send(f'no relevant results found for {search}')


@bot.command()
async def disconnect(ctx) -> None:
    if ctx.voice_client:
        await ctx.send(f'bye')
        guild = guilds[[_guild.id for _guild in guilds].index(ctx.guild.id)]
        guilds.remove(guild)
        await ctx.voice_client.disconnect()


@bot.command()
async def queue(ctx) -> None:
    if ctx.voice_client:
        guild = guilds[[_guild.id for _guild in guilds].index(ctx.guild.id)]
        links = list(guild.queue.queue)
        if len(links) > 0:
            ls = '\n'.join(links)
            await ctx.send(f'{ls}')
        else:
            await ctx.send(f'queue is empty')
