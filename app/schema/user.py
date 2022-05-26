from pydantic import BaseModel, Field

from app.schema.base_schema import ModelBaseInfo
from app.utils.schema_class_parser import AllOptional

class BaseUser(BaseModel):
    email: str
    password: str
    name: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    class Config:
        orm_mode = True

class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
    ...
