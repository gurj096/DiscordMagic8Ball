# Imports required modules
import discord
from discord.ext import commands
import random

# Dictionary pairing an integer with a value that will be returned 
MAG_DICT = {1:'It is certain', 2:'It is decidedly so', 3:'Without a doubt', 4:'Yes definitely', 5:'You may rely on it',
           6:'As I see it, yes', 7:'Most likely', 8:'Outlook good', 9:'Yes', 10:'Signs point to yes', 11:'Reply hazy, try again',
           12:'Ask again later', 13:'Better not tell you now', 14:'Cannot predict now', 15:'Concentrate and ask again',
           16:'Don\'t count on it', 17:'My reply is no', 18:'My sources say no', 19:'Outlook not so good', 20:'Very doubtful'}

# Establishes intents before initiating bot
intents = discord.Intents.default()
intents.message_content = True
# Sets the prefix which will queue the bot to listen in on commands
bot = commands.Bot(command_prefix='?', intents=intents)

# Command '?magic [<argument>, ...]'
@bot.command()
async def magic(ctx, *args): 
    # Handle case of empty arguments
    if len(args) == 0:
        await ctx.send(f'Please enter a question after the `?magic` command.\nFor Example, `?magic Will I win the lottery?`')
        return

    # Generate random number between 1 and 20 and use that number to search
    # the pre-defined set MAG_DIC
    shake_ball = random.randint(1,20)
    await ctx.send(MAG_DICT[shake_ball])

bot.run('') # This would normally include unique key provided by Discord
