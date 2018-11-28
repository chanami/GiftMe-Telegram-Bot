class Help():
    def __init__(self):
        self.com = f'''  /add_friend:  Adding a friend to the bot\n
/add_event:  Adding an event and linked to existing friend\n
/update:  update friend / event information\n
/delete_friend:  delete a friend\n
/show_friends:  show all friends of the member\n
/delete_event:  delete an event\n
/show_upcoming_events:  show upcoming events of this week\n
/send_gift: Opening a gift selection'''
    def get_explanation(self):
        return self.com