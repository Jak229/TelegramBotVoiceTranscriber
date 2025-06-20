from abc import ABC, abstractmethod
from db.models import async_session

from sqlalchemy import insert, select, update, func


class AbstractRepository(ABC):
    @abstractmethod
    async def find_by_id():
        raise NotImplementedError

    @abstractmethod
    async def add():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError

    @abstractmethod
    async def find_one_or_none():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def find_by_id(self, model_id: int):
        """
        Find a record by its ID.
        :param model_id: The ID of the record to find.
        :return: The record if found, None otherwise.
        """
        async with async_session() as session:
            query = select(self.model).filter_by(id=int(model_id))
            result = await session.execute(query)
            return result.first()

    async def add(self, **data):
        """
        Add a new record to the database.
        :param data: The data to insert into the record.
        """
        async with async_session() as session:
            query = insert(self.model).values(**data)
            await session.execute(query)
            await session.commit()

    async def update(self, table_column, value, **data):
        """
        Update a record in the database.
        :param table_column: The column to filter by.
        :param value: The value to filter by.
        :param data: The data to update in the record.
        """
        async with async_session() as session:
            table = self.model
            query = update(table).where(table_column == value).values(**data)
            await session.execute(query)
            await session.commit()

    async def find_one_or_none(self, **filter_by):
        """
        Find a single record by its attributes.
        :param filter_by: The attributes to filter by.
        :return: The record if found, None otherwise.
        """
        async with async_session() as session:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def find_all(self, **filter_by):
        """
        Find all records by their attributes.
        :param filter_by: The attributes to filter by.
        :return: A list of records that match the filter.
        """
        async with async_session() as session:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    async def count(self, **filter_by):
        """
        Count the number of records that match the filter.
        :param filter_by: The attributes to filter by.
        :return: The count of records that match the filter.
        """
        async with async_session() as session:
            query = select(func.count()).select_from(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one()

    async def delete(self, **filter_by):
        """
        Delete a record from the database.
        :param filter_by: The attributes to filter by.
        """
        async with async_session() as session:
            query = self.model.__table__.delete().where(
                *[getattr(self.model, key) == value for key, value in filter_by.items()]
            )
            await session.execute(query)
            await session.commit()
