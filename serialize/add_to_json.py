import os
import random
import itertools
import json
import sqlite3

for pas in range(1, 100001):

    var = 'AAAAAAAAAA'

    with open("100.json", "r+", encoding='utf-8') as my_json:
        data = my_json.read()
        passw = json.loads(data)

        new_passw = passw['paroles']
        new_passw.append(var)

        passw['paroles'] = new_passw
        my_json.write(json.dumps(passw, sort_keys=True, indent=2))

    with open("100.json", "w", encoding='utf-8') as my_json:
        my_json.write(json.dumps(passw, sort_keys=True, indent=2))
