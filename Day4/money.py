from functools import total_ordering
import requests
import json
from pprint import pprint

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data_dict = response.json()

@total_ordering
class Money:
    def __init__(self, rub, coins):
        self.r = rub
        self.c = coins

    def __str__(self):
        if self.c > 99:
            rub_ceil = int(str((self.c / 99)).split('.')[0])
            balance_coin = self.c % 99
            rub_sum = self.r + rub_ceil
            return f'{rub_sum} руб. {balance_coin} коп.'
        return f'{self.r} руб. {self.c} коп.'

    def __repr__(self):
        if self.c > 99:
            rub_ceil = int(str((self.c / 99)).split('.')[0])
            balance_coin = self.c % 99
            rub_sum = self.r + rub_ceil
#            return f'{rub_sum} руб. {balance_coin} коп.'
            return rub_sum + balance_coin / 100
#        return f'{self.r} руб. {self.c} коп.'
        return self.r + self.c / 100

    def __eq__(self, other):
        if self.r == other.r and self.c == other.c:
            return True

    def __lt__(self, other):
        return self.r < other.r

    def __add__(self, other):
        sum_rbls = int(self.r.__str__()) + int(other.r.__str__())
        sum_rbls_coins = int(self.c.__repr__()) + int(other.c.__repr__())
        return Money(sum_rbls, sum_rbls_coins)

    def __mod__(self, value):
        for_mod_rbls = self.__repr__()
        mod_rbls = for_mod_rbls * (value / 100)
        return round(mod_rbls)

    def convert(self, course_param):
        curse_value = data_dict['Valute'][course_param]['Value']
        nominal = data_dict['Valute'][course_param]['Nominal']
        if nominal > 1:
            min_cost = nominal / curse_value
            return min_cost * self.__repr__()
        rbls_to_other = self.__repr__() / curse_value
        return round(rbls_to_other, 2), f'{course_param}'

money1 = Money(4, 155)
money2 = Money(17, 1200)
mod_money = money1 % 21
print(money1)
print(mod_money)

print(money1.convert('UZS'))
