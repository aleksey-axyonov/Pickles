# запись отсортированных паролей по длине в файл
import pickle

sorted_passwords = {
    13: set()
}

a = sorted_passwords[13]
a.add('123213123123')
sorted_passwords[13] = a

with open(f'sorted/20.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)
    data = data.union(sorted_passwords[13])
    # for i in sorted_passwords[13]:
    #     data.add(i)
    print(data)
    # var = set()
    # for i in data:
    #     var.add(i)
    #
    # var.add(sorted_passwords[13])
    # print(var)

# Запись в файл
# with open(f'sorted/13.pickle', 'wb') as f:
#     data.add(sorted_passwords[13])
#     pickle.dump(data, f)


"""
3 - 68
4 - 585
5 - 1016
6 - 3611
7 - 2537
8 - 3416
9 - 882
10 - 364
11 - 92
12 - 40
13 - 6
14 - 0
15 - 0
16 - 0
17 - 0
18 - 0
19 - 0
20 - 0
21 - 0

3 - 1
4 - 2
5 - 2
6 - 99
7 - 41
8 - 49
9 - 11
10 - 2
11 - 0

3 - 2410
4 - 9052
5 - 14606
6 - 41991
7 - 31364
8 - 89161
9 - 39553
10 - 29341
11 - 18575
12 - 12373
13 - 7948
14 - 4758
15 - 1400
16 - 477
17 - 131
18 - 47
19 - 25
20 - 15
21 - 0

3 - 1
4 - 27
5 - 87
6 - 646
7 - 366
8 - 350
9 - 75
10 - 17
11 - 4
12 - 1
13 - 0


8 - 89161
9 - 39553
10 - 29341
11 - 18575
12 - 12373
13 - 7948
14 - 4758
15 - 1400
16 - 477
17 - 131
18 - 47
19 - 25
20 - 15
21 - 0

"""