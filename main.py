import os
import requests
import misc
import json
import mysql.connector
import random
from trash import CURRENT_OFFSET_FILE, URL
from update import Update

def get_updates(offset=0):
    if os.path.exists(CURRENT_OFFSET_FILE) and os.path.isfile(CURRENT_OFFSET_FILE):
        with open(CURRENT_OFFSET_FILE) as f:
            read_current_offset_id = f.read()
        if read_current_offset_id and read_current_offset_id.isdigit() and int(read_current_offset_id) > offset:
            offset = int(read_current_offset_id)
    url = URL + 'getupdates?offset={}'.format(offset)

    r = requests.get(url)
    data = r.json()
    if data['ok']:
        updates = list()
        for update in data['result']:
            updates.append(Update({
            "update_id": update['update_id'],
            "chat_id": update['message']['chat']['id'],
            "text": update['message']['text'],
            "user_id": update['message']['from']['id'],
            "first_name": update['message']['from']['first_name'],
            "last_name": update['message']['from']['last_name']
            }))
        return updates

def main():
    updates = get_updates()
    if not updates:
        print('Nothing to do!')
        return

    for update in updates:
        update.parseTextField()

if __name__ == '__main__':
    main()
