import discord
from discord import app_commands
import asyncio

//WHAT YOU NEED TO CHANGE!!!
gids = [] //add your guild ID in here
ffmpegLoc = "" //set the location of ffmpeg.exe here
key = "KEY GOES HERE!!!!!"

//To add an extra sound, just follow the format here
sounds = {"joner":"Woodson_High_School.mp3", "ping":"ping.mp3", "heheheha":"heheheha.mp3", "cry":"huh", "yawn":"yawn.mp3", "wat da dog doin":"dog.mp3", "lick":"lick.mp3"}
names = list(sounds.keys())
soundLoc = ".\\sounds\\"

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=gids[0]))
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name="hee hee", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

@tree.command(name = "emote", description = "annoy them as much as possible", guild=discord.Object(id=gids[0]))
async def emote(ctx, emote: str):
        voice_channel = ctx.user.voice.channel
        channel = None
        if voice_channel != None and emote in names:
            await ctx.response.send_message(f"hahahahaha", ephemeral=True)
            channel = voice_channel.name
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable=ffmpegLoc, source=soundLoc + sounds[emote]))
            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()
        else:
            await ctx.respond(f"Try again. Make sure to be in a voice channel and choose an option given.", ephemeral=True)

@emote.autocomplete("emote")
async def fruits_autocomplete(interaction: discord.Interaction, current: str): 
    return [
        app_commands.Choice(name=emo, value=emo)
        for emo in names if current.lower() in emo
    ]

client.run(key)
