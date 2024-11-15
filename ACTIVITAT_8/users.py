import json
from typing import Union

def get_users():
    with open("users.json", "r") as file:
        data = json.load(file)
    return data

def get_user(id: int):
    users = get_users().get("users", [])
    
    for user in users:
        if user.get("id") == id: return user
    return None

def create_user(name: str, last_name: str, age: int, gender: str, email: str, phone: int):
    users = get_users()

    new_id = max([user["id"] for user in users["users"]], default=0) +1
    new_user = {
        "id": new_id, 
        "name": name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone
    }

    users["users"].append(new_user)

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def update_user(id: int, name: str, last_name: str, age: int, gender: str, email: str, phone: int):
    users = get_users().get("users", [])

    new_user = {
        "id": id, 
        "name": name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone
    }

    found = False
    for i, user in enumerate(users):
        if user.get("id") == id:
            users[i] = new_user
            found = True
            break
    
    if found:
        with open("users.json", "w") as file:
            json.dump({"users": users}, file, indent=4)
        return new_user
    return None

def modify_user(id: int, key: str, value: Union[str, int]):
    users = get_users().get("users", [])

    found = False
    for i, user in enumerate(users):
        if user.get("id") == id:
            users[i][key] = value
            new_user = users[i]
            found = True
            break
    
    if found:
        with open("users.json", "w") as file:
            json.dump({"users": users}, file, indent=4)
        return new_user
    return None