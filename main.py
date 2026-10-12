from settings import settings
import discord
from discord.ext import commands
# import * - isso é o mesmo que listar todos os arquivos
from bot_logic import *

# Variáveis de intenção - armazena privilégios do bot
intents = discord.Intents.default()
# Habilita o privilégio de ler mensagens
intents.message_content = True
# Criamos um bot na variável do cliente e passamos todos os privilégios
bot = commands.Bot(command_prefix='$', intents=intents)


# client = discord.Client(intents=intents)
# # Quando o bot estiver pronto, ele escreverá seu nome no console!
# @client.event
# async def on_ready():
#     print(f'Fizemos login como {client.user}')


# # Quando o bot recebe uma mensagem, ele envia algumas mensagens para o mesmo canal!
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('Oi'):
#         await message.channel.send('Olá! Eu sou um bot')
#     elif message.content.startswith('Emoji'):
#         await message.channel.send(gen_emodji())
#     elif message.content.startswith('Moeda'):
#         await message.channel.send(flip_coin())
#     elif message.content.startswith('Tchau') or message.content.startswith('Flw'):
#         await message.channel.send("\U0001f642")
#     elif message.content.startswith('Senha'):
#         message.content.split()
#         pass_length = int(message.content.split()[1])
#         await message.channel.send(gen_pass(pass_length))
#     else:
#         await message.channel.send("Não entendo esse comandiu!")

# client.run(settings["TOKEN"])

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá eu sou um bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(settings["TOKEN"])
