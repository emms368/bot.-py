import discord
from bot import gen_emodji, flip_coin, gen_pass, random_link

from bot_logic import *
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith("$link"):
        await message.channel.send(random_link())
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run("")       
