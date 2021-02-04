format_date = {
    "type": "string",
    "pattern": "^20[0-9]{2}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$",
    "message": "Дата добавления должна быт формата ГГГГ-ММ-ДД"
}


product = {
    "type": "object",
    "required": ["name", "count", "price", "date_add"],
    "properties": {
        "name": {"type": "string", "minLength": 1, "message": "Название продукта должно быть не пустой строкой"},
        "count": {"type": "integer", "minLength": 1, "message": "Количетсво должно быть целым числом"},
        "price": {"type": "number", "minLength": 1, "message": "Цена должна быть десятичным числом"},
        "date_add": format_date
    }
}
