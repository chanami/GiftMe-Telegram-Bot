import datetime

import requests
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import secret_settings
import settings
import logging
import notifications
from event_model import Event
from help import Help
from client import Client
from telegram.ext import CommandHandler, CallbackQueryHandler
from gift_DB import giftList
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater


status = {"add_member": 0, "add_friend":  0, "add_event": 0, "send_gift": 0, "delete_event": 0,"delete_friend":  0}

some_event = []

some_friend = []
logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)
updater = Updater(token=secret_settings.BOT_TOKEN)
dispatcher = updater.dispatcher

kind_present = ""
def button(bot, update):
    global kind_present
    query = update.callback_query
    chat_id = query.message.chat_id
    if query.data == 'SEND A GIFT':
        logger.info(f"= Got on chat #{chat_id}: pressed send a gift button")
        choosing_gift(bot, update)
    elif query.data == 'SEND A MESSAGE':
        logger.info(f"= Got on chat #{chat_id}: pressed send a message button")
        choosing_message(bot, update)
        pass
    elif query.data == 'Flowers':
        kind_present = 'Flowers'
        logger.info(f"= Got on chat #{chat_id}: pressed Flowers button")
        price_range(bot, update)
    elif query.data == 'Balloons':
        kind_present = 'Balloons'
        logger.info(f"= Got on chat #{chat_id}: pressed Balloons button")
        price_range(bot, update)
    elif query.data == 'Chocolates':
        kind_present = 'Chocolates'
        logger.info(f"= Got on chat #{chat_id}: pressed Chocolates button")
        price_range(bot, update)
    elif query.data == 'Surprise_Gift':
        kind_present = 'Surprise Gift'
        logger.info(f"= Got on chat #{chat_id}: pressed Surprise Gift button")
        price_range(bot, update)
    elif query.data == '20 40':
        logger.info(f"= Got on chat #{chat_id}: pressed {query.data} button")
        gif = get_elements(kind_present, query.data)
        for g in gif:
            link = g["link"]
            bot.send_photo(chat_id=chat_id, photo=link)
            keyboard = [[InlineKeyboardButton("Buy it now", callback_data=g["price"])]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=chat_id, text="what is your choice?",reply_markup=reply_markup)

    elif query.data == '40 60':
        logger.info(f"= Got on chat #{chat_id}: pressed {query.data} button")
        gif = get_elements(kind_present, query.data)
        for g in gif:
            link = g["link"]
            bot.send_photo(chat_id=chat_id, photo=link)
            keyboard = [[InlineKeyboardButton("Buy it now", callback_data=g["price"])]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=chat_id, text="what is your choice?",reply_markup=reply_markup)

    elif query.data == '60 80':
        logger.info(f"= Got on chat #{chat_id}: pressed {query.data} button")
        gif = get_elements(kind_present, query.data)
        for g in gif:
            link = g["link"]
            bot.send_photo(chat_id=chat_id, photo=link)
            keyboard = [[InlineKeyboardButton("Buy it now", callback_data=g["price"])]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=chat_id, text="what is your choice?",reply_markup=reply_markup)

    elif query.data == '80 100':
        logger.info(f"= Got on chat #{chat_id}: pressed {query.data} button")

        gif = get_elements(kind_present, query.data)
        for g in gif:
            link = g["link"]
            bot.send_photo(chat_id=chat_id, photo=link)
            keyboard = [[InlineKeyboardButton("Buy it now", callback_data=g["price"])]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=chat_id, text="what is your choice?",reply_markup=reply_markup)

    else:
        print("start callback") #start callback(query.data)

