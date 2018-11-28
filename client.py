from pymongo.mongo_client import MongoClient


class Client:
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.lists = self.db.get_collection("friends")

    def create_new_member(self, chat_id):
        self.lists.replace_one({"chat_id": chat_id}, {
            "chat_id": chat_id,
            "full name": '',
            "friends": [],
        }, upsert=True)

    def add_friend_to_list(self, chat_id, full_name,  friend):
        self.lists.update_one({"chat_id": chat_id}, {"full_name": full_name}, {"$push": {"friends": friend}})

    def get_friends(self, chat_id):
        return self.db.collection.find({"friends"})

    def get_items(self, chat_id):
        doc = self.get_doc(chat_id)
        return doc['items']