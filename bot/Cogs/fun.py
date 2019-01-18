import discord
import asyncio
import random
from discord.ext import commands

class fun:
    """Fun commands to annoy someone"""
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def weeb(self, member: discord.Member):
        '''Call someone a fucking weeb'''
        random_weebsponse = ['A shut in NEET','definitely a weeb','rather an otaku','Maybe a weeb','a lolicon','A FUCKING WEEB REEEEEEE']
        await self.bot.say("{} is {}".format(member.name, random.choice(random_weebsponse)))
        
    @commands.command(pass_context=True)
    async def slap(self, ctx, member: discord.Member):
        '''Slap someone you hate.'''
        try:
            if self.bot.user.id in member.mention:
                await self.bot.say('gtfo cunt :middle_finger: ')

            else:
                await self.bot.say("{} slapped the shit out of {}".format(ctx.message.author.name, member.name))
        except:
            await self.bot.say("You need to mention a user to slap them")
            
    @commands.command(pass_context=True)
    async def kill(self, ctx, *,member:discord.Member = None):
        '''Kill someone.'''
        author = ctx.message.author
        try:
            if member is None:
                await self.bot.say(author.mention +": I can't kill someone if no one is mentioned :coffin:")
                return
            elif member.id == author.id:
                await self.bot.say(author.mention +": you want to commit soduku? :rofl:")
                await self.bot.say("i mean i can help but :thinking:")
            elif member.id == self.bot.user.id:
                await self.bot.say("You cant kill me first if i kill you first! :knife:")
            elif member.id != author.id:
                await self.bot.say("affirmative, mobilizing poisoned knife to target {} :knife: ".format(member.name))
            else:
                await self.bot.say("There is no member named {}".format(ctx.message.author))
        except: await self.bot.say("You need to mention a user pleb!")
        if commands.BadArgument:
            await self.bot.say("ERROR")
    @commands.command(pass_context=True)
    async def slots(self,ctx):
        '''Test your luck!'''
        slotindex= [":coffin:",":rofl:",":cherries:",":seven:"]
        slot1 = random.choice(slotindex)
        slot2 = random.choice(slotindex)
        slot3 = random.choice(slotindex)
        
        slot4 = random.choice(slotindex)
        slot5 = random.choice(slotindex)
        slot6 = random.choice(slotindex)
        
        slot7 = random.choice(slotindex)
        slot8 = random.choice(slotindex)
        slot9 = random.choice(slotindex)
        
        
        slotOutput1 = "vvvv| {} | {} | {} |vvvv\n".format(slot1, slot2, slot3)
        slotOutput2 = ">>>| {} | {} | {} |<<< \n".format(slot4, slot5, slot6)
        slotOutput3 = "^^^^| {} | {} | {} |^^^^\n".format(slot7, slot8, slot9)
        if slot4 == slot5 and slot5 == slot6:
            await self.bot.send_message(ctx.message.channel, "{} \n {} \n {} \n Won".format(slotOutput1,slotOutput2, slotOutput3))
        else:
            await self.bot.send_message(ctx.message.channel, "{} \n {} \n {} \nLost".format(slotOutput1, slotOutput2,slotOutput3))
                  
    @commands.command(pass_context=True)
    async def rps(self,ctx):
        '''Roll a rock-paper-scissors, if you dare'''
        randomRPS = ["Rock." , "Paper." , "Scissors."]
        await self.bot.say("I challenge you to a rock-papers-scissors duel :knife:")
        choice = "{}".format(random.choice(randomRPS))
        await self.bot.say ("You threw a whopping " + choice)
        resultBot = "{}".format(random.choice(randomRPS))
        await self.bot.say("And i threw a {}".format(resultBot))
      
        if choice == resultBot:
            await self.bot.say("It's a TIE, FfS")
        elif choice == randomRPS[0] and resultBot == randomRPS[2]:
            await self.bot.say("FFS you win **ragequits**")
        elif choice == randomRPS[1] and resultBot == randomRPS[0]:
            await self.bot.say("FFS you win **ragequits**")
        elif choice == randomRPS[2] and resultBot == randomRPS[1]:
            await self.bot.say("FFS you win **ragequits**")
        elif choice == randomRPS[0] and resultBot == randomRPS[1]:
            await self.bot.say("Git gud noob")
        elif choice == randomRPS[1] and resultBot == randomRPS[2]:
            await self.bot.say("Git gud noob")
        elif choice == randomRPS[2] and resultBot == randomRPS[0]:
            await self.bot.say("Git gud noob")
    
        
def setup(bot):
    bot.add_cog(fun(bot))