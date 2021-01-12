def quadratic_equation(a, b, c, rnd=4):

    """Solving quadratic equations"""

    if a == 0:
        if b == 0:
            if c == 0:
                return 'any numbers'
            else:
                return 'No solutions'
        elif c == 0:
            return 0.0
        else:
            return -c / b
    elif b == 0:
        if c <= 0:
            return c**0.5
        else:
            x1 = (-c)**0.5
            return  complex(f'{round(x1.imag, rnd)}j') + round(x1.real, rnd)
        

    dD = b**2 - 4*a*c

    if dD >= 0:
        x1 = (-b + dD**0.5) / 2*a
        if dD == 0:
            return x1
        x2 = (-b - dD**0.5) / 2*a

        return x1, x2

    else:
        sqrtD = dD**0.5

        x1 = (-b + sqrtD**0.5) / 2*a
        x2 = (-b - sqrtD**0.5) / 2*a

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