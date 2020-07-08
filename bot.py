# bot.py
import os 
import sys

from twitchio.ext import commands
from pydub import AudioSegment
from pydub.playback import play

from counter import Counter
from dsmessages import DSMessages


##### RESSOURCES: #########################################################
# Tutorial on how to make this bot:
# https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8
###########################################################################



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

# how loud the sound effects are going to play
volume = 7


def playsound(filename):
    if filename.endswith(".mp3"):
        sound = AudioSegment.from_mp3(filename) + volume
    elif filename.endswith(".wav"):
        sound = AudioSegment.from_file(filename) + volume
    else:
        return
    play(sound)


@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws 
    await ws.send_privmsg(os.environ['CHANNEL'], "/me successfully b00ted!")


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
    playsound("sounds/alert.mp3")


@bot.command(name='modem')
async def modem(ctx):
    await ctx.send('/me does not compute...')
    playsound("sounds/modem.mp3")


@bot.command(name='yeet')
async def yeet(ctx):
    await ctx.send('/me yeet')
    playsound("sounds/yeet.mp3")


@bot.command(name='oof')
async def oof(ctx):
    await ctx.send('/me oof')
    playsound("sounds/oof.mp3")


@bot.command(name='oooooof')
async def oooooof(ctx):
    await ctx.send('/me oooooof')
    playsound("sounds/oooooof.mp3")


@bot.command(name='youdied')
async def youdied(ctx):
    await ctx.send('/me YOU DIED')
    playsound("sounds/youdied.mp3")


@bot.command(name='steam')
async def steam(ctx):
    await ctx.send('/me got a new message')
    playsound('sounds/steam.mp3')


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
        await ctx.send(f"/me @{ctx.author.name} See '!help <topic>' to learn about a specific topic. Available topics: sounds, counter, about")
    elif topic == 'sounds':
        await ctx.send(f'/me @{ctx.author.name} Available sound commands are: !alert !modem !oof !oooooof !steam !yeet !youdied')
    elif topic == 'counter':
        await ctx.send(f'/me @{ctx.author.name} Available counter commands are: !count (show current count) !increment (count + 1) !decrement (count - 1) !reset (count = 0) !modify +/-n (count +/- n) !set n (counter = n)')
    elif topic == 'about':
        await ctx.send("This bot was made by sn0wtime. For more information, check out the source code on Github: https://github.com/heckelson/b0ttime")
    else:
        pass


@bot.command(name='dsmessage')
async def dsmessage(ctx):
    await ctx.send(f"/me {dsmsg.randommsg()}")


if __name__ == "__main__":
    bot.run()

