import event_model
import settings


def test_bulid_list():
    tester = event_model.Event(settings.HOST, settings.TEST_DB)
    chat_id = 87613871638461
    tester.create_new_list(chat_id)
    tester.add_item_to_list(chat_id, {'first name': 'Sara', 'last Name': 'Cohen', })
    # tester.add_item_to_list(chat_id, "cookies")
    # tester.add_item_to_list(chat_id, "peanuts")
    assert 3 == 2
    #assert tester.count_items(chat_id) == 3
    #assert tester.get_items(chat_id) == ["milk", "cookies", "peanuts", ]

#test_bulid_list()