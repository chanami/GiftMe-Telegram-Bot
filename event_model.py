from pymongo.mongo_client import MongoClient


class Event:
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.events = self.db.get_collection("events")

    def create_new_list(self, chat_id):
        self.events.replace_one({"chat_id": chat_id}, {
            "chat_id": chat_id,
            "items": [],
        }, upsert=True)

    def add_item_to_list(self, chat_id, item):
        self.events.update_one({"chat_id": chat_id}, {"$push": {"items": item}})

    def get_doc(self, chat_id):
        return self.events.find_one({"chat_id": chat_id})

    def count_items(self, chat_id):
        doc = self.get_doc(chat_id)
        return len(doc['items'])

    def get_items(self, chat_id):
        doc = self.get_doc(chat_id)
        return doc['items']
