import datetime
from functools import wraps
from time import sleep

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
import secret_settings
import settings
from event_model import Event
from help import Help
from client import Client
from telegram.ext import CommandHandler, CallbackQueryHandler
from gift_DB import giftList
from telegram import (LabeledPrice, ShippingOption)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, PreCheckoutQueryHandler, ShippingQueryHandler)
import logging

status = {"add_member": 0, "add_friend":  0, "add_event": 0, "send_gift": 0, "delete_event": 0,"delete_friend":  0}

some_event = []
delete = []
some_friend = []
logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)
updater = Updater(token=secret_settings.BOT_TOKEN)
dispatcher = updater.dispatcher

kind_present = ""

def send_action(action):
    """Sends `action` while processing func command."""
    def decorator(func):
        @wraps(func)
        def command_func(*args, **kwargs):
            bot, update = args
            bot.send_chat_action(chat_id=update.message.chat_id, action=action)
            func(bot, update, **kwargs)

        return command_func

    return decorator

@send_action(ChatAction.TYPING)
def typing(bot, update):
    sleep(2)


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
        return
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
    elif query.data == 'MESSAGE':
        logger.info(f"= Got on chat #{chat_id}: pressed {query.data} button")
        bot.send_message(chat_id=chat_id, text="Wish Card was sent to your friend!")

    else:
        print("start callback")  # start callback(query.data)
        start_shipping_callback(bot,update)


