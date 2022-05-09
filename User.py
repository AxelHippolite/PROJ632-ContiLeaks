class User():
    def __init__(self, adress):
        """
        contructor of the class Users
        """
        self.onion = adress
        self.nb_links = 0
        self.received_from = []
        self.sent_to = []
    def addReceived(self, user):
        """
        adds the address of a user who sent a message to self
        """
        self.received_from.append(user)
        self.nb_links += 1
    def addSent(self, user):
        """
        adds the address of a user who received a message sent by self
        """
        self.sent_to.append(user)
        self.nb_links += 1