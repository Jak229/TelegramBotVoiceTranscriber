from utils.repository import AbstractRepository


class UserService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo()

    async def find_one_user(self, id: int):
        """
        Find a user by ID.
        :param id: The ID of the user to find.
        :return: The user if found, None otherwise.
        """
        user = await self.user_repo.find_one_or_none(id=id)
        return user

    async def find_user_by_id(self, id: int):
        """
        Find a user by ID.
        :param id: The ID of the user to find.
        :return: The user if found, None otherwise.
        """
        user = await self.user_repo.find_by_id(id)
        return user

    async def add_user(self, **data):
        """
        Add a new user to the database.
        :param data: The data to insert into the user record.
        """
        user_id = data.get("id")
        if user_id is not None:
            existing_user = await self.user_repo.find_by_id(user_id)
            if existing_user:
                # Optionally, you can raise an exception or just return
                return
        await self.user_repo.add(**data)

    async def update_user(self, value, **data):
        """
        Update a user in the database.
        :param value: The value to filter by.
        :param data: The data to update in the user record.
        """
        await self.user_repo.update(self.user_repo.model.id, value, **data)

    async def delete_user(self, id: int):
        """
        Delete a user from the database.
        :param id: The ID of the user to delete.
        """
        await self.user_repo.delete(id)

    async def get_count_users(self):
        """
        Get the count of all users in the database.
        :return: The count of users.
        """
        count = await self.user_repo.count()
        return count

    async def get_all_users(self):
        """
        Get all users from the database.
        :return: A list of all users.
        """
        users = await self.user_repo.find_all()
        return users
