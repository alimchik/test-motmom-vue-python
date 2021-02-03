auth = {
    "type": "object",
    "required": ["email", "password"],
    "properties": {
        "email": {
            "type": "string",
            "pattern": r"^$|^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        },
        "password": {"type": "string", "minLength": 3},
    }
}
