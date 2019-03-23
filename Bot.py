import discord
from discord.ext import commands
import asyncio

bot =commands.Bot(command_prefix='?')
		
@bot.event
async def on_ready():
    print('The bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    bot.loop.create_task(status_task())    
    
@bot.command(pass_context = True)
async def meme(ctx):
    choices = ['https://img.memecdn.com/english_o_869587.webp', 'https://img.memecdn.com/everybody-knows-muricans-don-amp-039-t-speak-english-the-same-way-mexicans-don-amp-039-t-speak-spanish_c_7233205.webp', 'https://img.memecdn.com/english-reaction-when-they-heard-about-eu_c_6994013.webp', 'https://images3.memedroid.com/images/UPLOADED393/5b0c3ee92799f.jpeg' , '2/5b0c284b71cd0.jpeg', 'https://images3.memedroid.com/images/UPLOADED207/5b0c265a58cf4.jpeg', 'https://images7.memedroid.com/images/UPLOADED920/5b0c06813741a.jpeg', 'https://images3.memedroid.com/images/UPLOADED46/5a91c871e61f1.jpeg', 'https://images7.memedroid.com/images/UPLOADED737/5a91c7f234bd2.jpeg', 'https://images7.memedroid.com/images/UPLOADED757/5a91bd39e1323.jpeg', 'https://images7.memedroid.com/images/UPLOADED963/5a91b4f7aba7e.jpeg', 'https://images7.memedroid.com/images/UPLOADED794/5a91ac0900506.jpeg', 'https://images3.memedroid.com/images/UPLOADED188/5a91aa326ad4e.jpeg']
    embed = discord.Embed(title='Meme', description='For more memes check- https://www.memedroid.com')
    embed.set_image(url = random.choice(choices))
    await bot.send_typing(ctx.message.channel)
    await bot.send_message(ctx.message.channel, embed=embed)                                                            
  
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def kick(ctx,target:discord.Member):
	await bot.kick(target)
	await bot.say(f'{target} Has been Kicked!')
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def ban(ctx,target:discord.Member):
	await bot.ban(target)   
	await bot.say(f'{target} Has been Banned!')
	
     	 
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('?staffhelp'):
        embed = discord.Embed(title="staff commands", description="help!", color=0xff0000)
        embed.set_author(name="StaffHelp", icon_url="https://image.ibb.co/caM2BK/help.gif")
        embed.add_field(name=":x:Ban", value="to ban someone",inline=False)
        embed.add_field(name=":x:kick", value="to kick someone", inline=False)
        embed.add_field(name=":x:warn", value="to warn someone", inline=False)
        embed.add_field(name="purge", value="To delete messages", inline=False)
        embed.add_field(name="annoucement", value="under devlopping", inline=False)
        await bot.send_message(message.author, embed=embed)             	                         
        
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def warn(ctx,target:discord.Member):
	await bot.send_message(target,'U got a warning in Mehdi M.M.O server!!!')
	await bot.say(f'{target} have a new warning')
    
@bot.command()
async def giveaways():
	await bot.say('NEXT GIVEAWAY IS SHOUTOUT')
	await bot.say('__**SUBSCRIBE TO MEHDI MMO FOR MORE**__')
  
@bot.command()
async def support():
    await bot.say('__**HERE IS THE SUPPORT SERVER**__ https://discord.gg/a9TX5Fq ')
    
@bot.command()
@commands.has_permissions(manage_messages = True)
async def creator():
    await bot.say('$**mehdi m.m.o is the owner of this bot**$')
    await bot.say('**he have a youtube channel too named MEHDI MMO**')
                    
@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content=':ping_pong: Took: {}ms'.format(int(ms)))
    
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await bot.purge_from(ctx.message.channel, limit = number+1)
    
@bot.command()
async def yt():
    await bot.say('__**check Mehdi M.M.O Youtube Channel!!**__')
    await bot.say('https://www.youtube.com/channel/UCoJ_AY5z1xvYQbcJwW2XFew')
    await bot.say('__**subscribe and thanks!!**__')
    
@bot.command()
async def commands():
    await bot.say('```COMANDS:```')
    await bot.say('``` check your DM```')
    await bot.send_message(target,'__**The Commands**__ ')
    await bot.send_message(target,'**support : Get the support server invite**')
    await bot.send_message(target,'**yt : Get Mehdi M.M.O youtubes channel link**')
    await bot.send_message(target,'**meme : Get a meme**')
    await bot.send_message(target,'**giveaways : Get info about what is the next giveaway**')
    await bot.send_message(target,('**ping : To know much is the ping**')
 
 bot.remove_command('help')
bot.run('NTU3ODU4Mzc4OTE1Nzc0NDY0.D3Py6Q.RNKu7fhqHC-hRxiSok29BDVCT-w')
