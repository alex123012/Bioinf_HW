def reverse_compliment(string):
    comp_Watson_Crick = {'A': 'T',
                         'T': 'A',
                         'G': 'C',
                         'C': 'G',
                         }
    res = ''
    for i in string[::-1].upper():
        try:
            res += comp_Watson_Crick[i]
        except KeyError:
            res += '-'

    return res


def main():
    a = input("Enter your sequence 3'-> 5': ")
    x = reverse_compliment(a)

    print(f"3'- {x} -5'\n\n")
    print(f"3'- {a.upper()} -5'")
    print(f'    {"|"*len(a)}')
    print(f"5'- {x[::-1]} -3'")


if __name__ == '__main__':
    main()
