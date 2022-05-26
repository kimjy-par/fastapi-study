from sqlalchemy.ext.declarative import declared_attr, as_declarative

@as_declarative()
class Base():
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