def start(bot, update):
    client_t = Client(settings.HOST, settings.DB)
    chat_id = update.message.chat_id
    logger.info(f"> Start chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="HI!!!")
    bot.send_message(chat_id=chat_id, text="Enter Your Full Name -- ")
    full_name = update.message.text
    status["add_member"] = 1
    client_t.create_new_member(chat_id, full_name)

def get_elements(kind_present, text):
    g = giftList(settings.HOST, settings.DB)
    return g.get_gifts_by_cond(kind_present, text)

def respond(bot, update):
    global kind_present
    text = update.message.text
    chat_id = update.message.chat_id

    if status["add_event"]:
        add_event(bot, update)

    elif status["delete_friend"]:
        status["delete_friend"] = 1
        delete_friend(bot, update)

    elif status['delete_event']:
        delete_event(bot, update)

    elif status["add_member"] == 1:
        name = update.message.text
        client_t = Client(settings.HOST, settings.DB)
        client_t.create_new_member(chat_id, name)
        status["add_member"] = 0

    elif status["add_friend"]:
        add_friend(bot, update)

    else:
        bot.send_message(chat_id=chat_id, text="you can add your friends by /add_friend and event by /add_event")

    logger.info(f"= Got on chat #{chat_id}: {text!r}")

def send_gift(bot, update):
    keyboard = [[InlineKeyboardButton("Send a Gift", callback_data='SEND A GIFT'),
                 InlineKeyboardButton("Send a Message", callback_data='SEND A MESSAGE')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.message.chat_id, text="what is your choice?",
                     reply_markup=reply_markup)

def choosing_gift(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    #[['Flowers', 'Balloons', 'Chocolates', 'Surprise Gift']]
    keyboard = [[InlineKeyboardButton("Flowers", callback_data='Flowers'),
                 InlineKeyboardButton("Balloons", callback_data='Balloons'),
                 InlineKeyboardButton("Chocolates", callback_data='Chocolates'),
                 InlineKeyboardButton("Surprise Gift", callback_data='Surprise_Gift')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text="what is your choice?", reply_markup=reply_markup)

def choosing_message(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    keyboard = [[InlineKeyboardButton("Happy Birthday!!!", callback_data='Flowers')],
                 [InlineKeyboardButton("Happy anniversary!!", callback_data='Balloons')],
                 [InlineKeyboardButton("Happy Valentine's Day!!", callback_data='Chocolates')],
                 [InlineKeyboardButton("Congratulations!!!", callback_data='Chocolates')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text="what is your choice?", reply_markup=reply_markup)

def price_range(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    # [[, '40$ - 60$', '60$ - 80$', '80$ - 100$']]
    keyboard = [[InlineKeyboardButton("20$ - 40$", callback_data='20 40'),
                 InlineKeyboardButton("40$ - 60$", callback_data='40 60'),
                 InlineKeyboardButton("60$ - 80$", callback_data='60 80'),
                 InlineKeyboardButton("80$ - 100$", callback_data='80 100'),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text="what is your choice?",
                     reply_markup=reply_markup)

def help(bot, update):
    help_o = Help()
    message = help_o.get_explanation()
    bot.send_message(chat_id=update.message.chat_id, text=message)

def send_notification(bot,update):
    e = Event(settings.HOST, settings.DB)
    events = e.get_all_events()
    for event in events:
        d0 = datetime.datetime.now()
        d1 = datetime.datetime(d0.year, event['date'].month, event['date'].day)
        delta = d1 - d0
        if str(delta.days) in "7321":
            bot_message = f"Friendly Reminder its {event['name']} {event['type']} in {delta.days}" + (
                f"days" if delta.days > 1 else "day")

        elif delta.days == 0:
            bot_message = f"Friendly Reminder its {event['name']} {event['type']}" + (
                " is TOMORROW" if delta.seconds / 3600 > 0 else "TODAY")
        else:
            continue
        bot.send_message(chat_id=update.message.chat_id, text=bot_message)
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
        bot.sendDocument(chat_id=update.message.chat_id, document="https://media.giphy.com/media/6gT5hWNOZxkVq/giphy.gif")

def add_event(bot, update):
    global some_event

    if status["add_event"] == 0:
        status["add_event"] = 4
        message = "adding event to a friend :)"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        message = "Please enter your friend's name: "
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_event"] -= 1
        some_event.append(update.message.chat_id)

    elif status["add_event"] == 3:
        name = update.message.text
        c = Client(settings.HOST, settings.DB)
        flag = False
        for friend in c.get_friends(update.message.chat_id):
            if friend['full_name'] == name:
                flag = True
        if flag:
            some_event.append(name)
            message = "Enter Event Type:"
            bot.send_message(chat_id=update.message.chat_id, text=message)
            status["add_event"] -= 1
        else:
            status["add_event"] = 0
            some_event = []
            message = "your friend doesn't exist in the list. add him by /add_friend"
            bot.send_message(chat_id=update.message.chat_id, text=message)

    elif status["add_event"] == 2:
        type = update.message.text
        some_event.append(type)
        message = "Enter event Date <yyyy/mm/dd>: "
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_event"] -= 1

    elif status["add_event"] == 1:
        date = update.message.text
        date = date.split('/')
        date = [int(d) for d in date]
        date = datetime.datetime(*date)
        some_event.append(date)
        some_event.append(False)
        e = Event(settings.HOST, settings.DB)
        e.add_event(*some_event)
        message = f"YAY you added an event to {some_event[1]}"
        some_event = []
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_event"] -= 1
        send_notification(bot,update)


def delete_event(bot, update):
    if status['delete_event'] == 0:
        message = "OH NO you are deleting an event :("
        bot.send_message(chat_id=update.message.chat_id, text=message)
        message = "Enter friend Name ??"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status['delete_event'] = 2

    elif status['delete_event'] == 2:
        status['delete_event'] -= 1
        e = Event(settings.HOST, settings.DB)
        ev = e.get_events_by_name(update.message.text)
        if len(ev) == 0:
            message = "you don't have such friend"
            bot.send_message(chat_id=update.message.chat_id, text=message)
            return
        message = ""
        for event in ev:
            print(event["type"])
            print(event["date"])
            message += "=> {} on {}\n".format(event["type"], event["date"])
        message += "enter type event:"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        ########not complete


def show_upcoming_events(bot, update):
    message = "Upcoming Events "
    e = Event(settings.HOST, settings.DB)
    events = e.get_all_events()
    upcoming_events = []
    for event in events:
        d0 = datetime.datetime.now()
        d1 = datetime.datetime(d0.year, event['date'].month, event['date'].day)
        delta = d1 - d0
        if delta.days < 10:
            upcoming_events.append(event)
    message += "\n".join(upcoming_events)
    bot.send_message(chat_id=update.message.chat_id, text=message)
    ###not completed


def show_friends(bot, update):
    message = "All of Your Friends\n"
    c_model = Client(settings.HOST, settings.DB)
    friends = c_model.get_friends(update.message.chat_id)
    for f in friends:
        message += f"Name: {f['full_name ']}, Address: {f['address']}\n"
    bot.send_message(chat_id=update.message.chat_id, text=message)


def delete_friend(bot, update):
    c_model = Client(settings.HOST, settings.DB)
    if status["delete_friend"] == 0:
        message = "Please enter the friend you wants to delete:"
        bot.send_message(chat_id=update.message.chat_id, text=message)
    elif status["delete_friend"] == 1:
        c_model.delete_friend(update.message.chat_id, update.message.text)
        print(update.message.text)
        message = "YES"
        bot.send_message(chat_id=update.message.chat_id, text=message)


def add_friend(bot, update):
    global some_friend
    if status["add_friend"] == 0:
        status["add_friend"] = 3
        message = "adding friend :)"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        message = "Please enter your friend's name: "
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_friend"] -= 1

    elif status["add_friend"] == 2:
        name = update.message.text
        some_friend.append(name)
        message = "Please enter your friend address:"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_friend"] -= 1

    elif status["add_friend"] == 1:
        address = update.message.text
        some_friend.append(address)
        # some_friend.append(False)
        c = Client(settings.HOST, settings.DB)
        friend = {"full_name": some_friend[0], "address": some_friend[1]}
        c.add_friend_to_list(update.message.chat_id, friend)
        message = f"YAY you added an friend"
        some_friend = []
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_friend"] -= 1


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

delete_friend_handler = CommandHandler('delete_friend', delete_friend)
dispatcher.add_handler(delete_friend_handler)

sand_gift_handler = CommandHandler('send_gift', send_gift)
dispatcher.add_handler(sand_gift_handler)


add_event_handler = CommandHandler('add_event', add_event)
dispatcher.add_handler(add_event_handler)

show_friends_handler = CommandHandler('show_friends', show_friends)
dispatcher.add_handler(show_friends_handler)

delete_event_handler = CommandHandler('delete_event', delete_event)
dispatcher.add_handler(delete_event_handler)

show_upcoming_events_handler = CommandHandler('show_upcoming_events', show_upcoming_events)
dispatcher.add_handler(show_upcoming_events_handler)

add_friend_handler = CommandHandler('add_friend', add_friend)
dispatcher.add_handler(add_friend_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()

updater.dispatcher.add_handler(CallbackQueryHandler(button))