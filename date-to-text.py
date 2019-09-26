#!/usr/bin/env python3

"""
  Автор: Мурашов Борис, группа №P3355

  Поскольку в исходной задаче ограничений на год не указано, то будем
  считать, что ограничения входных данных диктуются datetime
"""

from datetime import datetime



def generic_convert(tens, units, value):
    """Перевод десятков и единиц по значению в строковую форму

    tens  :: dict int string
    unit  :: dict int string
    value :: int

    FIXME: по хорошему эта функция должна быть приватной функцией
    классах TimeToTextClass и DateToTextClass ибо глобальное
    использование подобной функции не годится на роль библиотечной
    из-за ее специфичности именно для русского языка, но т.к:
    * меньше кода - меньше проблем
    * большая связность в задаче подобного размера роли не играет
    * если бы требовалось разработать общий интерфейс для всех языков,
    то архитектура была бы совершенно другой
    * подобный код крайне редко подвергается редактированию

    делаю вывод, что в данной реализации эта функция может находиться
    тут
    """
    def ten(value):
        return (value // 10) * 10

    def unit(value):
        return value % 10

    maybe_result = units.get(value)
    if maybe_result == None:
        return tens[ten(value)] + " " + units[unit(value)]
    else:
        return maybe_result

class TimeToTextClass:
    __hours_units = dict([
        (0, "ноль часов"),
        (1, "один час"),
        (2, "два часа"),
        (3, "три часа"),
        (4, "четыре часа"),
        (5, "пять часов"),
        (6, "шесть часов"),
        (7, "семь часов"),
        (8, "восемь часов"),
        (9, "девять часов"),
        (10, "десять часов"),
        (11, "одиннадцать часов"),
        (12, "двенадцать часов"),
        (13, "тринадцать часов"),
        (14, "четырнадцать часов"),
        (15, "пятнадцать часов"),
        (16, "шестнадцать часов"),
        (17, "семнадцать часов"),
        (18, "восемнадцать часов"),
        (19, "девятнадцать часов"),
        (20, "двадцать часов")
    ])

    __hours_tens = dict([
        (20, "двадцать")
    ])

    __minutes_units = dict([
        (0, "ноль минут"),
        (1, "одна минута"),
        (2, "две минуты"),
        (3, "три минуты"),
        (4, "четыре минуты"),
        (5, "пять минут"),
        (6, "шесть минут"),
        (7, "семь минут"),
        (8, "восемь минут"),
        (9, "девять минут"),

        (10, "десять минут"),
        (11, "одиннадцать минут"),
        (12, "двенадцать минут"),
        (13, "тринадцать минут"),
        (14, "четырнадцать минут"),
        (15, "пятнадцать минут"),
        (16, "шестнадцать минут"),
        (17, "семнадцать минут"),
        (18, "восемнадцать минут"),
        (19, "девятнадцать минут"),

        (20, "двадцать минут"),
        (30, "тридцать минут"),
        (40, "сорок минут"),
        (50, "пятьдесят минут")
    ])

    __minutes_tens = dict([
        (20, "двадцать"),
        (30, "тридцать"),
        (40, "сорок"),
        (50, "пятьдесят")
    ])

    __seconds_units = dict([
        (0, "ноль секунд"),
        (1, "одна секунда"),
        (2, "две секунды"),
        (3, "три секунды"),
        (4, "четыре секунды"),
        (5, "пять секунд"),
        (6, "шесть секунд"),
        (7, "семь секунд"),
        (8, "восемь секунд"),
        (9, "девять секунд"),

        (10, "десять секунд"),
        (11, "одиннадцать секунд"),
        (12, "двенадцать секунд"),
        (13, "тринадцать секунд"),
        (14, "четырнадцать секунд"),
        (15, "пятнадцать секунд"),
        (16, "шестнадцать секунд"),
        (17, "семнадцать секунд"),
        (18, "восемнадцать секунд"),
        (19, "девятнадцать секунд"),

        (20, "двадцать минут"),
        (30, "тридцать минут"),
        (40, "сорок минут"),
        (50, "пятьдесят минут")
    ])

    __seconds_tens = dict([
        (20, "двадцать"),
        (30, "тридцать"),
        (40, "сорок"),
        (50, "пятьдесят")
    ])

    __time = None

    def __init__(self, time):
        """
        time :: datetime
        """
        self.__time = time

    def convert(self):
        hours = generic_convert(self.__hours_tens, self.__hours_units, self.__time.hour)
        minutes = generic_convert(self.__minutes_tens, self.__minutes_units, self.__time.minute)
        seconds = generic_convert(self.__seconds_tens, self.__seconds_units, self.__time.second)

        return "{} {} {}".format(hours, minutes, seconds)

class DateToTextClass:
    __days_units = dict([
        (0, ""),
        (1, "первое"),
        (2, "второе"),
        (3, "третье"),
        (4, "четвертое"),
        (5, "пятое"),
        (6, "шестое"),
        (7, "седьмое"),
        (8, "восьмое"),
        (9, "девятое"),
        (10, "десятое"),
        (11, "одиннадцатое"),
        (12, "двенадцатое"),
        (13, "тринадцатое"),
        (14, "четырнадцатое"),
        (15, "пятнадцатое"),
        (16, "шестнадцатое"),
        (17, "семнадцатое"),
        (18, "восемнадцатое"),
        (19, "девятнадцатое"),
        (20, "двадцатое"),
        (30, "тридцатое")
    ])

    __days_tens = dict([
        (20, "двадцать"),
        (30, "тридцать")
    ])

    __months = [
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

    __thousands = [
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

    __hundreds = [
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

    __years_units = dict([
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

    __years_tens = dict([
        (20, "двацать"),
        (30, "тридцать"),
        (40, "сорок"),
        (50, "пятидесят"),
        (60, "шестидесят"),
        (70, "семидесят"),
        (80, "восьмидесят"),
        (90, "девяносто")
    ])

    __date = None

    def __init__(self, date):
        """
        date :: datetime
        """
        self.__date = date

    def __convert_year(self):
        def year_thousand(year):
            return year // 1000

        def year_hundred(year):
            return (year // 100) % 10

        def year_ten_and_unit(year):
            return year % 100

        year = self.__date.year

        thousands = self.__thousands[year_thousand(year)]
        hundreds = self.__hundreds[year_hundred(year)]
        tens_and_units = generic_convert(self.__years_tens, self.__years_units, year_ten_and_unit(year))

        words = [thousands, hundreds, tens_and_units]

        nonempty_words = filter(lambda x: len(x) > 0, words)

        return " ".join(nonempty_words)

    def convert(self):
        days = generic_convert(self.__days_tens, self.__days_units, self.__date.day)
        months = self.__months[self.__date.month]
        years = self.__convert_year()

        return  "{} {} {} года".format(days, months, years)

class DateTimeToTextClass:
    __DATETIME_FORMAT = "%d.%m.%Y %H:%M:%S"

    __datetime = None

    def __init__(self, datetime_string):
        """
        datetime_string :: string
        """
        self.__datetime = datetime.strptime(datetime_string, self.__DATETIME_FORMAT)

    def convert(self):
        date = DateToTextClass(self.__datetime).convert()
        time = TimeToTextClass(self.__datetime).convert()

        return "{} {}".format(date, time)

def assert_equal(actual, expected):
    assert actual == expected, "Assertion failed.\n"
    "Expected value: {}\n"
    "Actual value: {}".format(expected, actual)

def assert_exception(function, arg, expected_exception):
    try:
        eval(function)(arg),
    except Exception as e:
        actual_exception = type(e).__name__
        assert actual_exception == expected_exception, "Expected exception: {}\n"
        "Actual except: {}".format(expected_exception, actual_exception)

if __name__ == '__main__':
    """
    Тесты границ
    """
    assert_equal(
        DateTimeToTextClass('01.01.0001 00:00:00').convert(),
        "первое января первого года ноль часов ноль минут ноль секунд"
    )
    assert_equal(
        DateTimeToTextClass('31.12.9999 23:59:59').convert(),
        "тридцать первое декабря девять тысяч девятьсот девяносто девятого года двадцать три часа пятьдесят девять минут пятьдесят девять секунд"
    )
    """
    Тесты из условия задачи
    """
    assert_equal(
        DateTimeToTextClass('25.09.2019 08:17:59').convert(),
        "двадцать пятое сентября две тысячи девятнадцатого года восемь часов семнадцать минут пятьдесят девять секунд"
    )
    assert_equal(
        DateTimeToTextClass('06.10.1990 23:45:06').convert(),
        "шестое октября одна тысяча девятьсот девяностого года двадцать три часа сорок пять минут шесть секунд"
    )
    """
    Тесты обработки некорректного ввода данных
    """
    assert_exception(
        "DateTimeToTextClass", '25.09.0000 08:17:59',
        "ValueError"
    )
    assert_exception(
        "DateTimeToTextClass", '25.09.2019 25:17:59',
        "ValueError"
    )
    assert_exception(
        "DateTimeToTextClass", '25.09.10000 25:17:59',
        "ValueError"
    )
    print("All test cases passed")
