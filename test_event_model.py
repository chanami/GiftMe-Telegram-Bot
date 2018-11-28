import datetime

import event_model
import settings

def test_off():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    tester.events.drop()

def test_bulid_list():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    chat_id = 66613871638461
    tester.add_event(chat_id, 'Sara Cohen',datetime.datetime(1996,11,29), 'Birthday', False,'0548524490' )
    tester.add_event(chat_id, 'Tzippy Levi', datetime.datetime(1996,2,1), 'Birthday', False, '0527156889',)
    tester.add_event(chat_id, 'Rachel Vagshal', datetime.datetime(1996,2,1), 'Anniversary', False, '0527156887')
    chat_id = 55555871638461
    tester.add_event(chat_id, 'Sara Cohen', datetime.datetime(1997,1,1), 'Anniversary', False, '0500024490')
    tester.add_event(chat_id, 'Malka Levi', datetime.datetime(1998,1,1), 'Anniversary', False, '0527159989', )
    tester.add_event(chat_id, 'Shira Vagshal', datetime.datetime(1996,1,5), 'Birthday', False, '0527444887')
    assert tester.count_events() == 6

def test_delete_event():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    tester.delete_event('Shira Vagshal','Birthday',datetime.datetime(1996,1,5))
    assert tester.count_events() == 5

def test_event_by_date():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    assert len(tester.get_events_by_date(datetime.datetime(1996,1,5))) == 0
    assert len(tester.get_events_by_date(datetime.datetime(1997,1,1))) == 1
    assert len(tester.get_events_by_date(datetime.datetime(1996,2,1))) == 2

def test_event_by_name():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    assert len(tester.get_events_by_name("Rut")) == 0
    assert len(tester.get_events_by_name("Malka Levi")) == 1
    assert len(tester.get_events_by_name("Sara Cohen")) == 2

def test_all_events():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    assert len(tester.get_all_events()) == 5

def test_upcoming_events():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    assert len(tester.get_upcoming_events(datetime.datetime(1990,1,5),datetime.datetime(1990,1,6))) == 0
    assert len(tester.get_upcoming_events(datetime.datetime(1990,1,5),datetime.datetime(1999,1,6))) == 5
    assert len(tester.get_upcoming_events(datetime.datetime(1996,3,5),datetime.datetime(1999,1,6))) == 3

