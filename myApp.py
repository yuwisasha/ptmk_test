import argparse
import random
import time
import config

from db import User, Base

from tqdm import tqdm
from datetime import date
from functools import wraps

from sqlalchemy.orm import Session
from sqlalchemy import Engine
from sqlalchemy import create_engine, select


_PERSON_NAME = ('Alexanrdr', 'Maria', 'Natalia',
                'Anton', 'Fedor', 'Timur')
_PERSON_SURNAME = ('Fillimonova', 'Fillipov', 'Panteleev',
                   'Vavilov', 'Karatenkov')
_PERSON_PATRONYMIC = ('Sergeevich', 'Konstantinovich',
                      'Alexandrovich', 'Olegovna')
_DATES_OF_BIRTH = ('26.05.2000', '12.07.1989', '13.04.1992',
                   '16.09.1997', '22.06.1985')
_SEX = ('male', 'female')


try:
    ENGINE: Engine = create_engine(config.DATABASE)
except Exception as ex:
    print(ex)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start
        print(end)
    return wrapper


def _parse_args() -> argparse.Namespace:
    """
    Parse args from terminal
    """
    parser = argparse.ArgumentParser(prog='myApp', description='Test')

    parser.add_argument(
        'task',
        nargs='+',
    )

    return parser.parse_args()


def _create_table() -> None:
    """
    Create table named - user
    """
    try:
        Base.metadata.create_all(ENGINE)
        print('Table \'user\' has been created')
    except Exception:
        print('Something goes wrong when creating table')


def _create_record(record_data: list[str]) -> None:
    """
    Create record using terminal
    """
    try:
        with Session(ENGINE) as session:
            user = User(
                surname=f'{record_data[0]}',
                name=f'{record_data[1]}',
                patronymic=f'{record_data[2]}',
                birthdate=f'{record_data[3]}',
                sex=f'{record_data[4]}',
            )

        session.add(user)
        session.commit()
        print('User added successfully')

    except Exception:
        print('Not enough arguments, or some data is wrong')


def _sort_records() -> None:
    """
    Select record with unique fullname + birthdate,
    sorted by fullname
    """
    try:
        with Session(ENGINE) as session:
            stmt = select(User) \
                    .distinct(User.surname, User.name,
                              User.patronymic, User.birthdate) \
                    .order_by(User.surname, User.name,
                              User.patronymic)

        today = date.today()

        for user in tqdm(session.scalars(stmt)):
            age: int = (today.year - user.birthdate.year)
            if user.birthdate.month >= today.month and \
               user.birthdate.day > today.day:
                age -= 1
            print(user, f'Age: {age}', '\n', sep='')

    except Exception as ex:
        print(ex)


def _fill_table() -> None:
    """
    Generating 1.000.000 random records
    and 100 records with a surname starts with letter "F"
    """
    try:
        with Session(ENGINE) as session:
            print('Generating records...')
            for _ in tqdm(range(1000000)):
                user = User(
                    surname=f'{random.choice(_PERSON_SURNAME[2:])}',
                    name=f'{random.choice(_PERSON_NAME)}',
                    patronymic=f'{random.choice(_PERSON_PATRONYMIC)}',
                    birthdate=f'{random.choice(_DATES_OF_BIRTH)}',
                    sex=f'{random.choice(_SEX)}',
                )

                session.add(user)

            for _ in tqdm(range(100)):
                user = User(
                    surname=f'{random.choice(_PERSON_SURNAME[:2])}',
                    name=f'{random.choice(_PERSON_NAME)}',
                    patronymic=f'{random.choice(_PERSON_PATRONYMIC)}',
                    birthdate=f'{random.choice(_DATES_OF_BIRTH)}',
                    sex=f'{(_SEX[0])}',
                )

                session.add(user)

            print('Commiting changes...')
            session.commit()
            print('Records have been generated')

    except Exception as ex:
        print(ex)


@timer
def _selection() -> None:
    """
    Select users which surname starts with "F" and sex == male
    """
    try:
        with Session(ENGINE) as session:
            stmt = select(User).where(User.surname.startswith('F'),
                                      User.sex == 'male')

        for user in tqdm(session.scalars(stmt)):
            print(user)

    except Exception as ex:
        print(ex)


def _task_manager(task_number: int, record_data: list[str]) -> None:
    match task_number:
        case 1:
            _create_table()
        case 2:
            _create_record(record_data)
        case 3:
            _sort_records()
        case 4:
            _fill_table()
        case 5:
            _selection()


def _main() -> None:
    args = _parse_args()

    try:
        task = int(args.task[0])
    except ValueError:
        print('Type of task must be integer')
        return

    if not (0 < task < 6):
        print(f'''Wrong argument \'{task}\',
              it must be more then 0 and less then 6''')

    ENGINE.connect()
    _task_manager(task_number=task, record_data=args.task[1:])


if __name__ == '__main__':
    _main()
