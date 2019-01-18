import discord
from discord.ext import commands
import math
import operator

class Calculations:
    
    def __init__(self,bot):
        self.bot = bot
        
    def add(number1,number2):
        return int(number1) + int(number2)
    
    def sub(number1, number2):
        return int(number1) - int(number2)
    
    def mul(number1,number2):
        return int(number1) * int(number2)
    
    def div(number1,number2):
        return float(number1) / int(number2)
    
    def sqrt(number1):
        return math.sqrt(float(number1))
    
    def exp(number1,number2):
        return int(number1) ** int(number2)
        


class Calculator:
    def __init__(self,bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def calc(self, ctx):
        '''basic calculations, add/sub/mul/div/sqrt/exp'''
        if ctx.invoked_subcommand is None:
            await self.bot.say("``You need to enter a subcommand! these are: add,sub,mul,sqrt and exp``")
        
    @calc.group()
    async def add (self, number1: int, number2: int):
        try:
            await self.bot.say("{} + {} =".format(number1,number2))
            await self.bot.say( Calculations.add(number1,number2))
        except:
            await self.bot.say("Error, too stupid to calculate the requested data")
        
    @calc.group()
    async def sub (self, number1: int, number2: int):
        try:
            await self.bot.say("{} - {} =".format(number1,number2))
            await self.bot.say( Calculations.sub(number1,number2))
        except:
            await self.bot.say("Error, too stupid to calculate the requested data")
        
    @calc.group()   
    async def mul (self, number1: int, number2: int):
        try:
            await self.bot.say("{} * {} =".format(number1,number2))
            await self.bot.say( Calculations.mul(number1,number2))
        except:
            await self.bot.say("Error, too stupid to calculate the requested data")
    @calc.group()   
    async def div (self, number1: int, number2: int):
        try:
            await self.bot.say("{} / {} =".format(number1,number2))
            await self.bot.say( Calculations.div(number1,number2))
        except:
            await self.bot.say("Error, too stupid to calculate the requested data")
    @calc.group()
    async def sqrt(self,number1):
        try:
            await self.bot.say("the square root of {} =".format(number1))
            await self.bot.say(Calculations.sqrt(number1))
        except:
            await self.bot.say("Error, too stupid to calculate the requested data")
    @calc.group()
    async def exp(self,number1: int, number2: int):
        left = '\U000023E9'
        right = '\U000023EA'
        if  number1 < 10000000000000000 and number2 < 101:
            await self.bot.say("The exponent {} ^ {} =".format(number1,number2))
            await self.bot.say(Calculations.exp(number1,number2))
        else:
            await self.bot.say("Error, too stupid to calculate the requested data, base limit is 10000000000000000 (16 zero's), exponent limit is 100")
    
    @calc.error
    async def calc_on_error(self,ctx,error):
        await self.bot.send_message(ctx.message.channel, "Error, too stupid to calculate the requested data")
    
    
def setup(bot):
    bot.add_cog(Calculator(bot))
