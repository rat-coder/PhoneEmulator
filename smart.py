import os
import random

global balance_bet
global balance2
global balance
balance = 0
balance2 = 0
balance_bet = 0


class SmartPhone:
    def __init__(self):
        self._serial_number = 654987
        global balance

    def version(self):
        print('v', 1.0)

    def call(self):
        try:
            a = str(input('Введите номер без +: '))
        except ValueError:
            print('Надо ввести числа!')
            return iphone.call()
        aa = list(a)
        num_el = len(aa)
        if num_el < 11:
            print('Неправильно набран номер!')
            return iphone.call()
        if num_el > 11:
            del aa[11:]
        aa = ''.join(aa)
        print('Звонок на номер +', aa, '\nПожалуйста подождите...')
        print('-----------------------')
        iphone.loading2()

    def calc(self):
        try:
            what = int(input('Сколько элементов будете считать(не больше 3): \n\n5 - Выход'))
        except ValueError:
            print('Надо ввести число!')
            return iphone.calc()
        if what == 2:
            try:
                num1 = int(input('Введите первое число: '))
                znak1 = input('Введите математический знак: ')
                num2 = int(input('Введите второе число: '))
            except ValueError:
                print('Надо ввести число!')
                return iphone.calc()
            res = 1
            if znak1 == '+':
                res = num1 + num2
            elif znak1 == '-':
                res = num1 - num2
            elif znak1 == '*':
                res = num1 * num2
            elif znak1 == '/':
                res = num1 / num2
            print('Ответ: ', res)
            print('-----------------------')
            iphone.loading2()

        elif what == 3:
            try:
                num1 = int(input('Введите первое число: '))
                znak1 = input('Введите математический знак: ')
                num2 = int(input('Введите второе число: '))
                znak2 = input('Введите математический знак: ')
                num3 = int(input('Введите третье число: '))
            except ValueError:
                print('Надо ввести число!')
                return iphone.calc()
            res = 1
            if znak1 == '+':
                if znak2 == '+':
                    res = num1 + num2 + num3
            elif znak1 == '-':
                if znak2 == '-':
                    res = num1 - num2 - num3
            elif znak1 == '*':
                if znak2 == '*':
                    res = num1 * num2 * num3
            elif znak1 == '/':
                if znak2 == '/':
                    res = num1 / num2 / num3
            elif znak1 == '+':
                if znak2 == '-':
                    res = num1 + num2 - num3
            elif znak1 == '+':
                if znak2 == '*':
                    res = num1 + num2 * num3
            elif znak1 == '+':
                if znak2 == '/':
                    res = num1 + num2 / num3
            elif znak1 == '-':
                if znak2 == '+':
                    res = num1 - num2 + num3
            elif znak1 == '-':
                if znak2 == '*':
                    res = num1 - num2 * num3
            elif znak1 == '-':
                if znak2 == '/':
                    res = num1 - num2 / num3
            elif znak1 == '*':
                if znak2 == '+':
                    res = num1 * num2 + num3
            elif znak1 == '*':
                if znak2 == '-':
                    res = num1 * num2 - num3
            elif znak1 == '*':
                if znak2 == '/':
                    res = num1 * num2 / num3
            elif znak1 == '/':
                if znak2 == '-':
                    res = num1 / num2 - num3
            elif znak1 == '/':
                if znak2 == '*':
                    res = num1 / num2 * num3
            elif znak1 == '/':
                if znak2 == '+':
                    res = num1 / num2 + num3

            print('Ответ: ', res)
        if what == 5:
            print('-----------------------')
            iphone.loading2()


