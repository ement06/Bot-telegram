
# TODOs:
#  1) create new User class that will inherited an existing
# Update class with all required attributes

# 2) refactor all code below as a part of Update AND/OR User classes

import requests, mysql.connector, misc, random

token = misc.token
CURRENT_OFFSET_FILE = 'updates_id'
URL = "https://api.telegram.org/bot" + token + "/"

conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = misc.user_db,
    passwd = misc.password_db,
    database = 'members'
)
my_cursor = conn.cursor()

def send_message(chat_id, text = 'Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def send_sticker(chat_id, sticker_id):
    url = URL + 'sendsticker?chat_id={}&sticker={}'.format(chat_id, sticker_id)
    requests.get(url)
