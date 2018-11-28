import client
import settings


def test_add_client():
    new_client = client.Client(settings.HOST, settings.TEST_DB)
    chat_id = 87613871638461
    new_client.create_new_member(chat_id, {'full_name': 'Yael Yazdi'})
    new_client.add_friend_to_list(chat_id,  {'full_name': 'roy mak', "address": 'jerusalem'})
    new_client.add_friend_to_list(chat_id,  {"full_name": 'boris', "address": 'Tal Aviv'})
    new_client.add_friend_to_list(chat_id,  {"full_name": 'miki', "address": 'jerusalem'})
    new_client.get_friends(chat_id)
    new_client.delete_friend(chat_id, {"full_name": 'boris', "address": 'Tal Aviv'})

