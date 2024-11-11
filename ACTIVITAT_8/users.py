import json

def get_users():
    with open("users.json", "r") as file:
        data = json.load(file)
    return data

def get_user(id: int):
    users = get_users()["users"]
    return [user for user in users if user["id"] == id][0]

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