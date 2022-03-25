# Не загружайте с помощью модуля pickle файлы из ненадёжных источников. Это может привести к необратимым последствиям.

import pickle
import itertools
import datetime

symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

stop = 0

start = datetime.datetime.now()
print(f'Start generate - {start}')

var = {}

for i in itertools.combinations_with_replacement(symbols, 6):
    if stop == 100000:
        break

    stop += 1
    var[f'{"".join(i)}'] = {}

end = datetime.datetime.now()
print(f'End generate - {end}')

# Запись в файл
with open('100.pickle', 'wb') as f:
    print(f'Start write to file - {datetime.datetime.now()}')
    pickle.dump(var, f)
    print(f'End write to file - {datetime.datetime.now()}')


# Чтение из файла
with open('100.pickle', 'rb') as f:
    print('Начинаю читать')
    data = pickle.load(f)
    print('Прочтено')

    stop2 = 0

    for key in data:
        stop2 += 1
        if stop2 == 50:
            break

        print(key, data[key])
