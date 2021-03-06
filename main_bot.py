# coding=utf-8
from setting import setting_bot
import requests
import datetime
from rate import currency


class BotHandler(object):

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=60):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()
        return result_json['result']

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update


greet_bot = BotHandler(setting_bot.get('bot_token'))
rate = ('avg', 'black', 'commercial', 'government', 'interbank')
get_currency = currency.Currency()
now = datetime.datetime.now()


def main():
    new_offset = None
    # today = now.day
    # hour = now.hour

    while True:
        print(greet_bot.get_updates(new_offset))

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        # last_chat_name = last_update['message']['chat']['first_name']
        greet_bot.send_message(last_chat_id,
                               'select your choice: avg, black, commercial, government, interbank')

        if last_chat_text.lower() in rate:
            correct = get_currency.select_currency
            for key, value in correct(last_chat_text.lower()):

                greet_bot.send_message(last_chat_id, '{} - {}'.format(key, value))

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
