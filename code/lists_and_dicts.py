def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname':'Oscar','lastname':'Palomino'}
    
    super_list = [
        {'firstname':'Oscar','lastname':'Palomino'},
        {'firstname':'Eduardo','lastname':'Cardenas'},
        {'firstname':'Lisney','lastname':'Gomez'},
        {'firstname':'Jurenni','lastname':'Berdugo'},
        {'firstname':'Ana','lastname':'Cardenas'},
        {'firstname':'Doris','lastname':'Toscano'},
    ]
    
    super_dict = {
        'natural_nums':[1,2,3,4,5,6],
        'integer_nums':[-1,-2,0,1,2],
        'floating_nums':[1.1,2.5,5.7,7.3,9.7]
    }
    
    for key, value in super_dict.items():
        print(f"""
Key: {key}
  * Value: {value}""")
    
    for item in super_list:
        print(item)


if __name__ == '__main__':
    main()
    