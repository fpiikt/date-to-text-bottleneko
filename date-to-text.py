#!/usr/bin/env python3

"""
  Автор: Мурашов Борис, группа №P3355
"""

from datetime import datetime


class DateToTextClass:
    __DATETIME_FORMAT = "%d.%m.%Y %H:%M:%S"

    days = [
        "",
        "первое",
        "второе",
        "третье",
        "четвертое",
        "пятое",
        "шестое",
        "седьмое",
        "восьмое",
        "девятое",
        "десятое",
        "одиннадцатое",
        "двенадцатое",
        "тринадцатое",
        "четырнадцатое",
        "пятнадцатое",
        "шестнадцатое",
        "семнадцатое",
        "восемнадцатое",
        "девятнадцатое",
        "двадцатое",
        "двадцать первое",
        "двадцать второе",
        "двадцать третье",
        "двадцать четвертое",
        "двадцать пятое",
        "двадцать шестое",
        "двадцать седьмое",
        "двадцать восьмое",
        "двадцать девятое",
        "тридцатое",
        "тридцать первое"
    ]

    months = [
        "",
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря"
    ]

    thousands = [
        "",
        "одна тысяча",
        "две тысячи",
        "три тысячи",
        "четыре тысячи",
        "пять тысяч",
        "шесть тысяч",
        "семь тысяч",
        "восемь тысяч",
        "девять тысяч"
    ]

    hundreds = [
        "",
        "сто",
        "двести",
        "триста",
        "четыреста",
        "пятьсот",
        "шестьсот",
        "семьсот",
        "восемьсот",
        "девятьсот"
    ]

    units = dict([
        (1, "первого"),
        (2, "второго"),
        (3, "третьего"),
        (4, "четвертого"),
        (5, "пятого"),
        (6, "шестого"),
        (7, "седьмого"),
        (8, "восьмого"),
        (9, "девятого"),
        (10, "десятого"),

        (11, "одиннадцатого"),
        (12, "двенадцатого"),
        (13, "тринадцатого"),
        (14, "четырнадцатого"),
        (15, "пятнадцатого"),
        (16, "шестнадцатого"),
        (17, "семнадцатого"),
        (18, "восемнадцатого"),
        (19, "девятнадцатого"),

        (20, "двацатого"),
        (30, "тридцатого"),
        (40, "сорокового"),
        (50, "пятидесятого"),
        (60, "шестидесятого"),
        (70, "семидесятого"),
        (80, "восьмидесятого"),
        (90, "девяностого")
    ])

    tens = dict([
        (20, "двацать"),
        (30, "тридцать"),
        (40, "сорок"),
        (50, "пятидесят"),
        (60, "шестидесят"),
        (70, "семидесят"),
        (80, "восьмидесят"),
        (90, "девяносто")
    ])

    datetime = None

    def __init__(self, datetime_string):
        self.datetime = datetime.strptime(datetime_string, self.__DATETIME_FORMAT)

    def __convert_year(self):
        def convert_tens_and_units():
            ten_or_unit = self.datetime.year % 100
            maybe_result = self.units.get(ten_or_unit)
            if maybe_result == None:
                return self.tens[(ten_or_unit // 10) * 10] + " " + self.units[ten_or_unit % 10]
            else:
                return maybe_result

        year = self.datetime.year
        words = [self.thousands[year // 1000], self.hundreds[(year // 100) % 10], convert_tens_and_units()]

        nonempty_words = filter(lambda x: len(x) > 0, words)

        return " ".join(nonempty_words)

    def __convert_date(self):
        return self.days[self.datetime.day] + " " + self.months[self.datetime.month] + " " + self.__convert_year() + " года"

    def __convert_time(self):
        raise NotImplemented

    def convert(self):
        return self.__convert_date()

def assert_equal(actual, expected):
    assert actual == expected, "Assertion failed.\nExpected value: {}\nActual value: {}".format(expected, actual)

if __name__ == '__main__':
    assert_equal(
        DateToTextClass('01.01.0001 00:00:00').convert(),
        "первое января первого года"
    )
    assert_equal(
        DateToTextClass('31.12.9999 23:59:59').convert(),
        "тридцать первое декабря девять тысяч девятьсот девяносто девятого года"
    )
    assert_equal(
        DateToTextClass('25.09.2019 08:17:59').convert(),
        "двадцать пятое сентября две тысячи девятнадцатого года"
    )
    assert_equal(
        DateToTextClass('06.10.1990 23:45:06').convert(),
        "шестое октября одна тысяча девятьсот девяностого года"
    )
    print("All test cases passed")
