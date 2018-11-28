from pymongo.mongo_client import MongoClient


class Client:
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.lists = self.db.get_collection("Clients")

    def create_new_member(self, chat_id, full_name):
        self.lists.drop()
        self.lists.replace_one({"chat_id": chat_id}, {
            "chat_id": chat_id,
            "full name": full_name,
            "friends": [],
        }, upsert=True)

    def add_friend_to_list(self, chat_id, friend):
        self.lists.update_one({"chat_id": chat_id}, {"$push":{ "friends": friend}})

    def get_doc(self, chat_id):
        return self.lists.find_one({"chat_id": chat_id})

    def get_friend(self, chat_id):
        doc = self.get_doc(chat_id)
        return doc['friends']

    def delete_friend(self, chat_id, friend):
        self.lists.update({"chat_id": chat_id}, {"$pull": {'friends': friend}})