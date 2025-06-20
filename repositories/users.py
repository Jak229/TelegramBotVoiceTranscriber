from db.models import User
from utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """
    Repository class for User model.

    Provides database operations for User entities using SQLAlchemyRepository as a base.

    Attributes:
        model: The User model class.
    """
    model = User
