a = int(input('Enter number of iterations '))
if a < 2:
    raise ValueError('Too small for this program')

fir = float(input('Enter number '))
sec = float(input('Enter number '))
if sec > fir:
    fir, sec = sec, fir

for _ in range(a-2):

    c = float(input('Enter number '))
    if c > fir:
        sec, fir = fir, c
    elif c > sec and c < fir:
        sec = c

print(sec)