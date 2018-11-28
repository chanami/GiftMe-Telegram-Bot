import secret_settings
import settings
import logging
import client

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater


logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)
updater = Updater(token=secret_settings.BOT_TOKEN)
dispatcher = updater.dispatcher


def start(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> Start chat #{chat_id}")

    bot.send_message(chat_id=chat_id, text="HI!!! Enter Your Full Name -- ")
    full_name = update.message.text
    client.Client.create_new_member(chat_id,full_name)

def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")

    response = "some..."

    if(text == "help"):
        response = help_function()
    bot.send_message(chat_id=update.message.chat_id, text=response)

def help_function():
    return help.Help.get_explanation()

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()