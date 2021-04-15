import math

def main():
    # Challenge 1: Create a dictionary wich the key is the first 100 natural numbers and the value is the cube of these keys
    my_challenge = {x: x**3 for x in range(1,101)}
    print('Challenge 1: The keys are the first 100 numbers and the value is the cube of the key.')
    print(my_challenge)

    # Challenge 2: Create a dictionary wich the key is the first 100 natural numbers and the value is the cube of these keys BUT, each number MUST NOT be divisible by 3.
    my_challenge2 = {x:x**3 for x in range(1,101) if x%3 != 0}
    print('Challenge 2: first 100 natural numbers BUT, not divisible by 3')
    print(my_challenge2)
    
    # Challenge 3: Create a dictionary which the key is the first 1000 natural numbers and the value the square root of those numbers.
    my_challenge3 = {x: round(math.sqrt(x), 3) for x in range(1, 1001)}
    print('first 1000 natural numbers and their square root.')
    print(my_challenge3)

if __name__ == '__main__':
    main()
    