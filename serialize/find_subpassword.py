# Не загружайте с помощью модуля pickle файлы из ненадёжных источников. Это может привести к необратимым последствиям.
import os
import sys
import pickle


def find_sub_key(ver_path, pickle_file_path):
    # Чтение из файла
    with open(pickle_file_path, 'rb') as f:
        data = pickle.load(f)

    subs = {}

    for key in data:
        sub_key = key[:round(len(key)/2)]
        sub_value = key[round(len(key)/2):]

        if sub_key not in subs:
            subs[sub_key] = {sub_value}
        else:
            var = subs[sub_key]
            var.add(key[round(len(key)/2):])
            subs[sub_key] = var

    # for i in subs:
    #     print(i)

    # Запись в файл
    with open(ver_path, 'wb') as f:
        pickle.dump(subs, f)

    return f'{ver_path} is Done!'


if __name__ == '__main__':

    version = 1     # версия списка паролей
    version_path = 'passwords/version/' + f'{version}'      # путь для хранения списка паролей

    if not os.path.exists(version_path):
        try:
            os.makedirs(version_path)
        except Exception as e:
            print(f'Create Directory Error! - {e}')
            sys.exit(1)

    sorted_files_path = os.listdir('sorted')

    for file in sorted_files_path:
        print(find_sub_key(os.path.join(version_path, file), os.path.join('sorted', file)))
