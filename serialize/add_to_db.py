import sqlite3
import datetime


for pas in range(1, 100001):

    start = datetime.datetime.now()

    var = 'AAAAAA'

    try:
        with sqlite3.connect("test.db") as db:
            sql = db.cursor()
            sql.execute("INSERT INTO six(password) VALUES (?)", (var,))
            db.commit()
            # print(f'Добавлен новый заказ - {var}')

            if pas % 1000 == 0:
                end = datetime.datetime.now()
                print(f'{pas} - {end - start}')

    except Exception as e:
        print(f'{e} - err, password - {var}')
