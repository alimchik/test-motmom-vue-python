import copy
import falcon
from jsonschema import Draft7Validator, validators
from jsonschema.exceptions import ValidationError

from .helpers import extract_params


def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(
            validator, properties, instance, schema,
        ):
            yield error

    return validators.extend(
        validator_class, {"properties": set_defaults},
    )


DefaultValidatingDraft4Validator = extend_with_default(Draft7Validator)


def validate_params(schema, data):
    vschema = schema
    if 'properties' not in vschema:
        schemas = copy.deepcopy(vschema)
        vschema = schemas.pop('__default__')
        for condition, cschema in schemas.items():
            field, value = condition.split('=')
            if data.get(field) == value:
                vschema = cschema
                break

    DefaultValidatingDraft4Validator(vschema).validate(data)


def validate(schema, chained_validators=None):
    def wrapper(req, resp, resource, params):
        if req.method in ('POST', 'PUT'):
            req_params = extract_params(req)
        # elif req.method == 'GET':
        #     req_params = req.params
        elif req.method in ('GET', 'PATCH'):
            req_params = extract_params(req)
        try:
            # import pdb
            # pdb.set_trace()
            validate_params(schema, req_params)
        except ValidationError as err:
            raise falcon.HTTPUnprocessableEntity(title='Ошибка валидации', description=err.message)
        else:
            req.context['validated_params'] = req_params
    return wrapper