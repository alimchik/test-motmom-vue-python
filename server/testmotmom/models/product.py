from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Unicode, Date, Numeric

from datetime import datetime

from .meta import MBase, Lister



class ProductLister(Lister):
    def _get_where_condition(self, kw):
        conditions = []

        if kw.get('name'):
            conditions.append(self.model.name.ilike(f"%{kw['name'].strip()}%"))

        return conditions


class Product(MBase):
    __tablename__ = 'product'
    __lister__ = ProductLister

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    date_add = Column(Date, nullable=False, default=datetime.now())
