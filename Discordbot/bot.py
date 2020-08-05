import discord
import time
import asyncio


#id widget =667266163465519106

messages = joined = 0
dic = {"Levi#6138": 2, "Dic323" : 3}

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

async def update_start():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("start.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, memberJoined: {joined}\n")

                messages = 0
                joined = 0
                await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)

'''
@client.event
async def on_message(message):
    channels = ["chatbot"]

    if str(message.channel) in channels:
        id = client.get_guild(667266163465519106)
        if message.content.startswith("!Hey bot"):
            await message.channel.send("Hi there")
        elif message.content in "!users":
            await message.channel.send(f"""# of members {id.member_count}""")
'''
@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "genaral":
            await client.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(667266163465519106)
    channels = ["chatbot"]
    valid_users = ["le#6183"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        else:
            print(f"""User: {message.author} tried to say {message.content}, in channel: {message.channel}""")


client.loop.create_task(update_start())
client.run(token)
