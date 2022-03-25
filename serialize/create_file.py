import os
import random
import itertools
import json
import sqlite3

with open("data2.txt", 'a+', encoding='utf-8') as my_file:

    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    stop = 0

    for pas in itertools.combinations_with_replacement(symbols, 6):
        stop += 1
        if stop == 100000:
            break

        if stop % 1000 == 0:
            print(stop)

        var = ''.join(pas)

        my_file.write(var)
        my_file.write('\n')

        with open("data.json", "r+", encoding='utf-8') as my_json:
            data = my_json.read()
            passw = json.loads(data)

            new_passw = passw['paroles']
            new_passw.append(var)

            passw['paroles'] = new_passw
            my_json.write(json.dumps(passw, sort_keys=True, indent=2))

        with open("data.json", "w", encoding='utf-8') as my_json:
            my_json.write(json.dumps(passw, sort_keys=True, indent=2))

        try:
            with sqlite3.connect("data.db") as db:
                sql = db.cursor()
                sql.execute("INSERT INTO passwords(password) VALUES (?)", (var,))
                db.commit()
                # print(f'Добавлен новый заказ - {var}')
        except Exception as e:
            print(f'{e} - err, password - {var}')


# 65-90 A-Z
# 97-122 a-z

# letters = []
#
# for i in range(65, 91):
#     # print(f'{i} - {chr(i)}')
#     letters.append(chr(i))
#
# for i in range(97, 123):
#     # print(f'{i} - {chr(i)}')
#     letters.append(chr(i))

# print(letters)