class IPhone(SmartPhone):
    def loading(self):
        print('Loading...')
        print('Samsung')
        iphone.version()
        try:
            nm = int(input('Что вы хотите сделать?\n1 - Позвонить на номер  |6 - Баланс\n2 - Калькулятор         |7 - Работа с примерами\n3 - Блокнот             |8 - Tower\n4 - Игра - угадай число |9 - Скоро\n5 - Настройки           |10 - Скоро\nВыберите цифру: '))
        except ValueError:
            print('Надо ввести число!')
            return iphone.loading()

        if nm == 1:
            print('-----------------------')
            iphone.call()
        elif nm == 2:
            print('-----------------------')
            iphone.calc()
        elif nm == 3:
            print('-----------------------')
            iphone.notepad()
        elif nm == 4:
            print('-----------------------')
            iphone.playran()
        elif nm == 5:
            print('-----------------------')
            iphone.Settings()
        elif nm == 6:
            print('-----------------------')
            iphone.bal()
        elif nm == 7:
            print('-----------------------')
            iphone.work1()
        elif nm == 8:
            print('-----------------------')
            iphone.tower()

    def loading2(self):
        try:
            nm = int(input(
                'Что вы хотите сделать?\n1 - Позвонить на номер  |6 - Баланс\n2 - Калькулятор         |7 - Работа с примерами\n3 - Блокнот             |8 - Tower\n4 - Игра - угадай число |9 - Скоро\n5 - Настройки           |10 - Скоро\nВыберите цифру: '))
        except ValueError:
            print('Надо ввести число!')
            return iphone.loading2()
        if nm == 1:
            print('-----------------------')
            iphone.call()
        elif nm == 2:
            print('-----------------------')
            iphone.calc()
        elif nm == 3:
            print('-----------------------')
            iphone.notepad()
        elif nm == 4:
            print('-----------------------')
            iphone.playran()
        elif nm == 5:
            print('-----------------------')
            iphone.Settings()
        elif nm == 6:
            print('-----------------------')
            iphone.bal()
        elif nm == 7:
            print('-----------------------')
            iphone.work1()
        elif nm == 8:
            print('-----------------------')
            iphone.tower()

    def notepad(self):
        try:
            a = int(input(
                'Выберите действие: \n1 - Создать новый файл\n2 - Продолжить запись в существующем файле\n3 - Прочитать существующий файл\n4 - Удалить файл\n\n5 - Выход\n'))

        except ValueError:
            print('Надо ввести число!')
            return iphone.notepad()
        if a == 1:
            x = input('Назовите файл:')
            f = open(x + '.txt', 'w+', encoding='UTF-8')
            tax = input('Введите текст: ')
            f.write('{}'.format(tax))
            f.seek(0)
            f.close()
            print('В файле:', x, 'Записано:', tax)
            print('-----------------------')
            iphone.loading2()
        elif a == 2:
            xx = input('В каком файле хотите продолжить запись:')
            f = open(xx + '.txt', 'a+', encoding='UTF-8')
            taxx = input('Что вы хотите записать: ')
            f.write('{}\n'.format(taxx))
            f.seek(0)
            f.close()
            print('-----------------------')
            iphone.loading2()
        elif a == 3:
            xxx = input('Какой файл хотите прочитать:')
            f = open(xxx + '.txt', 'r', encoding='UTF-8')
            print(f.read())
            f.close()
            print('-----------------------')
            iphone.loading2()
        elif a == 4:
            xxxx = input('Какой файл хотите удалить:' + '.txt')
            xxxp = 'C:/Users/kpron/OneDrive/Рабочий стол/SmartPhone/' + xxxx
            if os.path.isfile(xxxp):
                os.remove(xxxp)
                print('Файл', xxxx, 'Успешно удален')
                print('-----------------------')
                iphone.loading2()
            else:
                print('Такого файла не существует')
                print('-----------------------')
                iphone.loading2()
        elif a == 5:
            print('-----------------------')
            iphone.loading2()

    def playran(self):
        global balance
        try:
            print(
                'Выберите уровень сложности:\n1 - от 1 до 10, награда 15 монет \n2 - от 1 до 15, награда 20 монет \n3 - от 1 до 20, награда 30 монет\n\n4 - Выход\n')
            print('---')
            a = int(input(' '))
            print('---')
        except ValueError:
            print('Надо ввести число!')
            return iphone.playran()
        if balance >= 1:
            if a == 1:
                balance -= 1
                iphone.bal2()
                try:
                    aa = int(input('Введите число от 1 до 10: '))
                except ValueError:
                    print('Надо ввести число!')
                x = random.randrange(1, 10)
                if aa == x:
                    balance += 15
                    iphone.bal2()
                    print('Вы угадали число!')
                    print('-----------------------')
                    iphone.playran()
                else:
                    print('Вы не угадали число( Загаданное число: ', x)
                    print('-----------------------')
                    iphone.playran()
        elif balance < 1:
            print('Вам не хватает средств(')
            print('-----------------------')
            return iphone.loading2()

        if balance >= 1:
            if a == 2:
                balance -= 1
                iphone.bal2()
                try:
                    aa = int(input('Введите число от 1 до 15: '))
                except ValueError:
                    print('Надо ввести число!')
                    return iphone.playran()
                x = random.randrange(1, 10)
                if aa == x:
                    balance += 20
                    iphone.bal2()
                    print('Вы угадали число!')
                    print('-----------------------')
                    iphone.playran()
                else:
                    print('Вы не угадали число( Загаданное число: ', x)
                    print('-----------------------')
                    iphone.playran()
        elif balance < 1:
            print('Вам не хватает средств(')
            print('-----------------------')
            return iphone.loading2()

        if balance >= 1:
            if a == 3:
                balance -= 1
                iphone.bal2()
                try:
                    aa = int(input('Введите число от 1 до 20: '))
                except ValueError:
                    print('Надо ввести число!')
                    return iphone.playran()
                x = random.randrange(1, 10)
                if aa == x:
                    balance += 30
                    iphone.bal2()
                    print('Вы угадали число!')
                    print('-----------------------')
                    iphone.playran()
                else:
                    print('Вы не угадали число( Загаданное число: ', x)
                    print('-----------------------')
                    iphone.playran()
            elif balance < 1:
                print('Вам не хватает средств(')
                print('-----------------------')
                return iphone.loading2()

            elif a == 4:
                print('-----------------------')
                iphone.loading2()

    def Settings(self):
        print('1 - Поменять цвет текста\n2 - Поменять фон текста\n3 - Эффекты\n4 - Сброс эффектов\n5 - Выход')
        try:
            a = int(input(' '))
            print('-----------------------')
        except ValueError:
            print('Надо ввести число!')
        if a == 1:
            print(
                'Выберите цвет: \n1 - Чёрный\n2 - Красный\n3 - Зелёный\n4 - Жёлтый\n5 - Синий\n6 - Фиолетовый\n7 - Бирюзовый\n8 - Белый')
            try:
                aa = int(input())
                print('-----------------------')
            except ValueError:
                print('Надо ввести число')
                print('-----------------------')
                iphone.Settings()
            if aa == 1:
                print('\033[30mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 2:
                print('\033[31mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 3:
                print('\033[32mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 4:
                print('\033[33mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 5:
                print('\033[34mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 6:
                print('\033[35mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 7:
                print('\033[36mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aa == 8:
                print('\033[37mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
        elif a == 2:
            print(
                'Выберите цвет: \n1 - Чёрный\n2 - Красный\n3 - Зелёный\n4 - Жёлтый\n5 - Синий\n6 - Фиолетовый\n7 - Бирюзовый\n8 - Белый')
            try:
                aaa = int(input())
                print('-----------------------')
            except ValueError:
                print('Надо ввести число')
                print('-----------------------')
                iphone.Settings()
            if aaa == 1:
                print('\033[40mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 2:
                print('\033[41mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 3:
                print('\033[42mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 4:
                print('\033[43mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 5:
                print('\033[44mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 6:
                print('\033[45mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 7:
                print('\033[46mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif aaa == 8:
                print('\033[47mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
        elif a == 3:
            print(
                'Выберите эффект: \n1 - Жирный\n2 - Блёклый\n3 - Курсив\n4 - Подчёркнутый\n5 - Редкое мигание\n6 - Частое мигание')
            try:
                eph = int(input())
                print('-----------------------')
            except ValueError:
                print('Надо ввести число')
                print('-----------------------')
                iphone.Settings()
            if eph == 1:
                print('\033[1mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif eph == 2:
                print('\033[2mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif eph == 3:
                print('\033[3mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif eph == 4:
                print('\033[4mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif eph == 5:
                print('\033[4mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
            elif eph == 6:
                print('\033[5mЦвет успешно изменен')
                print('-----------------------')
                iphone.loading2()
        elif a == 4:
            print('Эффекты успешно сброшены \033[32m{}\033[0m'.format('☑'))
            print('-----------------------')
            iphone.Settings()
        elif a == 5:
            print('-----------------------')
            iphone.loading2()

    def bal(self):
        global balance
        balance_list = []

        with open('wallet.txt', 'r') as file:
            for line in file:
                balance_list.append(line)

        balance = float(balance_list[0])
        balance_list[0] = float(balance)
        print('Ваш баланс: ', balance)
        file.close()
        print('-----------------------')

    def bal2(self):
        global balance
        global balance2
        balance_list = []

        with open('wallet.txt', 'r') as file:
            for line in file:
                balance_list.append(line)

        balance_list[0] = balance2
        balance = balance2 + balance


        if os.path.isfile('C:/Users/kpron/OneDrive/Рабочий стол/SmartPhone/wallet.txt'):
            os.remove('C:/Users/kpron/OneDrive/Рабочий стол/SmartPhone/wallet.txt')
        else:
            print('Ошибка')

        f = open('wallet.txt', 'w+', encoding='UTF-8')
        f.write('{}'.format(balance))
        f.seek(0)
        f.close()
    def work1(self):
        global balance
        print('Выбери уровень сложности:\n1 - Легко\n2 - Средне\n3 - Сложно\n\n4 - Выход\n')
        try:
            a = int(input())
        except ValueError:
            print('Надо ввести число!')
        if a == 1:
            ab = random.randrange(1, 3)
            if ab == 1:
                zn = '+'
            else:
                zn = '-'
            aa = random.randrange(1, 100)
            b = random.randrange(1, 100)
            if ab == 1:
                x = aa + b
            else:
                x = aa - b
            print(aa, zn, b, '= ')
            try:
                res = int(input('Ответ: '))
            except ValueError:
                print('Надо ввести число!')
                iphone.work1()
            if x == res:
                if aa >= 50 or b >= 50:
                    print('Правильно! Вы заработали 2 монеты')
                    balance += 2
                    iphone.bal2()
                    iphone.loading2()
                else:
                    print('Правильно! Вы заработали 1 монету')
                    balance += 1
                    iphone.bal2()
                    iphone.loading2()
            else:
                print('Неправильно! Ответ: ', x)
                iphone.loading2()

        elif a == 2:
            ab2 = random.randrange(1, 3)
            abb2 = random.randrange(1, 3)
            if ab2 == 1:
                zn = '+'
            else:
                zn = '-'
            if abb2 == 1:
                zn1 = '+'
            else:
                zn1 = '-'
            aa = random.randrange(1, 100)
            b = random.randrange(1, 100)
            bb = random.randrange(1, 100)
            if ab2 == 1:
                if abb2 == 1:
                    x = aa + b + bb
            elif ab2 > 1:
                if abb2 > 1:
                    x = aa - b - bb
            if ab2 == 1:
                if abb2 > 1:
                    x = aa + b - bb
            elif ab2 > 1:
                if abb2 == 1:
                    x = aa - b + bb
            print(aa, zn, b, zn1, bb, '= ')
            try:
                res = int(input('Ответ: '))
            except ValueError:
                print('Надо ввести число!')
                iphone.work1()
            if x == res:
                if aa >= 50 or b >= 50 or bb >= 50:
                    print('Правильно! Вы заработали 4 монеты')
                    balance += 4
                    iphone.bal2()
                    iphone.loading2()
                else:
                    print('Правильно! Вы заработали 3 монеты')
                    balance += 3
                    iphone.bal2()
                    iphone.loading2()
            else:
                print('Неправильно! Ответ: ', x)
                iphone.loading2()

        elif a == 3:
            ab2 = random.randrange(1, 3)
            abb2 = random.randrange(1, 3)
            if ab2 == 1:
                zn = '*'
            else:
                zn = '/'
            if abb2 == 1:
                zn1 = '*'
            else:
                zn1 = '/'
            aa = random.randrange(1, 100)
            b = random.randrange(1, 100)
            bb = random.randrange(1, 100)
            if ab2 == 1:
                if abb2 == 1:
                    x = aa * b * bb
            elif ab2 > 1:
                if abb2 > 1:
                    x = aa / b / bb
            if ab2 == 1:
                if abb2 > 1:
                    x = aa * b / bb
            elif ab2 > 1:
                if abb2 == 1:
                    x = aa / b * bb
            print(aa, zn, b, zn1, bb, '= ')
            try:
                res = int(input('Ответ: '))
            except ValueError:
                print('Надо ввести число!')
                iphone.work1()
            if x == res:
                if aa >= 50 or b >= 50 or bb >= 50:
                    print('Правильно! Вы заработали 7 монет')
                    balance += 7
                    iphone.bal2()
                    iphone.loading2()
                else:
                    print('Правильно! Вы заработали 6 монет')
                    balance += 6
                    iphone.bal2()
                    iphone.loading2()
            else:
                print('Неправильно! Ответ: ', x)
                iphone.loading2()
        elif a == 4:
            iphone.loading2()

    def tower(self):
        global balance
        global balance2
        global balance_bet
        what0 = ('Введи 0 1 2 или 3')
        what = ('? ? ? ?')
        easy = ['-', '+', '+', '+']
        medium = ['-', '-', '+', '+']
        hard = ['-', '-', '-', '+']
        print('Выберите сложность:\n1 - Легкая 3 правильных из 4\n2 - Средняя 2 правильных из 4\n3 - Сложно 1 правильный из 4\n4 - Выход')
        try:
            diff = int(input())
        except ValueError:
            print('Надо ввести число!')



        if diff == 1: # Lvl 1
            try:
                bet = float(input('Введите сумму ставки: '))
            except ValueError:
                print('Надо ввести число!')
            if balance >= bet:
                balance -= bet
                iphone.bal2()
                balance_bet += bet
                print(what0)
                print(what)
                try:
                    x = int(input())
                except ValueError or IndexError:
                    print('Введи 1 2 3 или 4')
                easy_rand = random.shuffle(easy)
                print(easy[x])
                if easy[x] == '+':
                    balance_bet *= 1.2
                    print('-----------------------')
                    print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                    try:
                        answer = int(input())
                    except ValueError:
                        print('Надо ввести число!')
                    if answer == 1: # Lvl 2
                        print('-----------------------')
                        easy1 = ('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                        print(what0)
                        print('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                        print(what)
                        try:
                            x = int(input())
                        except ValueError or IndexError:
                            print('Введи 1 2 3 или 4')
                        easy_rand = random.shuffle(easy)
                        print(easy[x])
                        if easy[x] == '+':
                            balance_bet *= 1.3
                            print('-----------------------')
                            print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                            try:
                                answer = int(input())
                            except ValueError:
                                print('Надо ввести число!')
                            if answer == 1: # Lvl 3
                                print('-----------------------')
                                easy2 = ('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                print(what0)
                                print(easy1)
                                print('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                print(what)
                                try:
                                    x = int(input())
                                except ValueError or IndexError:
                                    print('Введи 1 2 3 или 4')
                                easy_rand = random.shuffle(easy)
                                print(easy[x])
                                if easy[x] == '+':
                                    balance_bet *= 1.5
                                    print('-----------------------')
                                    print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                                    try:
                                        answer = int(input())
                                    except ValueError:
                                        print('Надо ввести число!')
                                    if answer == 1: # Lvl 4
                                        print('-----------------------')
                                        easy3 = ('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                        print(what0)
                                        print(easy1)
                                        print(easy2)
                                        print('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                        print(what)
                                        try:
                                            x = int(input())
                                        except ValueError or IndexError:
                                            print('Введи 1 2 3 или 4')
                                        easy_rand = random.shuffle(easy)
                                        print(easy[x])
                                        if easy[x] == '+':
                                            balance_bet *= 1.7
                                            print('-----------------------')
                                            print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                                            try:
                                                answer = int(input())
                                            except ValueError:
                                                print('Надо ввести число!')
                                            if answer == 1: # Lvl 5
                                                print('-----------------------')
                                                easy4 = ('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                                print(what0)
                                                print(easy1)
                                                print(easy2)
                                                print(easy3)
                                                print('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                                print(what)
                                                try:
                                                    x = int(input())
                                                except ValueError or IndexError:
                                                    print('Введи 1 2 3 или 4')
                                                easy_rand = random.shuffle(easy)
                                                print(easy[x])
                                                if easy[x] == '+':
                                                    balance_bet *= 2
                                                    print('-----------------------')
                                                    print('У вас хорошая интуиция, вы прошли игру!')
                                                    print(easy1)
                                                    print(easy2)
                                                    print(easy3)
                                                    print(easy4)
                                                    print('{} {} {} {}'.format(easy[0], easy[1], easy[2], easy[3]))
                                                    balance += balance_bet
                                                    iphone.bal2()
                                                    print('Ваш баланс = ', balance_bet)
                                                    balance_bet = 0
                                                    print('-----------------------')
                                                    iphone.tower()
                                            else:
                                                balance += balance_bet
                                                iphone.bal2()
                                                print('Вот ваш выигрышь = ', balance_bet)
                                                balance_bet = 0
                                                print('-----------------------')
                                                iphone.tower()
                                        else:
                                            print('Вы проиграли!')
                                            balance_bet = 0
                                            print('-----------------------')
                                            iphone.tower()
                                    else:
                                        balance += balance_bet
                                        iphone.bal2()
                                        print('Вот ваш выигрышь = ', balance_bet)
                                        balance_bet = 0
                                        print('-----------------------')
                                        iphone.tower()
                                else:
                                    print('Вы проиграли!')
                                    balance_bet = 0
                                    print('-----------------------')
                                    iphone.tower()
                            else:
                                balance += balance_bet
                                iphone.bal2()
                                print('Вот ваш выигрышь = ', balance_bet)
                                balance_bet = 0
                                print('-----------------------')
                                iphone.tower()
                        else:
                            print('Вы проиграли!')
                            balance_bet = 0
                            print('-----------------------')
                            iphone.tower()
                    else:
                        balance += balance_bet
                        iphone.bal2()
                        print('Вот ваш выигрышь = ', balance_bet)
                        balance_bet = 0
                        print('-----------------------')
                        iphone.tower()
                else:
                    print('Вы проиграли!')
                    balance_bet = 0
                    print('-----------------------')
                    iphone.tower()
            else:
                print('Недостаточно средств')
                print('-----------------------')
                iphone.loading2()
        elif diff == 2:
            try:
                bet = float(input('Введите сумму ставки: '))
            except ValueError:
                print('Надо ввести число!')
            if balance >= bet:
                balance -= bet
                iphone.bal2()
                balance_bet += bet
                print(what0)
                print(what)
                try:
                    x = int(input())
                except ValueError or IndexError:
                    print('Введи 1 2 3 или 4')
                medium_rand = random.shuffle(medium)

                print(medium[x])
                if medium[x] == '+':
                    balance_bet *= 1.4
                    print('-----------------------')
                    print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                    try:
                        answer = int(input())
                    except ValueError:
                        print('Надо ввести число!')
                    if answer == 1: # Lvl 2
                        print('-----------------------')
                        medium1 = ('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                        print(what0)
                        print('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                        print(what)
                        try:
                            x = int(input())
                        except ValueError or IndexError:
                            print('Введи 1 2 3 или 4')
                        medium_rand = random.shuffle(medium)
                        print(medium[x])
                        if medium[x] == '+':
                            balance_bet *= 1.7
                            print('-----------------------')
                            print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                            try:
                                answer = int(input())
                            except ValueError:
                                print('Надо ввести число!')
                            if answer == 1: # Lvl 3
                                print('-----------------------')
                                medium2 = ('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                print(what0)
                                print(medium1)
                                print('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                print(what)
                                try:
                                    x = int(input())
                                except ValueError or IndexError:
                                    print('Введи 1 2 3 или 4')
                                medium_rand = random.shuffle(medium)
                                print(medium[x])
                                if medium[x] == '+':
                                    balance_bet *= 2.1
                                    print('-----------------------')
                                    print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                                    try:
                                        answer = int(input())
                                    except ValueError:
                                        print('Надо ввести число!')
                                    if answer == 1: # Lvl 4
                                        print('-----------------------')
                                        medium3 = ('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                        print(what0)
                                        print(medium1)
                                        print(medium2)
                                        print('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                        print(what)
                                        try:
                                            x = int(input())
                                        except ValueError or IndexError:
                                            print('Введи 1 2 3 или 4')
                                        medium_rand = random.shuffle(medium)
                                        print(medium[x])
                                        if medium[x] == '+':
                                            balance_bet *= 3.5
                                            print('-----------------------')
                                            print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                                            try:
                                                answer = int(input())
                                            except ValueError:
                                                print('Надо ввести число!')
                                            if answer == 1: # Lvl 5
                                                print('-----------------------')
                                                medium4 = ('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                                print(what0)
                                                print(medium1)
                                                print(medium2)
                                                print(medium3)
                                                print('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                                print(what)
                                                try:
                                                    x = int(input())
                                                except ValueError or IndexError:
                                                    print('Введи 1 2 3 или 4')
                                                medium_rand = random.shuffle(medium)
                                                print(medium[x])
                                                if medium[x] == '+':
                                                    balance_bet *= 4.2
                                                    print('-----------------------')
                                                    print('У вас хорошая интуиция, вы прошли игру!')
                                                    print(medium1)
                                                    print(medium2)
                                                    print(medium3)
                                                    print(medium4)
                                                    print('{} {} {} {}'.format(medium[0], medium[1], medium[2], medium[3]))
                                                    balance += balance_bet
                                                    iphone.bal2()
                                                    print('Ваш баланс = ', balance_bet)
                                                    balance_bet = 0
                                                    print('-----------------------')
                                                    iphone.tower()
                                            else:
                                                balance += balance_bet
                                                iphone.bal2()
                                                print('Вот ваш выигрышь = ', balance_bet)
                                                balance_bet = 0
                                                print('-----------------------')
                                                iphone.tower()
                                        else:
                                            print('Вы проиграли!')
                                            balance_bet = 0
                                            print('-----------------------')
                                            iphone.tower()
                                    else:
                                        balance += balance_bet
                                        iphone.bal2()
                                        print('Вот ваш выигрышь = ', balance_bet)
                                        balance_bet = 0
                                        print('-----------------------')
                                        iphone.tower()
                                else:
                                    print('Вы проиграли!')
                                    balance_bet = 0
                                    print('-----------------------')
                                    iphone.tower()
                            else:
                                balance += balance_bet
                                iphone.bal2()
                                print('Вот ваш выигрышь = ', balance_bet)
                                balance_bet = 0
                                print('-----------------------')
                                iphone.tower()
                        else:
                            print('Вы проиграли!')
                            balance_bet = 0
                            print('-----------------------')
                            iphone.tower()
                    else:
                        balance += balance_bet
                        iphone.bal2()
                        print('Вот ваш выигрышь = ', balance_bet)
                        balance_bet = 0
                        print('-----------------------')
                        iphone.tower()
                else:
                    print('Вы проиграли!')
                    balance_bet = 0
                    print('-----------------------')
                    iphone.tower()
            else:
                print('Недостаточно средств!')
                print('-----------------------')
                iphone.loading2()
        elif diff == 3:
            try:
                bet = float(input('Введите сумму ставки: '))
            except ValueError:
                print('Надо ввести число!')
            if balance >= bet:
                balance -= bet
                iphone.bal2()
                balance_bet += bet
                print(what0)
                print(what)
                try:
                    x = int(input())
                except ValueError or IndexError:
                    print('Введи 1 2 3 или 4')
                hard_rand = random.shuffle(hard)
                print(hard[x])
                if hard[x] == '+':
                    balance_bet *= 1.8
                    print('-----------------------')
                    print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                    try:
                        answer = int(input())
                    except ValueError or IndexError:
                        print('Надо ввести число!')
                    if answer == 1: # Lvl 2
                        print('-----------------------')
                        hard1 = ('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                        print(what0)
                        print('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                        print(what)
                        try:
                            x = int(input())
                        except ValueError or IndexError:
                            print('Введи 1 2 3 или 4')
                        hard_rand = random.shuffle(hard)
                        print(hard[x])
                        if hard[x] == '+':
                            balance_bet *= 3.1
                            print('-----------------------')
                            print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                            try:
                                answer = int(input())
                            except ValueError:
                                print('Надо ввести число!')
                            if answer == 1: # Lvl 3
                                print('-----------------------')
                                hard2 = ('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                print(what0)
                                print(hard1)
                                print('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                print(what)
                                try:
                                    x = int(input())
                                except ValueError or IndexError:
                                    print('Введи 1 2 3 или 4')
                                hard_rand = random.shuffle(hard)
                                print(hard[x])
                                if hard[x] == '+':
                                    balance_bet *= 4.3
                                    print('-----------------------')
                                    print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                                    try:
                                        answer = int(input())
                                    except ValueError:
                                        print('Надо ввести число!')
                                    if answer == 1: # Lvl 4
                                        print('-----------------------')
                                        hard3 = ('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                        print(what0)
                                        print(hard1)
                                        print(hard2)
                                        print('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                        print(what)
                                        try:
                                            x = int(input())
                                        except ValueError or IndexError:
                                            print('Введи 1 2 3 или 4')
                                        hard_rand = random.shuffle(hard)
                                        print(hard[x])
                                        if hard[x] == '+':
                                            balance_bet *= 5.6
                                            print('-----------------------')
                                            print('Вы выиграли!', balance_bet, ' Хотите продолжить?\n1 - Да \n2 - Нет')
                                            try:
                                                answer = int(input())
                                            except ValueError:
                                                print('Надо ввести число!')
                                            if answer == 1: # Lvl 5
                                                print('-----------------------')
                                                hard4 = ('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                                print(what0)
                                                print(hard1)
                                                print(hard2)
                                                print(hard3)
                                                print('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                                print(what)
                                                try:
                                                    x = int(input())
                                                except ValueError or IndexError:
                                                    print('Введи 1 2 3 или 4')
                                                hard_rand = random.shuffle(hard)
                                                print(hard[x])
                                                if hard[x] == '+':
                                                    balance_bet *= 6.9
                                                    print('-----------------------')
                                                    print('У вас хорошая интуиция, вы прошли игру!')
                                                    print(hard1)
                                                    print(hard2)
                                                    print(hard3)
                                                    print(hard4)
                                                    print('{} {} {} {}'.format(hard[0], hard[1], hard[2], hard[3]))
                                                    balance += balance_bet
                                                    iphone.bal2()
                                                    print('Ваш баланс = ', balance_bet)
                                                    balance_bet = 0
                                                    print('-----------------------')
                                                    iphone.tower()
                                            else:
                                                balance += balance_bet
                                                iphone.bal2()
                                                print('Вот ваш выигрышь = ', balance_bet)
                                                balance_bet = 0
                                                print('-----------------------')
                                                iphone.tower()
                                        else:
                                            print('Вы проиграли!')
                                            balance_bet = 0
                                            print('-----------------------')
                                            iphone.tower()
                                    else:
                                        balance += balance_bet
                                        iphone.bal2()
                                        print('Вот ваш выигрышь = ', balance_bet)
                                        balance_bet = 0
                                        print('-----------------------')
                                        iphone.tower()
                                else:
                                    print('Вы проиграли!')
                                    balance_bet = 0
                                    print('-----------------------')
                                    iphone.tower()
                            else:
                                balance += balance_bet
                                iphone.bal2()
                                print('Вот ваш выигрышь = ', balance_bet)
                                balance_bet = 0
                                print('-----------------------')
                                iphone.tower()
                        else:
                            print('Вы проиграли!')
                            balance_bet = 0
                            print('-----------------------')
                            iphone.tower()
                    else:
                        balance += balance_bet
                        iphone.bal2()
                        print('Вот ваш выигрышь = ', balance_bet)
                        balance_bet = 0
                        print('-----------------------')
                        iphone.tower()
                else:
                    print('Вы проиграли!')
                    balance_bet = 0
                    print('-----------------------')
                    iphone.tower()
            else:
                print('Недостаточно средств')
                print('-----------------------')
                iphone.loading2()
        elif diff == 4:
            print('-----------------------')
            iphone.loading2()










iphone = IPhone()
iphone.bal()
iphone.loading()
