from typing import List

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, JSON

from sqlalchemy.orm import declarative_base, sessionmaker, Relationship, mapped_column, Mapped

from app.config import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine, echo=True)


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


class Advert(Base):
    __tablename__ = 'advertisements'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    url: str = Column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = Relationship(back_populates='adverts')
