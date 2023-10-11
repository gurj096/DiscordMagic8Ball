#Imports required modules
import discord
from discord.ext import commands
import random

#Dictionary pairing an integer with a value that will be returned 
mag_dic = {1:'It is certain', 2:'It is decidedly so', 3:'Without a doubt', 4:'Yes definitely', 5:'You may rely on it',
           6:'As I see it, yes', 7:'Most likely', 8:'Outlook good', 9:'Yes', 10:'Signs point to yes', 11:'Reply hazy, try again',
           12:'Ask again later', 13:'Better not tell you now', 14:'Cannot predict now', 15:'Concentrate and ask again',
           16:'Don\'t count on it', 17:'My reply is no', 18:'My sources say no', 19:'Outlook not so good', 20:'Very doubtful'}

#establishes intents before initiating bot
intents = discord.Intents.default()
intents.message_content = True
#Sets the prefix which will queue the bot to listen in on commands
bot = commands.Bot(command_prefix='/', intents=intents)

#Uses .command to initialize bot
@bot.command()
async def magic(ctx): #Defines the wake command as '/magic'. Once entered, the bot will respond with "What is your question"
    await ctx.send('What is your question?')
    question = await bot.wait_for('message') #Bot waits for msg from user before continuing
    if question != "" :
        shake_ball = random.randint(1,20) #Randomly selects an integer from 1-20
        await ctx.send(mag_dic[shake_ball]) #outputs the dictionary associated with integer key

bot.run('') # This would normally include unique key provided by Discord
