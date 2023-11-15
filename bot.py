import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

async def leave(ctx):
    await ctx.voice_client.disconnect()

async def play(ctx, url):
    ydl_opts = {
        'format': 'bestaudio',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_channel = ctx.voice_client
        voice_channel.stop()
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn',
        }
        voice_channel.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))

@bot.command(name='소환')
async def join_command(ctx):
    await join(ctx)

@bot.command(name='나가', aliases=["disconnect", "skrk", "leave"])
async def leave_command(ctx):
    await leave(ctx)

@bot.command(name='play', aliases=["재생", "p", "wotod", "ㅔ"])
async def play_command(ctx, url):
    await play(ctx, url)

bot.run('MTE3NDI4OTM2OTY2Mjc1NDg5Ng.G_tKXG.ZAArVimaZqczhw7sa_NFRWtuZswRcG_zk6WyBw')