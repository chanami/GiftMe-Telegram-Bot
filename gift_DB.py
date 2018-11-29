from pymongo.mongo_client import MongoClient

class giftList():
    def __init__(self, host, db):
        self.client = MongoClient(host)
        self.db = self.client.get_database(db)
        self.gifts = self.db.get_collection("gifts")

    def add_gift(self, type, price, link):
        self.gifts.replace_one({"link": link}, {"type": type, "price":price, "link": link}, upsert=True)

    def get_gifts_by_cond(self, type, price):
        p = price.split()
        myRange = self.gifts.find({"type": type})
        #{"price": {"$gt": int(p[0]), "$lt": int(p[1])}})
        list = []
        for x in myRange:
            list.append(x)
        return list
