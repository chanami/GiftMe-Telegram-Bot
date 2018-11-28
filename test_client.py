import client
import settings

def test_add_client():
    storage = client.Storage(settings.HOST, settings.TEST_DB)
    # chat_id = 87613871638461
    # storage.create_new_list(chat_id)
    # storage.add_item_to_list(chat_id, "milk")
    # storage.add_item_to_list(chat_id, "cookies")
    # storage.add_item_to_list(chat_id, "peanuts")
    # assert storage.count_items(chat_id) == 3
    # assert storage.get_items(chat_id) == ["milk", "cookies", "peanuts", ]
