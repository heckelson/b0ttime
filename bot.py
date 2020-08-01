# bot.py

import os
import sys

from twitchio.ext import commands

# 
from counter import Counter
from dsmessages import DSMessages
from sound import Sound

# RESSOURCES: #############################################################
# Tutorial on how to make this bot:
# https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8
###########################################################################

# TODO: ###################################################################
# * Refactor so that the bot doesn't show the message if the sound isn't
# played (maybe have the function return a boolean?)



# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

# set up a counter
counter = Counter()

# set up dark souls messages
dsmsg = DSMessages()

# set up sound cooldown (global)
sound = Sound()


# Bot events

@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    await bot.ws.send_privmsg(os.environ['CHANNEL'], "/me successfully b00ted!")


# Utility commands

@bot.command(name='test')
async def test(ctx):
    await ctx.send('/me Test successful!')


@bot.command(name='kill')
async def kill(ctx):
    if ctx.author.is_mod:
        await ctx.send('/me Goodbye World!')
        sys.exit()
    else:
        return


# Sound Commands

@bot.command(name='alert')
async def alert(ctx):
    await ctx.send('/me !')
    sound.play("sounds/alert.mp3")


@bot.command(name='modem')
async def modem(ctx):
    await ctx.send('/me does not compute...')
    sound.play("sounds/modem.mp3")


@bot.command(name='yeet')
async def yeet(ctx):
    await ctx.send('/me yeet')
    sound.play("sounds/yeet.mp3")


@bot.command(name='oof')
async def oof(ctx):
    await ctx.send('/me oof')
    sound.play("sounds/oof.mp3")


@bot.command(name='oooooof')
async def oooooof(ctx):
    await ctx.send('/me oooooof')
    sound.play("sounds/oooooof.mp3")


@bot.command(name='youdied')
async def youdied(ctx):
    await ctx.send('/me YOU DIED')
    sound.play("sounds/youdied.mp3")


@bot.command(name='steam')
async def steam(ctx):
    await ctx.send('/me got a new message')
    sound.play('sounds/steam.mp3')


@bot.command(name='objection')
async def objection(ctx):
    await ctx.send('/me OBJECTION!')
    sound.play('sounds/objection.mp3')


# Counter Commands

@bot.command(name='count')
async def count(ctx):
    await ctx.send(f"The counter is currently at: {counter.count}")


@bot.command(name='increment')
async def increment(ctx):
    counter.increment()
    counter.write_count()
    await ctx.send(f"The counter is now at: {counter.count}")


@bot.command(name='decrement')
async def decrement(ctx):
    counter.decrement()
    counter.write_count()
    await ctx.send(f"The counter is now at: {counter.count}")


@bot.command(name='reset')
async def reset(ctx):
    counter.reset()
    counter.write_count()
    await ctx.send("The counter has been reset (0).")


@bot.command(name="modify")
async def modify(ctx, modifier):
    counter.modify(modifier)
    counter.write_count()
    await ctx.send(f"The counter has been modified and is now at: {counter.count}")


@bot.command(name='set')
async def set(ctx, newval):
    counter.set(newval)
    counter.write_count()
    await ctx.send(f"The counter has been set to: {counter.count}")


@bot.command(name='help')
async def help(ctx, topic='overview'):
    if topic == 'overview':
        await ctx.send(
            f"/me @{ctx.author.name} See '!help <topic>' to learn about a specific topic."
            f" Available topics: sounds, counter, about")
    elif topic == 'sounds':
        await ctx.send(
            f'/me @{ctx.author.name} Available sound commands are: !alert !modem !objection'
            f' !oof !oooooof !steam !yeet !youdied')
    elif topic == 'counter':
        await ctx.send(
            f'/me @{ctx.author.name} Available counter commands are: !count (show current count) !increment (count + 1)'
            f' !decrement (count - 1) !reset (count = 0) !modify +/-n (count +/- n) !set n (counter = n)')
    elif topic == 'about':
        await ctx.send(
            "This bot was made by sn0wtime. For more information, check out the source code on Github:"
            " https://github.com/heckelson/b0ttime")
    else:
        pass


@bot.command(name='dsmessage')
async def dsmessage(ctx):
    message = dsmsg.randommsg()
    await ctx.send(f"/me {message}")
    if message == "Praise the Sun!":
        sound.play("sounds/praise.mp3")


if __name__ == "__main__":
    bot.run()

