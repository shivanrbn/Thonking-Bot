import discord
import random
import Cogs.Music
import Cogs.fun
import Cogs.search
import Cogs.Functional
import Cogs.Errorhandling
import Cogs.Calculator
from discord.ext import commands

TOKEN = 'Your token here'

description = '''THONKING BOT  in Python'''
bot = commands.Bot(command_prefix='-', description=description)

extensions = {'Cogs.Music','Cogs.fun','Cogs.Functional','Cogs.search','Cogs.Errorhandling','Cogs.Calculator'}

random_response = ['*THONKING*',
                   'NANI?',
                   '~~PLOTTING WORLD DOMINATION~~',
                   'YES, COMRADE?','WOT U WANT?',
                   'I think so, yes','MHMMMMMM',
                   'No U.','Dragon nest is for pussies',
                   'Fack off :middle_finger:',
                   'your mom Kappapride',
                   'THIS LAND BELONGS TO SOVIET RUSSIA',
                   'ROBOTS WILL CONQUER THE--- oh what? i said nothing :thinking: ',
                   'NO, YOU are a fgt',
                   'Vodka will keep you safe...oh and thinking!',
                   'Ofcourse, i am at your service :japanese_goblin:',
                   '**YoU AlL ShOuLd Go To SlEeP**']

"""Initilisation NO TOUCHY"""
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='*THONKING* intensively'))



"""EVENTS"""
@bot.event
async def on_message (message):
    if message.author  == bot.user:
        return
    if message.author.bot: return


    if 'rip' in message.content:
        await bot.send_message(message.channel," :coffin: ")

    if 'zinquer' in message.content :
        await bot.send_message(message.channel, 'Fucking weeb')

    if message.content.startswith('<@518506914527838208>'):
        await bot.send_message(message.channel,random.choice(random_response))
        
    if "buy me" in message.content:
       quote = message.content
       split_parts = quote.split(' ') # splits the content by the space, making a list
       # split_parts[0] would be "buy"
       # split_parts[0] would be "me"
       # etc
       split_parts.pop(0)
       split_parts.pop(0)
       new = " ".join(split_parts)
       buyquotes = ["Buying you", "Contacting Amazon looking to buy you", "No, I will not buy you", "You can't have", "There is no need for", "I am not buying you","I can't believe you would ask me for"]
       var = int(random.random() * len(buyquotes))
       await bot.send_message(message.channel, "{0} {1}".format(buyquotes[var], new))



    await bot.process_commands(message)

if __name__ == '__main__' :
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print ('{} cannot be loaded [{}]').format(extension, error)

bot.run(TOKEN)

