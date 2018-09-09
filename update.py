from trash import (
    CURRENT_OFFSET_FILE,
    URL, send_message, send_sticker, conn, my_cursor
)
import requests, random

class Update:

    def __init__(self, data):
        self.update_id = data.get("update_id", 0)
        self.chat_id = data.get("chat_id", None)
        self.text = data.get("text", None)
        self.user_id = data.get("user_id", None)
        self.first_name = data.get("first_name", None)
        self.last_name = data.get("last_name", None)

    def select_pidor(self, chat_id):
        my_cursor.execute('SELECT id, count FROM user_chat WHERE chat_id = {}'.format(self.chat_id))
        result = random.choice(my_cursor.fetchall())

        my_cursor.execute('SELECT first_name, last_name FROM users WHERE id = {}'.format(result[0]))
        pidor = my_cursor.fetchall()
        send_message(self.chat_id,  '{} - {} раз(а)'.format(' '.join(pidor[0]), result[1] + 1))
        sql = "UPDATE user_chat SET count = %s WHERE id = %s AND chat_id = %s"
        val = (result[-1] + 1, result[0], self.chat_id)
        my_cursor.execute(sql, val)
        conn.commit()

    def select_stiker(self, chat_id):
        my_cursor.execute('SELECT * FROM stickers')
        res = random.choice(my_cursor.fetchall())
        send_sticker(self.chat_id, res[0])

    def writting_into_db(self, user_id, first_name, last_name, chat_id):
        self.check = (self.user_id, self.chat_id)
        # checing and writind into users table
        my_cursor.execute('SELECT id FROM users;')
        for x0 in my_cursor.fetchall():
            if x0[0] == self.check[0]:
                break
        else:
            self.sql = "INSERT INTO users (id, first_name, last_name)VALUES (%s, %s, %s)"
            self.val = (self.user_id, self.first_name, self.last_name)
            my_cursor.execute(self.sql, self.val)
            conn.commit()
        # checing and writind into chats table
        my_cursor.execute('SELECT chat_id FROM chats;')
        for x1 in my_cursor.fetchall():
            if x1[0] == self.check[1]:
                break
        else:
            my_cursor.execute("INSERT INTO chats (chat_id)VALUES ({})".format(self.chat_id))
            conn.commit()
        # checing and writind into user_chat table
        my_cursor.execute('SELECT id, chat_id FROM user_chat;')
        for x in my_cursor.fetchall():
            if x == self.check:
                send_message(self.chat_id, 'уже зарегався, пидор!')
                break
        else:
            my_cursor.execute('INSERT INTO user_chat(id, chat_id) VALUES({}, {})'.format(self.user_id, self.chat_id))
            conn.commit()

    def parseTextField(self):
        if self.text == '/start@local_pidar_bot':
            self.writting_into_db(self.user_id, self.first_name, self.last_name, self.chat_id)
        if self.text == '/action@local_pidar_bot':
            self.select_pidor(self.chat_id)
            self.select_stiker(self.chat_id)

        with open(CURRENT_OFFSET_FILE, 'w') as f:
            f.write(str(self.update_id + 1))
