import discord
import openpyxl
client = discord.Client()


@client.event
async def on_ready():
        print(client.user.id)
        print("ready")
        game = discord.Game("dudogo이가 코딩")
        await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
        if message.content.startswith("안녕!"):
            await message.channel.send("반가워")

        if message.content.startswith("!채널메시지"):
            channel = message.content[7:25]
            msg = message.content[26:]
            await client.get_channel (int(channel)).send(msg)


client.run("NzIxMTI2NTU5NjAzMjI4Njgz.XuP_mg.-XW3cfaipvdKluEc4JGzpnOVtTA")