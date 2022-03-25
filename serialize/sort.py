# Не загружайте с помощью модуля pickle файлы из ненадёжных источников. Это может привести к необратимым последствиям.

import pickle


sorted_passwords = {i: set() for i in range(3, 28)}

# чтение паролей из текстового файла
with open("db/5.txt", "r") as txt_file:
    passwords = txt_file.read().split('\n')

# сортировака паролей по длине
for password in passwords:
    if 28 > len(password) > 2:
        new_password = sorted_passwords[len(password)]
        new_password.add(password)
        sorted_passwords[len(password)] = new_password


# запись отсортированных паролей по длине в файл
for key in sorted_passwords:
    try:
        with open(f'sorted/{key}.pickle', 'rb') as f:
            data = pickle.load(f)

    except FileNotFoundError:
        print(f'FileNotFoundError - {key}.pickle')
        print(f'Create {key}.pickle')

        with open(f'sorted/{key}.pickle', 'wb') as f:
            pickle.dump(sorted_passwords[key], f)
            print(f'Create {key}.pickle is Done!')

    else:
        # Запись в файл
        with open(f'sorted/{key}.pickle', 'wb') as f:
            data = data.union(sorted_passwords[key])
            pickle.dump(data, f)
            print(f'{key} - {len(sorted_passwords[key])}')
