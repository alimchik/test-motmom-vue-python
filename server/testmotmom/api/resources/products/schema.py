format_date = {
    "type": "string",
    "pattern": "^20[0-9]{2}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
}


product = {
    "type": "object",
    "required": ["name", "count", "price", "date_add"],
    "properties": {
        "name": {"type": "string"},
        "count": {"type": "integer"},
        "price": {"type": "number"},
        "date_add": format_date
    }
}
