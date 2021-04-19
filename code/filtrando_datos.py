DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print(all_python_devs)
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print(all_platzi_workers)
    
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print(adults)
    
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    for person in old_people:
        print(person)
    
    # Crear las listas all_python_devs y all_Platzi_workers usando una combinación de filter y map
    print('Challenge 1: Python developers')
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    for worker in all_python_devs:
        print(worker)
    
    print('Challenge 1: Platzi workers')
    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))
    for worker in all_platzi_workers:
        print(worker)
    
    # Crear la lista old_people y adults con list comprehensions
    print('Challenge 2: all adults')
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    for worker in adults:
        print(worker)
    
    print('Challenge 2: Old people with dictionary')
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    for worker in old_people:
        print(worker)
    
    pass

if __name__ == '__main__':
    main()