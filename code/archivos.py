def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
        f.close()
    print(numbers)
    return numbers

def write():
    names = ['Miguel', 'Facundo', 'Leonardo', 'Antonio', 'Rocío']
    with open("./archivos/names.txt", 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
        f.close()

def main():
    read()
    write()


if __name__ == '__main__':
    main()
    