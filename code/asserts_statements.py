def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        # if num%i == 1:
        if num%i == 0:
            divisors.append(i)
    return divisors

def main():
    num = input('Ingresa un numero: ')
    assert num.isnumeric() or int(num) > 0, 'Solo se puede ingresar valores numericos positivos.'
    print(divisors(int(num)))
    print('Termino la ejecución.')
    

if __name__ == '__main__':
    main()