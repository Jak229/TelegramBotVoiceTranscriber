"""
Database models for the bot.
This module contains the database models used in the bot.
It uses SQLAlchemy for ORM and SQLite as the database engine.
The User model has the following fields:
- id: The unique TG identifier for the user (primary key).
- username: The username of the user.
- lang: The language the user uses for voice transcription.
- admin: A boolean value indicating whether the user is an admin or not.
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import Table, Column, Integer, String, Boolean, BigInteger

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    lang = Column(String, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)

    def __str__(self):
        return f"{self.username}"


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
