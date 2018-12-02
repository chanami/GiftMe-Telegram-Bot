from pymongo.mongo_client import MongoClient
from initial_gifts import initial


class giftList():
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.gifts = self.db.get_collection("gifts")
        initial()

    def add_gift(self, type, price, link):
        self.gifts.replace_one({"link": link}, {"type": type, "price": price, "link": link}, upsert=True)

    def get_gifts_by_cond(self, type, price):
        p = price.split()
        start = int(p[0])-1
        end = int(p[1])+1
        myRange = self.gifts.find({"type":type, "price": {"$gt": start, "$lt": end}})
        list = []
        for x in myRange:
            list.append(x)
        return list
