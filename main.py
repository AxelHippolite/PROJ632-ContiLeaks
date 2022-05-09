import mysql.connector
import pandas as pd
from data_getter import getMessagesUsers, getUsersData

def fill_db(sql, conn, cursor):
    """
    input: sql query, database, cursor MySQL
    output: None
    execute the SQL query and update the database with commit()
    """
    cursor.execute(sql)
    conn.commit()

if __name__ == '__main__':
    conn = mysql.connector.connect(user='dbu1699444 ', password='XXXXXXXXX', host='XXXXXXXXX', database='dbs6173339') #connexion to database
    cursor = conn.cursor() #cursor creation
    print("##### CountiLeaks - SocialGraph #####\n")
    print("Based on a leaked database of a Russian hacker group, \nthe following program fills a database with \nall the exchanges between the members of this group,\nthe final goal being to make a \"Social Graph\".")
    print("\nExtraction of all messages and tor addresses of group members from .json files...")
    messages, users, from_list, to_list = getMessagesUsers() #acquisition of all messages (sender and recipient), of all users and of all users having received and sent messages
    print("Calculation of additional data (number of messages received and sent, number of exchanges, etc)...")
    users = getUsersData(users, from_list, to_list) #calculation of additional data
    print("Filling the DataBase...")
    for i in messages: #filling the "messages" table
        sql = "INSERT INTO messages(`from`, `to`) VALUES(" + i[0] + ", " + i[1] + ")"
        fill_db(sql, conn, curson)
    for i in users: #filling the "users" table
        sql = "INSERT INTO users(`idUser`, `total`, `messages_sent`, `messages_received`) VALUES(" + i[0]+ ", " + str(i[1]) + ", " + str(i[2]) + ", " + str(i[3]) + ")"
        fill_db(sql, conn, curson)
    print("Acquisition Completed...")

    



