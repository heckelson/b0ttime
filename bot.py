# bot.py
import os 
import sys

from twitchio.ext import commands
from pydub import AudioSegment
from pydub.playback import play


##### RESSOURCES: #########################################################
# Tutorial on how to make this bot:
# https://dev.to/ninjabunny9000/let-s-make-a-twitch-bot-with-python-2nd8
###########################################################################


# initial volume of the sound bits

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

# how loud the sound effects are going to play
volume = 10

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
    await ws.send_privmsg(os.environ['CHANNEL'], "/me successfully booted!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('/me Test successful')


@bot.command(name='kill')
async def kill(ctx):
    if ctx.author.is_mod:
        await ctx.send('/me Goodbye World!')
        sys.exit()
    else:
        return


@bot.command(name='sounds')
async def sounds(ctx):
    await ctx.send(f'@{ctx.author.name} Available sound commands are: !alert !modem !oof !oooooof !steam !yeet !youdied')


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




if __name__ == "__main__":
    bot.run()
