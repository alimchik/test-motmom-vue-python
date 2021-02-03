import inflect

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from mo.sqlalchemy.orm import model_base
from mo.sqlalchemy.lister import Lister

DBSession = scoped_session(sessionmaker(autoflush=False))
Base = declarative_base(cls=model_base(DBSession))

p = inflect.engine()


class ModelLister(Lister):

    def __call__(self):
        """ @return: dictionary representation of the returned object.
            @rtype: 'dict'
        """
        objects = self.generate_query()

        meta = {'total': self._get_result_count()}

        if self.query_gen.limit:
            meta['total_pages'] = int(math.ceil(float(meta['total']) / self.query_gen.limit))

        listname = getattr(self, '__listname__', self.model.__resourcename__)

        return {
            p.plural(listname): self._get_result(objects),
            'meta': meta
        }


class MBase(Base):
    __abstract__ = True
    __lister__ = ModelLister

    def save(self):
        super().save()
        return self

    def __jsonify__(self, *fields, exclude_fields=None, is_show_private_fields=False):
        ''' Сериализация текущего состояния модели в `dict`.

        :param list fields: список полей для сериализации
        :param list exclude_fields: список полей для исключения из `dict`
        :param bool is_show_private_fields: флаг для добавления приватных полей модели в `dict`

        В случае пустого списка `fields` и параметров функции по умолчанию, то результатом будет
        сериализация полей объекта модели без приватных полей, которые помечены флагом
        `is_private_field`
        '''
        exclude_fields = exclude_fields or []
        if not is_show_private_fields:
            exclude_fields += self.get_private_fileds()

        jsonified = {}
        for field in self.get_fields():
            if (
                # добавить ли поле в ответ при переданном списке полей
                ((fields and field in fields) or
                 # в случае пустого переданного списка для сериализации
                 # скрыть условно приватные поля
                 (not fields and field[0] != '_')) and
                # и скрыть поля из списка  `exclude_fields`
                (not exclude_fields or field not in exclude_fields)
            ):
                jsonified[field] = getattr(self, field)

        return jsonified
