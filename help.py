class Help():
    def __init__(self):
        self.com = {'/add_friend': ' Adding a friend to the bot',
               '/add_event': 'Adding an event and linked to existing friend',
               '/update': 'update friend / event information',
               '/delete_friend': 'delete a friend',
               '/show_friends': ' show all friends of the member',
               '/delete_event': 'delete an event',
               '/show_upcoming_events': ' show upcoming events of this week'}
    def get_explanation(self):
        return self.com