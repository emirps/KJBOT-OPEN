import discord
from discord import Member
import random
import discord.utils
from discord.ext import commands
import os
from config import TOKEN
prefixes = 'k?', 'kjbot ', 'kj ', 'kj!', 'k.'
bot=commands.Bot(command_prefix=prefixes)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'my prefix is k? [Currently watching {len(bot.guilds)} servers!]'))
    print('Logged on as {0.user}'.format(bot))
    print('https://www.akpress.org/friends-prisoner.html')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing arguments')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, you don't have permissions.")
@bot.event
async def on_guild_join(guild):
    channel=guild.system_channel
    embed = discord.Embed(title='Thanks for adding me!')
    embed.add_field(name='~Thanks!~',value='Thanks for adding me to the server! To see my prefixes, use k?prefixes! To see a list of commands, use k?help!')
    await channel.send(embed=embed)
@bot.command(category='Other')
async def choose(ctx, *choices: str):
    '''
    Choose from a certain number of choices
    '''
    embed=discord.Embed(title='Choose', color=0x0c0f27)
    val=random.choice(choices)
    embed=discord.Embed(title='Choose', color=0x0c0f27)
    embed.add_field(name='And the results are...', value=f'🎰 '+val)
    await ctx.send(embed=embed)
@bot.command(category='Moderation/Utility')
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    '''
    Ban a user
    '''
    await member.ban(reason = reason)
    embed=discord.Embed(title='Banned a member')
    embed.add_field(name='Member Banned', value=f'⛔ Banned '+member.name+' for '+reason)
    await ctx.send(embed=embed)
@bot.command(description='Flip a coin!', category='Fun and Games')
async def coinflip(ctx):
    '''
    Flip a coin
    '''
    hot=random.randint(1,2)
    embed=discord.Embed(title='Coinflip Results', color=0x0c0f27)
    if hot==1:
        embed.add_field(name='Coinflip', value=f'🪙 Heads!')
        await ctx.send(embed=embed)
    if hot==2:
        embed.add_field(name='Coinflip', value=f'🪙 Tails')
        await ctx.send(embed=embed)
@bot.command(aliases=['profile','avatar','pfp'],category='Moderation/Utility')
async def grabprofile(ctx, member: Member = None):
    '''
    Get a profile picture
    '''
    if not member:
        member = ctx.author
        profileurl=member.avatar_url
    embed = discord.Embed(title=member.name+"'s profile picture'")
    embed.set_image(url=profileurl)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
@bot.command(description='Bot latency',category='Moderation/Utility')
async def ping(ctx):
    '''
    Ping in ms
    '''
    embed = discord.Embed(title="Ping", color=0x0c0f27)
    embed.add_field(name="Bot", value=f'🏓 Pong! {round(bot.latency * 1000)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
@bot.command()
async def prefixes(ctx):
    '''
    View KJBOT's prefixes
    '''
    await ctx.send('My prefixes are k?, kjbot, and kj')
@bot.command()
@commands.is_owner()
async def restart(ctx):
    print(f"{ctx.author} sent a restart request")
    await ctx.send('Restarting...')
    await ctx.send('Restarted')
    os.system('py launcher.py')
bot.run(TOKEN)
