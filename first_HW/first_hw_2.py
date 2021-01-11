a = input('Enter list of numbers divided with spaces ')
a_list = [float(i) for i in a.split()]
print(sum(a_list)/len(a_list))