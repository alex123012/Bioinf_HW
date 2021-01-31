a = [1, 3, 2, 6, 4, 5, 7]
S, way = [0] * len(a), [''] * len(a)

S[0], way[0] = a[0], ['One']
S[1], way[1] = a[1], ['Two']

for i in range(2, len(S)):
    if S[i - 1] <= S[i - 2]:
        S[i] = S[i - 1] + a[i]
        way[i] = way[i - 1] + ['One']
    else:
        S[i] = S[i - 2] + a[i]
        way[i] = way[i - 2] + ['Two']

for i in range(len(S)):
    print(f'Стоимость для ступеньки номер {i}: {S[i]} ед.')
    print(f'Путь для ступеньки номер {i}:', end=' ')
    for j in way[i]:
        print(j, end=', ')
    print('\n')
