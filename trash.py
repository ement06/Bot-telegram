
# TODOs:
#  1) create new User class that will inherited an existing
# Update class with all required attributes

# 2) refactor all code below as a part of Update AND/OR User classes

import requests, mysql.connector, misc, random

token = misc.token
CURRENT_OFFSET_FILE = 'updates_id'
URL = "https://api.telegram.org/bot" + token + "/"

def send_message(chat_id, text = 'Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

# def insert_into_bd(id, first_name, last_name, chat_id, count_pidor=0):
#     mycursor.execute('SELECT id, chat_id FROM pidors;')
#     check = (id, chat_id)
#     not_found = True
#
#     for x in mycursor.fetchall():
#         if x == check:
#             not_found = False
#             break
#
#             if not_found:
#                 sql = "INSERT INTO pidors (id, first_name, last_name, chat_id, count_pidor) VALUES (%s, %s, %s, %s, %s)"
#                 val = (id, first_name, last_name, chat_id, count_pidor)
#                 mycursor.execute(sql, val)
#                 mydb.commit()
#             else:
#                 not_found = True
#                 send_message(chat_id, 'уже зарегався пидор!')
