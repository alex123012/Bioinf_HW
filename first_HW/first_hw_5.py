a = int(input('Enter number of iterations '))
if a < 2:
    raise ValueError('Number of iterations is too small for this program')

fir = float(input('Enter number '))
sec = float(input('Enter number '))

fir, sec = (sec, fir) if sec > fir else (fir, sec)

for _ in range(a-2):

    c = float(input('Enter number '))
    fir  = c if c > fir else fir
    sec = c if c > sec and c < fir else sec

print(sec)