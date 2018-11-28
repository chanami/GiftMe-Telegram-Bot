import secret_settings
import settings
import logging
import client
from help import Help
from client import Client

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
    client_t = Client(settings.HOST, settings.DB)
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")

    # full_name = update.message.text
    client_t.create_new_member(chat_id, text)

    # bot.send_message(chat_id=update.message.chat_id, text=response)

def help(bot, update):
    help_o = Help()
    message = help_o.get_explanation()
    bot.send_message(chat_id=update.message.chat_id, text=message)


def add_event(bot,update):
    message = "adding event to a friend :)"
    bot.send_message(chat_id=update.message.chat_id, text=message)
    message = "Please enter your friend name: "
    bot.send_message(chat_id=update.message.chat_id, text=message)

def show_upcoming_events(bot,update):
    pass
    

def add_friend(bot, update):
    client_t = Client(settings.HOST, settings.DB)
    chat_id = update.message.chat_id
    text = update.message.text
    client_t.add_friend_to_list(chat_id, text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

add_event_handler = CommandHandler('add_event', add_event)
dispatcher.add_handler(add_event_handler)

show_upcoming_events_handler = CommandHandler('show_upcomung_events', show_upcoming_events)
dispatcher.add_handler(show_upcoming_events_handler)

add_friend_handler = CommandHandler('add_friend', add_friend)
dispatcher.add_handler(add_friend_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()