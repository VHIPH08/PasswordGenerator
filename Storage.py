import json

def save(password:list[bytes]) -> None:
    with open('password.json', 'w') as f:
        json.dump(password, f)

def load_all() -> list[str] | None:
    try:
        with open("password.json", 'r') as f:
            data = json.load(f)
            return data

    except FileNotFoundError:
        print("File not found.")

def delete_all() -> None:
    try:
        with open("password.json", 'w') as f:
            f.write("{}")

    except FileNotFoundError:
        print("File not found.")

def delete(index:int) -> None:

    data = load_all()
    if index > len(data):
        print("Index out of range.")
    else:
        data.pop(index)
        save(data)


