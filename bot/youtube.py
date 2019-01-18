import discord
import youtube_dl
from discord.ext import commands


players = {}
queues = {}


class youtube:

    def __init__(self, bot):
        self.bot = bot

    """check queues NO TOUCHY"""
    def check_queue(id):
        if queues[id] != []:
            player = queues[id].pop(0)
            players[id] = player
            player.start()
            
        else:
            del players[id]

    """YOUTUBE SECTION NO TOUCHY"""

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice_channel
        await self.bot.join_voice_channel(channel)

    @commands.command( pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        await voice_client.disconnect()

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        try:
            if players[server.id].is_playing():
                player = await voice_client.create_ytdl_player(url, after=lambda : check_queue(server.id), before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")

                if server.id in queues:
                    queues[server.id].append(player)
                    await self.bot.say('Playing THONKING MUSIC')

                else:
                    queues[server.id] = [player]
                    await self.bot.say ('Video queued.')
            else:
                player = await voice_client.create_ytdl_player(url, after=lambda : check_queue(server.id), before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
                players[server.id] = player
                player.start()
                await self.bot.say('Now starting ZA MUSIC')

        except KeyError:
            player = await voice_client.create_ytdl_player(url, after=lambda : check_queue(server.id), before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
            players[server.id] = player
            player.start()
            await self.bot.say('Now starting ZA MUSICerror')

    """video controls"""
    @commands.command(pass_context=True)
    async def pause(self, ctx):
        id = ctx.message.server.id
        players[id].pause()

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        id = ctx.message.server.id
        players[id].stop()

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        id = ctx.message.server.id
        players[id].resume()

    @commands.command(pass_context=True)
    async def skip(self, ctx):
        id = ctx.message.server.id
        players[id].stop()

def setup(bot):
    bot.add_cog(youtube(bot))
