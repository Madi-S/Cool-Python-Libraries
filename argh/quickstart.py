import argh
from random import randint


users = {}


def data_types(name: str, age: int=18, male: bool=False):
    '''Test function to display data types, -m refers to male'''

    print(f'Name: {name}, type: {type(name)}')
    print(f'Age:  {age}, type: {type(age)}')
    print(f'Male: {male}, type: {type(male)}')

    return 'You are breathtaking'


def create_user(username: str, password: str, admin: bool = False, user_id: int = None):
    '''Creates and adds user to the database'''
    global users

    if not user_id:
        user_id = randint(1, 1000)
    users.update({
        user_id: {
            'username': username,
            'password': password,
            'admin': admin,
        }})
    return users


if __name__ == '__main__':
    argh.dispatch_commands([data_types, create_user])


'''
python quickstart.py --help

    Test function to display data types, -m refers to male

    positional arguments:
    name               -

    optional arguments:
    -h, --help         show this help message and exit
    -a AGE, --age AGE  18
    -m, --male         False

----------------------------------------------------------------

python quickstart.py data-types jack --age=39

    Name: jack, type: <class 'str'>
    Age:  39, type: <class 'int'>
    Male: False, type: <class 'bool'>
    You are breathtaking


python quickstart.py data-types jack --age=39jfk
    usage: quickstart.py data-types [-h] [-a AGE] [-m] name
    quickstart.py data-types: error: argument -a/--age: invalid int value: '39jfk'


python quickstart.py data-types aboy --age=12 --male
    Name: aboy, type: <class 'str'>
    Age:  12, type: <class 'int'>
    Male: True, type: <class 'bool'>
    You are breathtaking

----------------------------------------------------------------

python quickstart.py create-user user123 mypass


python quickstart.py create-user madi 55123 --user-id=123


python quickstart.py create-user madi 55123 --user-id=123 --admin
'''