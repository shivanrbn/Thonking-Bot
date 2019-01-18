import discord
from discord.ext import commands
import praw
import random
from bs4 import BeautifulSoup
import requests
import json
import wikipediaapi
from google import google
from igdb_api_python.igdb import igdb as igdb




wiki = wikipediaapi.Wikipedia('en')

reddit = praw.Reddit(username='your reddit username here',
                     user_agent='THONKING Bot v1.0',
                     client_id='your reddit client id here',
                     client_secret='your reddit client secret here')


igdb = igdb("Your igdb key here")


class search:
                      
    
    def __init__(self,bot):
        self.bot = bot
        

     
        
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 5.0,commands.BucketType.user)
    async def hmeme(self,ctx):
        '''Displays a random hot meme'''
        await self.bot.say("Searching....")
        memes_subreddit = reddit.subreddit('memes').hot()
        randompick = random.randint(1,25)
        try:
            for i in range(0, randompick):
                submission = next(x for x in memes_subreddit if not x.stickied)
            SearchCreatedEmbed = discord.Embed(
                title = 'Name:',
                description = submission.title,
                colour = discord.Colour.blue()
                )
                    
            SearchCreatedEmbed.set_footer(text='searched by {}'.format(ctx.message.author))
            SearchCreatedEmbed.set_image(url= submission.url)
            SearchCreatedEmbed.set_author(name = "Here's what i could find:" , icon_url ='')
            

            await self.bot.say(embed=SearchCreatedEmbed)
        except:
            await self.bot.sday("Error404, could not retrieve holy memes :cry:")
            
    @hmeme.error
    async def hmeme_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {:.2}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
    
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 5.0 ,commands.BucketType.user)
    async def nmeme(self,ctx):
        '''Displays a random new meme'''
        await self.bot.say("Searching....")
        memes_subreddit = reddit.subreddit('memes').hot()
        randompick = random.randint(1,25)
        try:
            for i in range(0, randompick):
                submission = next(x for x in memes_subreddit if not x.stickied)
            SearchCreatedEmbed = discord.Embed(
                title = 'Name:',
                description = submission.title,
                colour = discord.Colour.blue()
                )
                    
            SearchCreatedEmbed.set_footer(text='searched by {}'.format(ctx.message.author))
            SearchCreatedEmbed.set_image(url= submission.url)
            SearchCreatedEmbed.set_author(name = "Here's what i could find:" , icon_url ='')
            

            await self.bot.say(embed=SearchCreatedEmbed)
        except:
            await self.bot.sday("Error404, could not retrieve holy memes :cry:")
    
    @nmeme.error
    async def nmeme_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {:.2}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
    
    
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 5.0,commands.BucketType.user)
    async def r(self,ctx, subreddit_name):
        '''Search a subreddit for new posts'''  
        all_subreddits = reddit.subreddit('{}'.format(subreddit_name)).new(limit=1)
        if len(subreddit_name) > 2:
            try:
                await self.bot.say("Searching....")
                for submission in all_subreddits:
                    AllRedditEmbed = discord.Embed(
                        title = 'Name:',
                        description = submission.title,
                        colour = discord.Colour.blue()
                        )
                                
                    AllRedditEmbed.set_footer(text='searched by {}'.format(ctx.message.author))
                    AllRedditEmbed.add_field(name = "Subreddit:", value =submission.subreddit, inline = False)
                    AllRedditEmbed.add_field(name = "Link:", value =submission.url, inline = False)
                    """ALlRedditEmbed.add_field(name = "Text:", value =submission.selftext, inline = False)"""
                    AllRedditEmbed.set_image(url= submission.url)
                    AllRedditEmbed.set_author(name = "Here's what i could find:" , icon_url ='')
                        

                    await self.bot.say(embed=AllRedditEmbed)
            except:
                await selg.bot.say("Error, could not retrieve information")

        else:
            await self.bot.say("The subreddit's name must be atleast 3 letters long!")
            
    @r.error
    async def r_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {:.2}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
    
       
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 30.0,commands.BucketType.user)
    async def w(self, ctx, *,  page):
        '''Search a subject on wikipedia.'''
        await self.bot.say("Awaiting info.")
        info = wiki.page('{}'.format(page))
        if info.exists():
            try:
                WikiEmbed = discord.Embed(
                    title="Term:",
                    description=info.title,
                    colour=discord.Colour.red()
                    )
                
                WikiEmbed.set_author(name ="Here's what i could find:",icon_url ='')
                WikiEmbed.add_field(name="Summary:", value =info.text[0:1000], inline = False)
                WikiEmbed.add_field(name="Link:", value =info.fullurl, inline = False)
                
                await self.bot.say(embed=WikiEmbed)
            except:
                await self.bot.say("Could not retrieve Information")
        else:
            await self.bot.say("Page does not exist.")
    
    @w.error
    async def w_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
            
            
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 5.0 ,commands.BucketType.user)
    async def ud(self, ctx, *, search):
        '''Search the urban dictionary for a word!'''
        try:
            word = "{}".format(search)
            r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
            soup = BeautifulSoup(r.content)
            SearchCreatedEmbed = discord.Embed(
                colour = discord.Colour.blue()
                )
                    
            SearchCreatedEmbed.set_author(name = "Urban Dictionary" , icon_url ='')
            SearchCreatedEmbed.add_field(name='Word:', value ="{}".format(search),inline = False)
            SearchCreatedEmbed.add_field(name='Meaning:', value =soup.find("div",attrs={"class": "meaning"}).text , inline = False)
            SearchCreatedEmbed.add_field(name='Link:', value ="http://www.urbandictionary.com/define.php?term={}".format(word),inline = False)
            
            await self.bot.say(embed=SearchCreatedEmbed)
        except:
            await self.bot.say("Could not find the word {} in the dictionary Feelsbatman".format(search))
            
    @ud.error
    async def ud_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {:.2}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
    
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 30.0 ,commands.BucketType.user)
    async def g(self,ctx, *, query):
        await self.bot.say("Searching, please wait...")
        search_results = google.search("{}".format(query),num_page)
        for result in search_results:
            GoogleEmbed=discord.Embed(
                colour = discord.Colour.red()
                )
            GoogleEmbed.add_field(name="Result:",value=result.name,inline=False)
            await self.bot.say(embed=GoogleEmbed)
            
    @g.error
    async def g_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {:.2}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
        
    
    @commands.command(pass_context=True)
    @commands.cooldown(1.0, 300.0 ,commands.BucketType.user)
    async def igdb(self, ctx, *,  search):
        '''Search the Internet Game Database for a game.'''
        data = igdb.games({
            'search':"{}".format(search),
            'fields' : 'name'
            })
        
        IGDBEmbed = discord.Embed(
            colour = discord.Colour.green()
            )
        
        IGDBEmbed.set_author(name="Games:",icon_url='')
        for game in data.body:
            IGDBEmbed.add_field(name="Game name:", value=game['name'],inline= False)
        
        await self.bot.say(embed=IGDBEmbed)
        
    @igdb.error
    async def igdb_error(self, error, ctx):
        if isinstance(error,commands.CommandOnCooldown):
            msg = 'this command is ratelimited, please try again in {}s'.format(error.retry_after)
            await self.bot.send_message(ctx.message.channel,msg)
        
        
def setup(bot):
       bot.add_cog(search(bot))
        
    
