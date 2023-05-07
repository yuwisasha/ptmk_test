from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Date
from datetime import date


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
    birthdate: Mapped[date] = mapped_column(Date(), nullable=False)
    sex: Mapped[str] = mapped_column(String(6))

    def __repr__(self):
        return f"""id: {self.id}\nSurname: {self.surname}
                   \rName: {self.name}\nPatronymic: {self.patronymic}
                   \rBirth date: {self.birthdate}\nSex: {self.sex}\n"""
