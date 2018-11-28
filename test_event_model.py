import event_model
import settings

def test_off():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    tester.events.drop()

def test_bulid_list():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    chat_id = 66613871638461
    full_name = "Tehila"
    #tester.create_new_list(chat_id)
    tester.add_event(chat_id, 'Chaya Cohen','01/01/1996', 'Birthday', False,'0548524490' )
    tester.add_event(chat_id, 'Tzippy Levi', '02/02/1997', 'Birthday', False, '0527156889',)
    tester.add_event(chat_id, 'Rachel Vagshal', '03/03/1998', 'Birthday', False, '0527156887')

