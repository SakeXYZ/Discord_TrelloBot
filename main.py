import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
main_trello_end_point = os.getenv('URL')
trello_key = os.getenv('API_KEY')
trello_token = os.getenv('TOKEN')
application_list_id = os.getenv('ID')

story_message = []
config = {"token": os.getenv('TOKEN_DISCORD'),
          "prefix": "!", }

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"{client.user.name} Bot is ready")


@client.command()
async def hello(ctx):
    await ctx.reply('Hello')
    await ctx.send("Hello")


try:
    # Функция для создания карточки Trello
    def create_trello_card(card_name, card_desc):
        create_card_end_point = main_trello_end_point + 'cards'
        json_object = {"key": trello_key,
                       "token": trello_token,
                       "idList": application_list_id,
                       "name": card_name,
                       "desc": card_desc}

        # Отправка запроса на создание карточки в Trello
        new_card = requests.post(create_card_end_point, json=json_object)
        return json.loads(new_card.text)
except Exception as SendToTrelloErr:
    # Обработка ошибки, если возникает проблема при отправке запроса в Trello
    print(f"Ошибка {SendToTrelloErr} при отправке запроса в Trello")


@client.command()
async def tch(ctx, *args):
    msg = ' '.join(args)
    list_accept = []
    for i in msg.split():
        list_accept.append(i)
    print(list_accept[0:2], list_accept[2::])
    # Создание карточки Trello на основе текста сообщения пользователя
    print(create_trello_card(' '.join(list_accept[0:2]), ' '.join(list_accept[2::])))
    await ctx.reply(msg)


client.run(config['token'])
