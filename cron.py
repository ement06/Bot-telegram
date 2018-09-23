from trash import (
    send_message, send_sticker, conn, my_cursor
)
import requests, random

class Cron:

    def select_pidor(self, chat_id):
        my_cursor.execute('SELECT id, count FROM user_chat\
        WHERE chat_id = {}'.format(chat_id))
        result = random.choice(my_cursor.fetchall())

        my_cursor.execute('SELECT first_name, last_name FROM users\
        WHERE id = {}'.format(result[0]))
        pidor = my_cursor.fetchall()
        send_message(chat_id,  '{} - {} раз(а)'.format(' '.join(pidor[0]), result[1] + 1))
        sql = "UPDATE user_chat SET count = %s WHERE id = %s AND chat_id = %s"
        val = (result[-1] + 1, result[0], chat_id)
        my_cursor.execute(sql, val)
        conn.commit()

    def select_stiker(self, chat_id):
        my_cursor.execute('SELECT * FROM stickers')
        res = random.choice(my_cursor.fetchall())
        send_sticker(chat_id, res[0])

    def start(self):
        my_cursor.execute('SELECT chat_id FROM chats;')
        chats = my_cursor.fetchall()
        for chat in chats:
            my_cursor.execute('SELECT id FROM user_chat\
            WHERE chat_id={}'.format(chat[0]))
            res = my_cursor.fetchall()
            if len(res) >= 2:
                self.select_pidor(chat[0])
                self.select_stiker(chat[0])
