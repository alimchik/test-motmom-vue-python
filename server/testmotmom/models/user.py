from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Unicode

from .meta import MBase

class User(MBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    email = Column(Unicode, unique=True, nullable=False)
    password = Column(Unicode, nullable=False)
