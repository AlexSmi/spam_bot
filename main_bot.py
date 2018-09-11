from setting import setting_bot
from base.hendler import BotHandler
import datetime
from rate import currency


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

        if not greet_bot.get_updates(new_offset):
            continue

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
