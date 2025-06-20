from repositories.users import UserRepository
from services.users import UserService


def user_service():
    """
    Dependency function to provide a UserService instance.

    Returns:
        UserService: An instance of UserService initialized with UserRepository.
    """
    return UserService(UserRepository)
