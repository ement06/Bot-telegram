from trash import (
    CURRENT_OFFSET_FILE,
    URL
)
import requests, mysql.connector, misc, random


class Update:
    def __init__(self, data):
        self.update_id = data.get("update_id", 0)
        self.chat_id = data.get("chat_id", None)
        self.text = data.get("text", None)
        self.user_id = data.get("user_id", None)
        self.first_name = data.get("first_name", None)
        self.last_name = data.get("last_name", None)

class MySQL_connection(Update):
    def __init__(self, chat_id):
        Update.__init__(self.chat_id)
        self.conn = mysql.connector.connect(
            host = '127.0.0.1',
            user = misc.user_db,
            passwd = misc.password_db,
            database = 'members'
        )
        self.my_cursor = self.conn.cursor()

    def select_pidor(self):
        self.sql = 'SELECT first_name, last_name FROM pidors WHERE chat_id = {}'.format(self.chat_id)

        self.my_cursor.execute(self.sql)
        return random.choice(self.my_cursor.fetchall())

connect = MySQL_connection()
print(connect.select_pidor())
