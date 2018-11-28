import secret_settings
import settings

from event_model import Event
import datetime

now = datetime.datetime.now()
import requests


def check_event_dates():
    e = Event(settings.HOST, settings.TEST_DB)

    today = now.day
    events = e.get_all_events()
    for event in events:
        print(f"evens   {event}")
    for event in events:
        if today-event['date'] in [7, 2, 1, 0]:
            bot_message = f"friendly reminder its {event['full name']} {event['type']} in {today-event['date']} days"
            bot_send_notifications(bot_message)

def bot_send_notifications(bot_message):
    ### Send text message
    bot_token = secret_settings.BOT_TOKEN
    bot_chatID = '757815786'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)
def send_notifications():
    pass


bot_send_notifications("hello my friend")
check_event_dates()