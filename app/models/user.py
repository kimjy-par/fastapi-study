from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, DATETIME

from app.db.base import Base
from app.utils.date_utils import get_now


class User(Base):
    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    email = Column(VARCHAR(255), unique=True, nullable=False)
    username = Column(VARCHAR(255), nullable=True)
    password = Column(VARCHAR(255), nullable=False)

    is_active = Column(BOOLEAN, default=True)
    is_superuser = Column(BOOLEAN, default=False)

    created_at = Column(DATETIME, nullable=True, default=get_now)
    updated_at = Column(DATETIME, nullable=True, default=get_now, onupdate=get_now)
