import os
import json
from User import User

def getMessagesUsers():
    """
    input: None
    output: list
    returns all messages (sender and recipient), all users and all users who have received and sent messages
    """
    gap = 6 #number of line between "from :" and "to :" lines
    from_list, to_list = [], []
    users = []
    """
    directory = 'assets' #block to uncomment if we want to extract all messages from all .json files
    count = 0            #it remains commented here because there are in all 8 million messages and thus hundreds of go of data
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
    """
    path = 'assets/185.25.51.173-20200622.json' #deleted this line and indented this block and the two for loops to browse all the .json files
    f = open(path, encoding='utf-8')
    lines = f.readlines()

    for i in range(2, len(lines), gap): #creation of the list containing all the users who sent messages
        from_list.append(lines[i].split('"from": "')[1][:-3])
        users.append(from_list[-1])

    for i in range(3, len(lines), gap): #creation of the list containing all the users who received messages
        to_list.append(lines[i].split('"to": "')[1][:-3])
        users.append(to_list[-1])

    messages = [[from_list[i], to_list[i]] for i in range(len(from_list))] #formatting of messages to facilitate insertion into the database

    f.close()
    
    return messages, list(set(users)), from_list, to_list #list(set(user)) returns the list of unique users

def getUsersData(users, from_list, to_list):
    """
    input: list
    output: list
    returns users, their interactions and additional data
    """
    users_list = []
    for i in users:
        users_list.append(User(i))

        for j in range(len(from_list)):
            if users_list[-1].onion == from_list[j]:
                users_list[-1].addSent(to_list[j])

        for j in range(len(to_list)):
            if users_list[-1].onion == to_list[j]:
                users_list[-1].addReceived(from_list[j])

    return [[i.onion, i.nb_links, len(i.sent_to), len(i.received_from)] for i in users_list]