# Не загружайте с помощью модуля pickle файлы из ненадёжных источников. Это может привести к необратимым последствиям.

import os
import sys
import pickle


class Pickles:
    def __init__(self):
        self.version = version
        self.ver_path = version_path
        self.pickle_file_path = pickle_file_path

    def find_sub_key(self):
        # Чтение из файла
        with open(self.pickle_file_path, 'rb') as f:
            data = pickle.load(f)

        subs = {}

        for key in data:
            sub_key = key[:round(len(key) / 2)]
            sub_value = key[round(len(key) / 2):]

            if sub_key not in subs:
                subs[sub_key] = {sub_value}
            else:
                var = subs[sub_key]
                var.add(key[round(len(key) / 2):])
                subs[sub_key] = var

        # Запись в файл
        with open(self.ver_path, 'wb') as f:
            pickle.dump(subs, f)

        return f'{self.ver_path} is Done!'

    def find_subpassword(self):
        if not os.path.exists(version_path):
            try:
                os.makedirs(version_path)
            except Exception as e:
                print(f'Create Directory Error! - {e}')
                sys.exit(1)

        sorted_files_path = os.listdir('sorted')

        for file in sorted_files_path:
            print(self.find_sub_key(os.path.join(self.version_path, file), os.path.join('sorted', file)))


if __name__ == '__main__':
    version = 1
    version_path = 'passwords/version/' + f'{version}'  # путь для хранения списка паролей
    pickles_path = ''
    pickle_file_path = ''

    my_pickles = Pickles()
