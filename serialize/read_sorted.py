# Не загружайте с помощью модуля pickle файлы из ненадёжных источников. Это может привести к необратимым последствиям.

import pickle
import os


# Чтение из файлов
files = os.listdir('sorted')
all = 0

# for file in files:
#     if os.path.isfile(f'sorted/{file}'):
#         with open(f'sorted/{file}', 'rb') as f:
#             data = pickle.load(f)
#             all += len(data)
#             print(f'{file} - {len(data)}')
#
# print(all)

file = 13

with open(f'sorted/{file}.pickle', 'rb') as f:
    data = pickle.load(f)
    print('Original')
    print(data)
    print()


with open(f'passwords/version/1/{file}.pickle', 'rb') as f:
    data = pickle.load(f)
    print('Modify')
    print(data)
    print()
