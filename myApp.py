import psycopg2
import argparse
import random
import time
import config

from sqlalchemy.orm import DeclarativeBase, Mapped, Session
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Date, Engine
from sqlalchemy import create_engine, select


_PERSON_NAME = 'Alexanrdr', 'Maria', 'Natalia', 'Anton', 'Fedor', 'Timur'
_PERSON_SURNAME = 'Fillimonov', 'Fillipov', 'Panteleev', 'Vavilov', 'Karatenkov'
_PERSON_PATRONYMIC = 'Sergeevich', 'Konstantinovich', 'Alexandrovich', 'Olegovich'
_DATES_OF_BIRTH = '26.05.2000', '12.07.1989', '13.04.1992', '16.09.1997', '22.06.1985'
_SEX = 'male', 'female'


try:
    ENGINE: Engine = create_engine(config.DATABASE)
except Exception as ex:
    print(ex)


class Base(DeclarativeBase):
    pass


class User(Base):
    """
    User representation in a database
    """
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    surname: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(20), nullable=False)
    birthdate: Mapped[str] = mapped_column(Date(), nullable=False)
    sex: Mapped[str] = mapped_column(String(6))

    def __repr__(self):
        return f"""id: {self.id} \nSurname: {self.surname}
                   \rName: {self.name} \nPatronymic: {self.patronymic}
                   \rBirth date: {self.birthdate} \nSex: {self.sex} \n"""


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


def _create_table(engine: Engine) -> None:
    """
    Create table named - user
    """
    try:
        Base.metadata.create_all(engine)
    except Exception:
        print('Something goes wrong when creating table')


def _create_record(record_data: list[str]) -> None:
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

    except Exception as ex:
        print(ex)


def _sort_records() -> None:
    try:
        with Session(ENGINE) as session:
            stmt = select(User).distinct(User.surname, User.name,
                                         User.patronymic, User.birthdate,) \
                                         .order_by(User.surname, User.name,
                                                   User.patronymic,)

        for user in session.scalars(stmt):
            print(user)

    except Exception as ex:
        print(ex)


def _generate_record() -> None:
    try:
        with Session(ENGINE) as session:
            user = User(
                surname=f'{random.choice(_PERSON_SURNAME)}',
                name=f'{random.choice(_PERSON_NAME)}',
                patronymic=f'{random.choice(_PERSON_PATRONYMIC)}',
                birthdate=f'{random.choice(_DATES_OF_BIRTH)}',
                sex=f'{random.choice(_SEX)}',
            )

        session.add(user)
        session.commit()

    except Exception as ex:
        print(ex)


def _selection() -> None:
    try:
        with Session(ENGINE) as session:
            stmt = select(User).where(User.surname.startswith('F'), User.sex == 'male')

        for user in session.scalars(stmt):
            print(user)

    except Exception as ex:
        print(ex)


def _task_manager(task_number: int, record_data: list[str] = []) -> None:
    match task_number:
        case 1:
            _create_table(engine=ENGINE)
        case 2:
            _create_record(record_data)
        case 3:
            _sort_records()
        case 4:
            for _ in range(1000000):
                _generate_record()
        case 5:
            start = time.time()
            _selection()
            end = time.time() - start
            print(end)


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
