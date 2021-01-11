def quadratic_equation(a, b, c):

    """Solving quadratic equations"""

    dD = b**2 - 4*a*c

    if dD >= 0:
        x1 = (-b + dD**0.5) / 2*a
        if dD == 0:
            # print(f'x = {x1}')
            return x1
        x2 = (-b - dD**0.5) / 2*a
        # print(f'x1 = {x1}, x2 = {x2}')

        return x1, x2

    else:
        sqrtD = dD**0.5
        sqrtD = sqrtD - sqrtD.real if sqrtD.real < 1e-4 else sqrtD 

        x1 = (-b + sqrtD**0.5) / 2*a
        x2 = (-b - sqrtD**0.5) / 2*a

        rnd = 4
        x1 = complex(f'{round(x1.imag, rnd)}j') + round(x1.real, rnd)
        x2 = complex(f'{round(x2.imag, rnd)}j') + round(x2.real, rnd)
        # print(f'x1 = {x1}, x2 = {x2}')

        return x1, x2

def main():
    a = float(input('Enter coefficient A: '))
    b = float(input('Enter coefficient B: '))
    c = float(input('Enter coefficient C: '))
    print('Quadratic roots are', quadratic_equation(a, b, c))

if __name__=='__main__':
    main()