from pymongo.mongo_client import MongoClient


class Event:
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.events = self.db.get_collection("events")

    def add_event(self, client_id, full_name, date, type, mark, phone):
        self.events.insert_one({"client_id": client_id, "name":full_name, "date":date, "type":type, "mark":mark,"phone":phone})

    def delete_event(self, type, date):
        self.events.delete_one({"date":date, "type":type})

    def get_events_by_date(self, chat_id):
        return self.events.find_one({"date": chat_id})

    def get_events_by_name(self, name):
        return self.events.find_one({"name": name})

    def count_events(self, chat_id):
        doc = self.get_doc(chat_id)
        return len(doc['events'])

    def get_all_events(self, chat_id):
        doc = self.get_doc(chat_id)
        return doc['events']

