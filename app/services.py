import os
import json

# 🔧 Always use /app/data to match Docker volume
DATA_FOLDER = "/app/data"
DATA_SOURCE = os.path.join(DATA_FOLDER, "users.json")

def check_dataset_exists():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(DATA_SOURCE):
        with open(DATA_SOURCE, "w") as f:
            f.write('{"data": []}')  # ✅ initialize properly

def read_usersdata():
    check_dataset_exists()
    with open(DATA_SOURCE, "r") as f:
        content = f.read()
        if content.strip() == "":
            content = '{"data": []}'  # fallback if file is empty
        users = json.loads(content)
    return users

def add_userdata(user: dict):
    users = read_usersdata()

    if "data" in users:
        users["data"].append(user)
    else:
        users["data"] = [user]

    with open(DATA_SOURCE, "w") as f:
        json.dump(users, f, indent=2)
