def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        # if num%i == 1:
        if num%i == 0:
            divisors.append(i)
    return divisors

def main():
    try:
        num = int(input('Ingresa un numero: '))
        if num < 0:
            raise ArithmeticError('Debes ingresar un número negativo')
        print(divisors(num))
        print('Termino la ejecución.')
    except ValueError as ve:
        print(ve)
        print('Debes ingresar un número.')

if __name__ == '__main__':
    main()