def start(bot, update):
    typing(bot, update)
    client_t = Client(settings.HOST, settings.DB)
    chat_id = update.message.chat_id
    logger.info(f"> Start chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="Hi And Welcome To Gift ME Bot!!!  😉😉 ")
    bot.send_message(chat_id=chat_id, text="Enter Your Full Name  👉 ")
    full_name = update.message.text
    status["add_member"] = 1
    client_t.create_new_member(chat_id, full_name)


def get_elements(kind_present, text):
    g = giftList(settings.HOST, settings.DB)
    return g.get_gifts_by_cond(kind_present, text)


def respond(bot, update):
    typing(bot, update)
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
    typing(bot, update)
    keyboard = [[InlineKeyboardButton("Send a Gift", callback_data='SEND A GIFT'),
                 InlineKeyboardButton("Send a Message", callback_data='SEND A MESSAGE')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.message.chat_id, text="what is your choice?",
                     reply_markup=reply_markup)


def choosing_gift(bot, update):
    typing(bot, update)
    query = update.callback_query
    chat_id = query.message.chat_id
    keyboard = [[InlineKeyboardButton("Flowers", callback_data='Flowers'),
                 InlineKeyboardButton("Balloons", callback_data='Balloons'),
                 InlineKeyboardButton("Chocolates", callback_data='Chocolates'),
                 InlineKeyboardButton("Surprise Gift", callback_data='Surprise_Gift')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text="what is your choice?", reply_markup=reply_markup)


def choosing_message(bot, update):
    typing(bot, update)
    query = update.callback_query
    chat_id = query.message.chat_id
    keyboard = [[InlineKeyboardButton("Happy Birthday!!!", callback_data='MESSAGE')],
                 [InlineKeyboardButton("Happy anniversary!!", callback_data='MESSAGE')],
                 [InlineKeyboardButton("Happy Valentine's Day!!", callback_data='MESSAGE')],
                 [InlineKeyboardButton("Congratulations!!!", callback_data='MESSAGE')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text="choose your wish 😍", reply_markup=reply_markup)


def price_range(bot, update):
    typing(bot, update)
    query = update.callback_query
    chat_id = query.message.chat_id
    keyboard = [[InlineKeyboardButton("20$ - 40$", callback_data='20 40'),
                 InlineKeyboardButton("40$ - 60$", callback_data='40 60'),
                 InlineKeyboardButton("60$ - 80$", callback_data='60 80'),
                 InlineKeyboardButton("80$ - 100$", callback_data='80 100'),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text="what is your choice?",
                     reply_markup=reply_markup)


def help(bot, update):
    typing(bot, update)
    help_o = Help()
    message = help_o.get_explanation()
    bot.send_message(chat_id=update.message.chat_id, text=message)


def send_notification(bot, update, current_event):
    typing(bot, update)
    event_date = current_event[3]
    d0 = datetime.datetime.now()
    d1 = datetime.datetime(d0.year, event_date.month, event_date.day)
    delta = d1 - d0
    if str(delta.days) in "7321":
        bot_message = f" ⚠ Friendly Reminder its {current_event[1]} {current_event[2]} in {delta.days}" + (
            f"days" if delta.days > 1 else "day")

    elif delta.days == 0:
        bot_message = f" ⚠ Friendly Reminder its {current_event[1]} {current_event[2]}" + (
            " is TOMORROW" if delta.seconds / 3600 > 0 else "TODAY")
    else:
        return

    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
    bot.sendDocument(chat_id=update.message.chat_id, document="https://media.giphy.com/media/6gT5hWNOZxkVq/giphy.gif")
    bot.send_message(chat_id=update.message.chat_id, text=bot_message)
    # e = Event(settings.HOST, settings.DB)
    # events = e.get_all_events()
    # for event in events:
    #     d0 = datetime.datetime.now()
    #     d1 = datetime.datetime(d0.year, event['date'].month, event['date'].day)
    #     delta = d1 - d0
    #     if str(delta.days) in "7321":
    #         bot_message = f"Friendly Reminder its {event['name']} {event['type']} in {delta.days}" + (
    #             f"days" if delta.days > 1 else "day")
    #
    #     elif delta.days == 0:
    #         bot_message = f"Friendly Reminder its {event['name']} {event['type']}" + (
    #             " is TOMORROW" if delta.seconds / 3600 > 0 else "TODAY")
    #     else:
    #         continue
    #     bot.send_message(chat_id=update.message.chat_id, text=bot_message)
    #     bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
    #     bot.sendDocument(chat_id=update.message.chat_id, document="https://media.giphy.com/media/6gT5hWNOZxkVq/giphy.gif")


def add_event(bot, update):
    typing(bot, update)
    global some_event

    if status["add_event"] == 0:
        status["add_event"] = 4
        message = "adding event to a friend 😉"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        message = "Please enter your friend's name: "
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_event"] -= 1
        some_event.append(update.message.chat_id)

    elif status["add_event"] == 3:
        name = update.message.text
        c = Client(settings.HOST, settings.DB)
        flag = False
        for friend in c.get_all_friends(update.message.chat_id):
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
            message = " 🤔 your friend doesn't exist in the list. add him by /add_friend"
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
        message = f"YAY you added an event to {some_event[1]} 😊"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        send_notification(bot, update, some_event)
        some_event = []
        status["add_event"] -= 1


def delete_event(bot, update):
    typing(bot, update)
    if status['delete_event'] == 0:
        message = "OH NO you are deleting an event 😧"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        message = "Enter your friend Name:"
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status['delete_event'] = 3

    elif status['delete_event'] == 3:
        status['delete_event'] -= 1
        e = Event(settings.HOST, settings.DB)
        ev = e.get_events_by_name(update.message.text)
        if len(ev) == 0:
            status['delete_event'] = 0
            message = "🤔 you friend does not have this event"
            bot.send_message(chat_id=update.message.chat_id, text=message)
            return
        delete.append(update.message.text)
        message = ""
        for event in ev:
            message += "=> {} on {}\n".format(event["type"], event["date"])
        message += "enter type event:"
        bot.send_message(chat_id=update.message.chat_id, text=message)

    elif status['delete_event'] == 2:
        status['delete_event'] -= 1
        type = update.message.text
        delete.append(type)
        message = "enter date of event:"
        bot.send_message(chat_id=update.message.chat_id, text=message)

    elif status['delete_event'] == 1:
        status['delete_event'] -= 1
        date = update.message.text
        date = date.split('/')
        date = [int(d) for d in date]
        date = datetime.datetime(*date)
        delete.append(date)
        e = Event(settings.HOST, settings.DB)
        e.delete_event(*delete)
        message = "Deleted :("
        bot.send_message(chat_id=update.message.chat_id, text=message)


def show_upcoming_events(bot, update):
    typing(bot, update)
    message = "Upcoming Events ➙ \n"
    e = Event(settings.HOST, settings.DB)
    events = e.get_all_events()
    upcoming_events = []
    for event in events:
        d0 = datetime.datetime.now()
        d1 = datetime.datetime(d0.year, event['date'].month, event['date'].day)
        delta = d1 - d0
        if delta.days < 10:
            upcoming_events.append(event)
    for u_event in upcoming_events:
        if delta.days == 0:
            message += f"{u_event['name']} {u_event['type']}" + (" is TOMORROW\n" if delta.seconds / 3600 > 0 else "TODAY\n")
        else:
            message += f"{u_event['name']} {u_event['type']} in {delta.days}" + (f"days\n" if delta.days > 1 else "day\n")

    bot.send_message(chat_id=update.message.chat_id, text=message)


def show_friends(bot, update):
    message = "All of Your Friends ➙ \n"
    c_model = Client(settings.HOST, settings.DB)
    friends = c_model.get_all_friends(update.message.chat_id)
    for f in friends:
        message += f"Name: {f['full_name']}, Address: {f['address']}\n"
    bot.send_message(chat_id=update.message.chat_id, text=message)


def delete_friend(bot, update):
    typing(bot, update)
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
    typing(bot, update)
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
        c = Client(settings.HOST, settings.DB)
        friend = {"full_name": some_friend[0], "address": some_friend[1]}
        c.add_friend_to_list(update.message.chat_id, friend)
        message = f"YAY you added an friend"
        some_friend = []
        bot.send_message(chat_id=update.message.chat_id, text=message)
        status["add_friend"] -= 1

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start_shipping_callback(bot, update):
    typing(bot, update)
    if update.callback_query.message:
        mes = update.callback_query.message
    else:
        mes = update.callback_query.edited_message

    msg = "Use /shipping to get an invoice for shipping-payment, "
    msg += "or /noshipping for an invoice without shipping."
    # update.message.reply_text(msg)
    bot.send_message(chat_id=mes.chat.id, text=msg)


def start_with_shipping_callback(bot, update):
    typing(bot, update)
    chat_id = update.message.chat_id
    title = "Payment Example"
    description = "Payment Example using python-telegram-bot"
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
    provider_token = "284685063:TEST:ODdmNGVkMzViZjYw"
    start_parameter = "test-payment"
    currency = "USD"
    # price in dollars
    price = 1
    # price * 100 so as to include 2 d.p.
    # check https://core.telegram.org/bots/payments#supported-currencies for more details
    prices = [LabeledPrice("Test", price * 100)]

    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    bot.sendInvoice(chat_id, title, description, payload,
                    provider_token, start_parameter, currency, prices,
                    need_name=True, need_phone_number=True,
                    need_email=True, need_shipping_address=True, is_flexible=True)


def start_without_shipping_callback(bot, update):
    chat_id = update.message.chat_id
    title = "Payment Example"
    description = "Payment Example using python-telegram-bot"
    # select a payload just for you to recognize its the donation from your bot
    payload = "Custom-Payload"
    # In order to get a provider_token see https://core.telegram.org/bots/payments#getting-a-token
    provider_token = "284685063:TEST:ODdmNGVkMzViZjYw"
    start_parameter = "test-payment"
    currency = "USD"
    # price in dollars
    price = 1
    # price * 100 so as to include 2 d.p.
    prices = [LabeledPrice("Test", price * 100)]

    # optionally pass need_name=True, need_phone_number=True,
    # need_email=True, need_shipping_address=True, is_flexible=True
    bot.sendInvoice(chat_id, title, description, payload,
                    provider_token, start_parameter, currency, prices)


def shipping_callback(bot, update):
    typing(bot, update)
    query = update.shipping_query
    # check the payload, is this from your bot?
    if query.invoice_payload != 'Custom-Payload':
        # answer False pre_checkout_query
        bot.answer_shipping_query(shipping_query_id=query.id, ok=False,
                                  error_message="Something went wrong...")
        return
    else:
        options = list()
        # a single LabeledPrice
        options.append(ShippingOption('1', 'Shipping Option A', [LabeledPrice('A', 100)]))
        # an array of LabeledPrice objects
        price_list = [LabeledPrice('B1', 150), LabeledPrice('B2', 200)]
        options.append(ShippingOption('2', 'Shipping Option B', price_list))
        bot.answer_shipping_query(shipping_query_id=query.id, ok=True,
                                  shipping_options=options)


# after (optional) shipping, it's the pre-checkout
def precheckout_callback(bot, update):
    query = update.pre_checkout_query
    # check the payload, is this from your bot?
    if query.invoice_payload != 'Custom-Payload':
        # answer False pre_checkout_query
        bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=False,
                                      error_message="Something went wrong...")
    else:
        bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)


# finally, after contacting to the payment provider...
def successful_payment_callback(bot, update):
    # do something after successful receive of payment?
    update.message.reply_text("Thank you for your payment!")


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

# Add command handler to start the payment invoice
dispatcher.add_handler(CommandHandler("shipping", start_with_shipping_callback))
dispatcher.add_handler(CommandHandler("noshipping", start_without_shipping_callback))

# Optional handler if your product requires shipping
dispatcher.add_handler(ShippingQueryHandler(shipping_callback))

# Pre-checkout handler to final check
dispatcher.add_handler(PreCheckoutQueryHandler(precheckout_callback))

# Success! Notify your user!
dispatcher.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))

# log all errors
dispatcher.add_error_handler(error)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()

updater.dispatcher.add_handler(CallbackQueryHandler(button))