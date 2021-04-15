def main():
    # Challenge 1: Create alist with the first 100 natural numbers and return the square.
    my_challenge = [x**2 for x in range(1, 101)]
    print('Challenge 1: first 100 squares.')
    print(my_challenge)
    
    # Challenge 2: Square of the first 100 numbers but not those who are divisible by 3.
    my_challenge2 = [x**2 for x in range(1,101) if x%3 != 0]
    print('Challeng2: Squares not divisible by 3.')
    print(my_challenge2)
    
    # Challenge 3: Create a list comprehension that containes all the multiples of 4, 6 and 9, until the 5 digits.
    my_challenge3 = [x for x in range(1,100000) if x%4 == 0 and x%6 == 0 and x%9 == 0]
    print('Challenge 3: Multiples of 4, 6 and 9, until 5 digits.')
    print(my_challenge3)

if __name__ == '__main__':
    main()
    