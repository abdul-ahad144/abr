import pandas as pd
import os

FILE = "users.csv"

def load_users():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(FILE, index=False)
    else:
        df = pd.read_csv(FILE)

    return df


def register_user(username, password):
    df = load_users()

    if username in df["username"].values:
        return "User already exists"

    new_user = pd.DataFrame({
        "username": [username],
        "password": [password]
    })

    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(FILE, index=False)

    return "Registered Successfully"


def login_user(username, password):
    df = load_users()

    user = df[
        (df["username"] == username) &
        (df["password"] == password)
    ]

    if not user.empty:
        return "Login Successful"
    else:
        return "Invalid Credentials"
