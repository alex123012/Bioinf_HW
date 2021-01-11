a = int(input('Enter number of iterations '))
if a < 1:
    raise ValueError('Too small for this program')

b = float(input('Enter number '))

for _ in range(a-1):
    c = float(input('Enter number '))
    b = c if c > b else b
print(b)