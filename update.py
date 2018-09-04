from trash import (
    CURRENT_OFFSET_FILE,
    URL, send_message
)
import requests, mysql.connector, misc, random


class Update:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = misc.user_db,
        passwd = misc.password_db,
        database = 'members'
    )
    my_cursor = conn.cursor()
    def __init__(self, data):
        self.update_id = data.get("update_id", 0)
        self.chat_id = data.get("chat_id", None)
        self.text = data.get("text", None)
        self.user_id = data.get("user_id", None)
        self.first_name = data.get("first_name", None)
        self.last_name = data.get("last_name", None)

    def select_pidor(self, chat_id):
        self.sql = 'SELECT first_name, last_name FROM pidors WHERE chat_id = {}'.format(self.chat_id)

        self.my_cursor.execute(self.sql)
        return random.choice(self.my_cursor.fetchall())

    def writting_into_db(self, user_id, first_name, last_name, chat_id, count_pidor):
        self.my_cursor.execute('SELECT id, chat_id FROM pidors;')
        self.check = (self.user_id, self.chat_id)
        self.not_found = True

        for x in self.my_cursor.fetchall():
            if x == self.check:
                self.not_found = False
                break

            if self.not_found:
                self.sql = "INSERT INTO pidors (id, first_name, last_name, chat_id, count_pidor)VALUES (%s, %s, %s, %s, %s)"
                self.val = (self.user_id, self.first_name, self.last_name, self.chat_id, self.count_pidor)
                self.my_cursor.execute(self.sql, self.val)
                self.conn.commit()
            else:
                send_message(self.chat_id, 'уже зарегався пидор!')
                self.not_found = True

    def parseTextField(self):
        if self.text == '/start@local_pidar_bot':
            self.writting_into_db(self.user_id, self.first_name, self.last_name, self.chat_id, self.count_pidor)

        if self.text == '/action@local_pidar_bot':
            send_message(
                self.chat_id,
                ' '.join(self.select_pidor(self.chat_id))
            )
        # with open(CURRENT_OFFSET_FILE, 'w') as f:
        #     f.write(str(self.update_id + 1))
