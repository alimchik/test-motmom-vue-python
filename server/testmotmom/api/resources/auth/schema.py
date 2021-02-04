auth = {
    "type": "object",
    "required": ["email", "password"],
    "properties": {
        "email": {
            "type": "string",
            "pattern": r"^$|^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            "message": "Некорректный email"
        },
        "password": {"type": "string", "minLength": 3, "message": "Минимальная длина пароля 3 символа"},
    }
}
