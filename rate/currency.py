# coding=utf-8
import requests
import json
import os
import datetime
from setting import mashape_key

file_name = 'currency_data.json'
pwd = os.path.dirname(__file__)
currency_dump = os.path.join(pwd, file_name)

url = "https://hryvna-today.p.mashape.com/v1/rates/today"
today_key = '840'

headers = {
    "X-Mashape-Key": mashape_key['X-Mashape-Key'],
    "Accept": "application/json"
  }
day = datetime.date.today().strftime('%d.%m.%Y')


class Currency(object):

    def get_set_currency(self):
        to_day = {'day': day}
        data = self._get_read_currency()

        if day not in data['day']:
            with open(currency_dump, 'w') as js_file:

                response = requests.get(url, headers=headers)
                pars_json = response.json()
                dict.update(pars_json, to_day)
                json.dump(pars_json, js_file, sort_keys=True, indent=4)

        return data

    @staticmethod
    def _get_read_currency():
        with open(currency_dump, 'r') as json_file:
            get_currency = json.load(json_file)

        return get_currency

    def select_currency(self, text):

        set_currency = self.get_set_currency()

        to_day_currency = set_currency['data'][today_key][text]

        actual_currency = []

        for key, value in to_day_currency.items():
            actual_currency.append((key, value['value']))

        return actual_currency
