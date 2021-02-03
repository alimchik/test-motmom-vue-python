import decimal
import io
import json


def extract_params(req):
    body = req.stream.read()
    req.stream = io.BytesIO(body)
    if body:
        return json.loads(body.decode(), parse_float=decimal.Decimal)