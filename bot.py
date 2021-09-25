import discord
import json
import PIL
import textwrap
from PIL import Image, ImageDraw, ImageChops, ImageFont
from discord import client
from discord.ext import commands
import requests
import creds
from os import remove

bot = commands.Bot(command_prefix='*', description='Your Description')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Future is loading ...')
    print('----------------------------------------------------------')
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(name='*help || YOPI'))


@bot.command()
async def quotes(ctx):
    author = ctx.message.author.id
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(f'<@{author}>\n{quote}')
    base = Image.open('temp2.jpg')
    basee = base.convert('RGB')
    para = textwrap.wrap(quote, width=80)
    W, H = (1280,417)
    draw = ImageDraw.Draw(basee)
    w, h = draw.textsize(quote)
    font = ImageFont.truetype("Quote.ttf", 40)
    current_h, pad = 210,30
    for line in para:
        x, y = draw.textsize(line, font=font)
        draw.text(((W-x)/2,current_h), line,font = font)
        current_h += h + pad
    newimage = basee.resize((1280,417))
    newimage.save(f'final.jpg')
    with open(f'final.jpg','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final.jpg"))
    remove(f'final.jpg')


@bot.command()
async def quotes1(ctx):
    author = ctx.message.author.id
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    await ctx.send(f'<@{author}>\n{quote}')
    base = Image.open('template.jpg')
    para = textwrap.wrap(quote, width=90)
    W, H = (1280,417)
    draw = ImageDraw.Draw(base)
    w, h = draw.textsize(quote)
    font = ImageFont.truetype("Quote.ttf", 36)
    current_h, pad = 335,25
    for line in para:
        x, y = draw.textsize(line, font=font)
        draw.text(((W-x)/2,current_h), line,font = font)
        current_h += h + pad
    newimage = base.resize((1280,417))
    newimage.save(f'final.jpg')
    with open(f'final.jpg','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final.jpg"))
    remove(f'final.jpg')


@bot.command()
async def whomadeu(ctx):
    await ctx.send(f'<@254700247471751171>')

bot.run(creds.token)
