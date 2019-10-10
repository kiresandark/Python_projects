import math, sys

def calc():
    try:
        global start_point
        global strings
        for j in range(start_point[0] + 1, number_string):
            factor = (strings[j][start_point[1]] * (-1)) / (strings[start_point[0]][start_point[1]])
            print(factor)
            for i in range(number_arg):
                strings[j][i] = strings[j][i] + strings[start_point[0]][i] * factor
                print(strings[j][i])
    except ZeroDivisionError:
        print('Решений нет, либо их бесконечное множество')
        sys.exit()

number_string = int(input('Введите количество строк'))
number_arg = int(input('Введите количество переменных в строке')) + 1
args = []
strings = []
for j in range(number_string):
    args.clear()
    for i in range(number_arg):
        if i == number_arg - 1 :
            args.append(int(input('Введите результирующее число ' + str(j + 1) + ' строки')))
        else:
            args.append(int(input('Введите '+ str(i+1) +' число '+ str(j+1) +' строки')))
    strings.append(args.copy())
print(strings)

start_point = []
start_point.append(0)
start_point.append(0)
for k in range(number_string - 1):
    calc()
    print(start_point)
    start_point[0] = start_point[0] + 1
    start_point[1] = start_point[1] + 1
    print(strings)

results = []
boolean = []
for i in range(number_string):
    results.append(0)
for i in range(number_arg):
    boolean.append(False)

for i in range(number_arg):
    if i < number_arg -2 :
        if strings[number_string-1][i] == 0:
            boolean[i] = True
    else:
        if strings[number_string-1][i] != 0:
            boolean[i] = True
try:
    if all(boolean) == True:
        for j in range(number_string):
            sum_res = 0
            for i in range(len(results)):
                sum_res += results[i] * strings[number_string - 1 - j][i]
            results[number_string - 1 - j] = (strings[number_string - 1 - j][number_arg - 1] - sum_res) / \
                                             strings[number_string - 1 - j][number_string - 1 - j]

        for i in range(len(results)):
            results[i] = round(results[i])

        print(results)
    else:
        print('Решений нет, либо их бесконечное множество')
except ZeroDivisionError:
    print('Решений нет, либо их бесконечное множество')
