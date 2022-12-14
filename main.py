"""

CRUD - Create Read Update Delete

Database

Terminal View

UX - add Email and Message (CRUD)

"""

DataBase: dict = dict()

_id = 0

def create_data(email: str, message: str):
    """
    add object in DataBase
    """
    global _id

    obj = {
        'email': email,
        'message': message
    }
    DataBase[_id] = obj

    _id += 1


def show_database(flag: bool) -> None:
    """
    show all data in DataBase
    """
    if flag:
        for k, v in DataBase.items():
            print(k, v, '\n')
    else:
        print(DataBase)



for i in range(10):
    create_data(f'test{i}@test.com', 'hello it\'s spam')

show_database(flag=True)
print('-' * 50)
# create_data('test@test.com', 'hello it\'s spam')
show_database(flag=False)



# TODO Read for data
# TODO Update for data
# TODO Delete for data
# TODO ShowData upgrade