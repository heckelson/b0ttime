# bot.py

import os
import sys
import logging

from twitchio.ext import commands

from counter import Counter
from dsmessages import DSMessages
from sound import Sound

# RESSOURCES: #############################################################
# Tutorial on how to make this bot:
# https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8
###########################################################################

# TODO: ###################################################################
# * add a self.sound of eric andre saying "Cheers I'll drink to that bro" https://www.youtube.com/watch?v=O35Dxb_V2Sc

logging.basicConfig(level=logging.INFO)


class Bot(commands.Bot):
    # set up a counter
    counter = Counter()
    
    # set up dark souls messages
    dsmsg = DSMessages()

    # set up sound commands
    sound = Sound()
    
    def __init__(self):
        super().__init__(
        irc_token   =   os.environ['TMI_TOKEN'],
        client_id   =   os.environ['CLIENT_ID'],
        nick        =   os.environ['BOT_NICK'],
        prefix      =   os.environ['BOT_PREFIX'],
        initial_channels=[os.environ['CHANNEL']])


    async def event_ready(self):
        logging.info(f"{self.nick} is online!")
        await self._ws.send_privmsg(os.environ['CHANNEL'], "/me successfully b00ted!")


    # Utility commands

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('/me Test successful!')

    @commands.command(name='kill')
    async def kill(self, ctx):
        if ctx.author.is_mod:
            await ctx.send('/me Goodbye World!')
            sys.exit()
        else:
            return


    # self.sound Commands

    @commands.command(name='alert')
    async def alert(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me !')
        self.sound.play("sounds/alert.mp3")

    @commands.command(name='modem')
    async def modem(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me does not compute...')
        self.sound.play("sounds/modem.mp3")


    @commands.command(name='yeet')
    async def yeet(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me yeet')
        self.sound.play("sounds/yeet.mp3")


    @commands.command(name='oof')
    async def oof(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me oof')
        self.sound.play("sounds/oof.mp3")


    @commands.command(name='oooooof')
    async def oooooof(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me oooooof')
        self.sound.play("sounds/oooooof.mp3")


    @commands.command(name='youdied')
    async def youdied(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me YOU DIED')
        self.sound.play("sounds/youdied.mp3")


    @commands.command(name='steam')
    async def steam(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me got a new message')
        self.sound.play('sounds/steam.mp3')


    @commands.command(name='objection')
    async def objection(self, ctx):
        if not self.sound.is_on_cooldown():
            await ctx.send('/me OBJECTION!')
        self.sound.play('sounds/objection.mp3')


    # self.counter Commands

    @commands.command(name='count')
    async def count(self, ctx):
        await ctx.send(f"The self.counter is currently at: {self.counter.count}")


    @commands.command(name='increment')
    async def increment(self, ctx):
        self.counter.increment()
        self.counter.write_count()
        await ctx.send(f"The self.counter is now at: {self.counter.count}")


    @commands.command(name='decrement')
    async def decrement(self, ctx):
        self.counter.decrement()
        self.counter.write_count()
        await ctx.send(f"The self.counter is now at: {self.counter.count}")


    @commands.command(name='reset')
    async def reset(self, ctx):
        self.counter.reset()
        self.counter.write_count()
        await ctx.send("The self.counter has been reset (0).")


    @commands.command(name="modify")
    async def modify(self, ctx, modifier):
        self.counter.modify(modifier)
        self.counter.write_count()
        await ctx.send(f"The self.counter has been modified and is now at: {self.counter.count}")


    @commands.command(name='set')
    async def set(self, ctx, newval):
        self.counter.set(newval)
        self.counter.write_count()
        await ctx.send(f"The self.counter has been set to: {self.counter.count}")


    @commands.command(name='help')
    async def help(self, ctx, topic='overview'):
        if topic == 'overview':
            await ctx.send(
                f"/me @{ctx.author.name} See '!help <topic>' to learn about a specific topic."
                f" Available topics: self.sounds, self.counter, about")
        elif topic == 'sounds':
            await ctx.send(
                f'/me @{ctx.author.name} Available self.sound commands are: !alert !modem !objection'
                f' !oof !oooooof !steam !yeet !youdied')
        elif topic == 'counter':
            await ctx.send(
                f'/me @{ctx.author.name} Available self.counter commands are: !count (show current count) !increment (count + 1)'
                f' !decrement (count - 1) !reset (count = 0) !modify +/-n (count +/- n) !set n (counter = n)')
        elif topic == 'about':
            await ctx.send(
                "This bot was made by sn0wtime. For more information, check out the source code on Github:"
                " https://github.com/heckelson/b0ttime")
        else:
            pass


    @commands.command(name='dsmessage')
    async def dsmessage(self, ctx):
        message = self.dsmsg.randommsg()
        await ctx.send(f"/me {message}")
        if message == "Praise the Sun!":
            self.sound.play("sounds/praise.mp3")


if __name__ == "__main__":
    bot = Bot()
    bot.run()

