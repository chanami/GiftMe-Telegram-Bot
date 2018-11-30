import secret_settings
import settings
from event_model import Event
import datetime
import requests

def check_event_dates():
    print("here?????----")
    # e = Event(settings.HOST, settings.DB)
    # events = e.get_all_events()
    # for event in events:
    #     print(f"----event-----{event}")
    #     d0 = datetime.datetime.now()
    #     d1 = datetime.datetime(d0.year, event['date'].month, event['date'].day)
    #     delta = d1 - d0
    #     print(f"{delta.days}")
    #     if str(delta.days) in "7321":
    #         bot_message = f"Friendly Reminder its {event['name']} {event['type']} in {delta.days}" + (f"days" if delta.days > 1 else "day")
    #
    #     elif delta.days == 0:
    #         bot_message = f"Friendly Reminder its {event['name']} {event['type']}" +(" is TOMORROW" if delta.seconds/3600 > 0 else "TODAY")
    #     else:
    #         continue
    #     bot_send_notifications(bot_message,str(event['client_id']))
def send_notifications():
    pass

