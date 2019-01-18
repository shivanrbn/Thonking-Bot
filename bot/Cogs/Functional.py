import discord
import random
import asyncio
from discord.ext import commands

class Functional:
    """Functional commands"""
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def user_info(self, ctx):
        '''shows your own information'''
        UserCreatedEmbed = discord.Embed(
                title = 'User ID:',
                description = ctx.message.author.id,
                colour = discord.Colour.blue()
                )
                
        UserCreatedEmbed.set_footer(text='searched by {}'.format(ctx.message.author))
        UserCreatedEmbed.set_image(url=ctx.message.author.avatar_url)
        UserCreatedEmbed.set_author(name =ctx.message.author.name , icon_url ='')
        UserCreatedEmbed.add_field(name='Date created:', value ="{} ".format(ctx.message.author.created_at),inline = False)
        UserCreatedEmbed.add_field(name='Date joined:', value ="{}".format(ctx.message.author.joined_at),inline = False)
        
        
        await self.bot.say(embed=UserCreatedEmbed)
        
    @commands.command(pass_context=True)
    async def member_info(self, ctx, member: discord.Member):
        '''show user related information'''
        
        if member is None:
            await self.bot.say("You need to tag a member to get info about him/her/not assuming genders!")
        else:
            SearchCreatedEmbed = discord.Embed(
                    title = 'User ID:',
                    description = member.id,
                    colour = discord.Colour.blue()
                    )
                    
            SearchCreatedEmbed.set_footer(text='searched by {}'.format(ctx.message.author))
            SearchCreatedEmbed.set_image(url= member.avatar_url)
            SearchCreatedEmbed.set_author(name = member.name , icon_url ='')
            SearchCreatedEmbed.add_field(name='Date created:', value ="{} ".format(member.created_at),inline = False)
            SearchCreatedEmbed.add_field(name='Date joined:', value ="{}".format(member.joined_at),inline = False)
            
            
            await self.bot.say(embed=SearchCreatedEmbed)
        
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def createrole(self,ctx,*, create):
        '''Create a role, only Admins can do this.'''
        try:
            author = ctx.message.author
            await self.bot.create_role(author.server, name = ("{}".format(create)))
            await self.bot.say("Created the role {}.".format(create))
        except KeyError:
            author = ctx.message.author
            await self.bot.create_role(name="{}".format(create))
            await self.bot.say("Created the role {}.".format(create))
       
     
            
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def addrole(self,ctx, *, add):
        '''Add a role to yourself, currently only Admin can do this'''
        try:
            user = ctx.message.author
            role = discord.utils.get(user.server.roles,name="{}".format(add))
            await self.bot.add_roles(user, role)
            await self.bot.say("Added the role {} to the user {}.".format(add, user))
        except KeyError:
            user = ctx.message.author
            role = discord.utils.get(user.server.roles , name= "{}".format(add))
            await self.bot.add_roles(user, role)
            await self.bot.say("Added the role {} to the user {}.".format(add, user))
        except:
            await self.bot.say("You don't have permission to do this you shet")
    
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def removerole(self,ctx, *, remover):
        '''Remove a role from yourself, currently only Admin can do this'''
        try:
            user = ctx.message.author
            role = discord.utils.get(user.server.roles,name="{}".format(remover))
            await self.bot.remove_roles(user, role)
            await self.bot.say("Removed the role {} from the user {}.".format(remover, user))
        except KeyError:
            user = ctx.message.author
            role = discord.utils.get(user.server.roles , name= "{}".format(remover))
            await self.bot.remove_roles(user, role)
            await self.bot.say("Removed the role {} from the user {}.".format(remover, user))
        except:
            await self.bot.say("You don't have permission to do this you shet")
        
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def rolemute(self,ctx, member: discord.Member):
        role = discord.utils.get(member.server.roles,name='Muted')
        await self.bot.add_roles(member, role)
        await self.bot.say("Affirmative, the dirthy capitalist is muted with the role!")
        
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def roleunmute(self,ctx, member: discord.Member):
        role = discord.utils.get(member.server.roles,name='Muted')
        await self.bot.remove_roles(member, role)
        await self.bot.say("Affirmative, the role has been removed!")
        
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def mute(self,ctx, member: discord.Member):
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await self.bot.edit_channel_permissions(ctx.message.channel,member, overwrite)
        await self.bot.say("Da, {} is muted!".format(member))
        
    @commands.command(pass_context=True)
    @commands.has_role("Admin")
    async def unmute(self,ctx, member: discord.Member):
        await self.bot.delete_channel_permissions(ctx.message.channel,member)
        await self.bot.say("Da, {} is unmuted!".format(member))
                    

def setup(bot):
    bot.add_cog(Functional(bot))