from random import randint


def game_core(number, start_range=0, last_range=100):
    '''Эта функция угадывает число с использованием алгоритма бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        middle_range = (last_range + start_range)// 2
        count += 1
        if number == middle_range or number == start_range or number == last_range:
            return count
        elif number > middle_range:
            start_range = middle_range
        elif number < middle_range:
            last_range = middle_range


def score_game(game):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    random_ls = [randint(0, 100) for i in range(1000)]
    for number in random_ls:
        count_ls.append(game(number))
    score = int(sum(count_ls) / len(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {} попыток".format(score))
    return


score_game(game_core)
