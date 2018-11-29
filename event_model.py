from pymongo.mongo_client import MongoClient


class Event:
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.events = self.db.get_collection("events")

    def add_event(self, client_id, full_name, type, date, mark):
        self.events.insert_one({"client_id": client_id, "name":full_name, "type":type, "date":date, "mark":mark,})

    def delete_event(self, name, type, date):
        self.events.delete_one({"name": name, "type": type, "date": date})

    def get_events_by_date(self, date):
        myCursor =  self.events.find({"date": date})
        list = []
        for x in myCursor:
            list.append(x)
        return list

    def get_events_by_name(self, name):
        myCursor = self.events.find({"name": name})
        list = []
        for x in myCursor:
            list.append(x)
        return list

    def count_events(self):
        return self.events.count_documents({})

    def get_all_events(self):
        myCursor = self.events.find({})
        list = []
        for x in myCursor:
            list.append(x)
        return list

    def get_upcoming_events(self, start, end):
        myCursor = self.events.find({"date": {"$gt": start, "$lt": end } })
        list = []
        for x in myCursor:
            list.append(x)
        return list
