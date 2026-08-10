import json


def save(password: list[bytes]) -> None:
    with open('password.json', 'w') as f:
        json.dump(password, f)


def load_all() -> list[str]:
    try:
        with open("password.json", 'r') as f:
            data = json.load(f)
            return data

    except FileNotFoundError:
        print("File not found.")
        return []


def delete_all() -> None:
    with open("password.json", 'w') as f:
        json.dump([], f) 


def delete(index: int) -> None:
    data = load_all()
    if index < 0 or index >= len(data):
        print("Index out of range.")
    else:
        data.pop(index)
        save(data)




