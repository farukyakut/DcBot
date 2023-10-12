import discord
from utils import*
from discord.ext import commands
from functions import*


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!fy ", intents=intents)
game = Game()


@Bot.event
async def on_ready():
    print("Hazırım Reis!")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hos-geldiniz")
    await channel.send(f"{member} aramıza katıldı. Hoş geldin!")
    print(f"{member} aramıza katıldı. Hoş geldin!")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="ayrılanlar")
    await channel.send(f"{member} aramızdan ayrıldı. :( ")
    print(f"{member} aramızdan ayrıldı. :( ")

@Bot.command(aliases=["game","oyun"])
async def farukyakut(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:    
        await ctx.send('babaaa')

@Bot.command()
async def burakvecemal(msg):
    await msg.send('faruğun has müridleri')


Bot.run("ODQ2Nzk4NzEwNjc0Njg1OTgz.YK0wwQ.GONYOAq6--Y1yu1-ObpZ7shAxrc")



