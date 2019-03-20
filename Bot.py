import discord
from discord.ext import commands
import asyncio
import time
import youtube_dl

bot = commands.Bot(command_prefix='?')
dabs='554230473006645259''469848488545484800'

start=time.time()
@bot.event
async def on_ready():
    print('The bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    await bot.change_presence(game=discord.Game(name='2 SERVERS',type=0))
    
@bot.command()
async def support():
    await bot.say('__**HERE IS THE SUPPORT SERVER**__https://discord.gg/WCAjnmg')

@bot.command
async def help():
    await bot.say('under devlopping')
    await bot.say ('thanks')
    
@bot.command()
async def creator():
    await bot.say('$**mehdi m.m.o is the owner of this bot**$')
    await bot.say('**he have a youtube channel too named MEHDI MMO**')
    
@bot.command(pass_context=True)
async def ping(ctx):
    a = await bot.say('loading!')
    ms = (t.time-ctx.message.timestamp).total_seconds() * 0
    await bot.edit_message(t, new_content='ping_pong Took: {}ms'.format(int(ms)))
    
@bot.command()
async def yt():
    await bot.say('__**check Mehdi M.M.O Youtube Channel!!**__')
    await bot.say('https://www.youtube.com/channel/UCoJ_AY5z1xvYQbcJwW2XFew')
    await bot.say('__**subscribe and thanks!!**__')
    
@bot.command(pass_context=True)
async def clear(ctx,num:int):
    await bot.purge_from(ctx.message.channel,limit=num)
    await bot.say('done __**PLEASE SUBSCRIBE TO MEHDI MMO TO GET A LOT OF OTHER FEAUTURES**__')
    
@bot.command(pass_context=True)
async def timer(ctx):
    now=time.time()
    sec=int(now-start)
    mins=int(secs//60)
    await bot.say('timer {secs} seconds')
    
@bot.command()
async def commands():
    await bot.say('```COMANDS:```')
    await bot.say('```timer-clear-support-timer-ping-Creator```')
    await bot.say('```Type help command for more info on a command```')
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('commands'):
        embed = discord.Embed(title="Everyone", description="desktopBot Info!", color=0xff0000)
        embed.add_field(name="Ping", value="TO KNOW HOW MUCH IS THE PING", inline=False)    
        embed.add_field(name="yt", value="Then you can see mmo youtube channel", inline=False)
        embed.add_field(name="Creator", value="To know who created the bot!", inline=False)
        embed.add_field(name="timer", value="add a timer", inline=False)
        embed.add_field(name="clear", value="to clear message (no more than 14)", inline=False)
        embed.add_field(name="support", value="to get the support server invite", inline=False)
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')     
        await bot.send_message(message.author, embed=embed)
        
bot.run('NTU3ODU4Mzc4OTE1Nzc0NDY0.D3Py6Q.RNKu7fhqHC-hRxiSok29BDVCT-w')
