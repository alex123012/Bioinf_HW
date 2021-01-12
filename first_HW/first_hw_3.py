try:
    a_list = list(map(float, input('Enter list of numbers divided with spaces ').split()))[::-1]
except ValueError:
    print("Type only numbers!!!")
else:
    for i in a_list:
        print(i, end =' ')
    print()