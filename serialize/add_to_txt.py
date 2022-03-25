import datetime

with open("100.txt", 'a+', encoding='utf-8') as my_file:

    var = 'AAAAAA'

    for pas in range(1, 100001):
        start = datetime.datetime.now()

        my_file.write(var)
        my_file.write('\n')

        if pas % 1000 == 0:
            end = datetime.datetime.now()
            print(f'{pas} - {end - start}')
