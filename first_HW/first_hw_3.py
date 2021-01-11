a = input('Enter list of numbers divided with spaces ')
a_list = [float(i) for i in a.split()]
a_list.reverse()
for i in a_list:
    print(i, end =' ')
print()