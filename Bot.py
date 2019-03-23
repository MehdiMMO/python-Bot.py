import discord
from discord.ext import commands
import asyncio
from itertools import cycle

bot =commands.Bot(command_prefix='?')

status = [ 'Prefix: ?' , 'CREATED BY MEHDI M.M.O']
		
@bot.event
async def on_ready():
    print('The bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    await bot.remove.command('help')
    
@bot.command()
async def giveaways():
	await bot.say('NEXT GIVEAWAY IS SHOUTOUT')
	await bot.say('__**SUBSCRIBE TO MEHDI MMO FOR MORE**__')
  
@bot.command()
async def suppot():
    await bot.say('__**HERE IS THE SUPPORT SERVER**__ https://discord.gg/a9TX5Fq ')
    
@bot.command()
@commands.has_permissions(manage_messages = True)
async def creator():
    await bot.say('$**mehdi m.m.o is the owner of this bot**$')
    await bot.say('**he have a youtube channel too named MEHDI MMO**')
                    
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await bot.purge_from(ctx.message.channel, limit = number+1)
    
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
    
@bot.command()
async def commands():
    await bot.say('```COMANDS:```')
    await bot.say('```say commands and check your DM```')
    
@bot.command()
async def staff():
	await bot.say('@REDFA77I_69#3354')
	await bot.say('@TSMQRST#2303')
	await bot.say('@Clearly#6317')
	await bot.say( '@MEHDI M.M.O [YT]#3114')
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('Commands'):
        embed = discord.Embed(title="Everyone", description="desktopBot Info!", color=0xff0000)
        embed.add_field(name="Ping", value="TO KNOW HOW MUCH IS THE PING", inline=False)    
        embed.add_field(name="yt", value="Then you can see mmo youtube channel", inline=False)
        embed.add_field(name="Creator", value="To know who created the bot!", inline=False)
        embed.add_field(name="giveaways", value="To know what is the next giveaway", inline=False)
        embed.add_field(name="staff", value="To know who is moderators in my server", inline=False)
        embed.add_field(name="support", value="to get the support server invite", inline=False)
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        await bot.send_message(message.author, embed=embed)
        
bot.run('NTU3ODU4Mzc4OTE1Nzc0NDY0.D3Py6Q.RNKu7fhqHC-hRxiSok29BDVCT-w')
        
