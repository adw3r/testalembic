from typing import List

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, JSON

from sqlalchemy.orm import declarative_base, sessionmaker, Relationship, mapped_column, Mapped

from app.config import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


def create_session():
    return Session()


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)

    name: str = Column(String(20), nullable=False)
    surname: str = Column(String(20), nullable=False)
    status: str = Column(String, default='not spammed')
    user_info: dict = Column(JSON)

    adverts: Mapped[List["Advert"]] = Relationship(back_populates='user')

    def __repr__(self):
        return f'User(name={self.name}, surname={self.surname}, status={self.status})'


class Advert(Base):
    __tablename__ = 'advertisements'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    url: str = Column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = Relationship(back_populates='adverts')

    def __repr__(self):
        return f'Advert(url={self.url}, user_id={self.user_id})'


def create_users():
    users = [
        User(name='test', surname='test') for _ in range(6)
    ]
    session = create_session()

    session.add_all(users)
    session.commit()


def create_adverts():
    session = create_session()
    users = session.query(User).all()
    adverts = [
        Advert(url='https://testurl.com', user_id=users.pop().id),
        Advert(url='https://testurl.com', user_id=users.pop().id),
        Advert(url='https://testurl.com', user_id=users.pop().id),
        Advert(url='https://testurl.com', user_id=users.pop().id),
        Advert(url='https://testurl.com', user_id=users.pop().id),
        Advert(url='https://testurl.com', user_id=users.pop().id),
    ]
    session.add_all(adverts)
    session.commit()


if __name__ == '__main__':
    create_users()
    create_adverts()
