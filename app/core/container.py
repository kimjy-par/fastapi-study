from dependency_injector import containers, providers

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.db.database import Database
from app.core.config import settings

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules = [
            'app.apis.endpoints.user'
        ]
    )

    db = providers.Singleton(Database, db_url=settings.DATABASE_URI)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)

    user_service = providers.Factory(UserService, user_repository=user_repository)
