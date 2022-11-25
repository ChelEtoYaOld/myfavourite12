import sqlite3
import hashlib
import random

def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()

with sqlite3.connect("database_users.db") as db:
    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name VARCHAR(30),
    age INTEGER (3),
    sex INTEGER NOT NULL DEFAULT 1,
    balance INTEGER NOT NULL DEFAULT 2000,
    login VARCHAR(15),
    password VARCHAR(20)
    );
    CREATE TABLE IF NOT EXISTS shop(
    name VARCHAR(50),
    balance BIGINT NOT NULL DEFAULT 10000
    )
    """
    cursor.executescript(query)

def registration():
    name = input('Name - ')
    age = int(input('Age - '))
    sex = int(input('Sex /men>1, woman>2/ - '))
    login = input('Login - ')
    password = input('Password - ')

    try:
        db = sqlite3.connect("data_users.db")
        cursor = db.cursor()

        db.create_function("md5", 1, md5sum)

        cursor.execute("SELECT login FROM users WHERE login = ?", [login])
        if cursor.fetchone() is None:
            values = [name, age, sex, login, password]
            cursor.execute("INSERT INTO users(name, age, sex, login, password) VALUES(?, ?, ?, ?, md5(?))", values)
            db.commit()

        else:
            print("Такой логин уже присутствует!")
            registration()
    except sqlite3.Error as exc:
        print("Error:", exc)
    finally:
        cursor.close()
        db.close()

def log_in():
    login = input('Login - ')
    password = input('Password - ')

    try:
        db = sqlite3.connect("data_users.db")
        cursor = db.cursor()

        db.create_function("md5", 1, md5sum)
        cursor.execute("SELECT login FROM users WHERE login = ?", [login])
        if cursor.fetchone() is None:
            print("Такого логина не существует!")
        else:
            cursor.execute("SELECT password FROM users WHERE login = ? AND password = md5(?)", [login, password])
            if cursor.fetchone() is None:
                print("Пароль не правильний!")
            else:
                play_shop(login)
    except sqlite3.Error as exc:
        print("Error", exc)
    finally:
        cursor.close()
        db.close()

def play_shop(login):
    print("\n\tSHOP")

    try:
        db = sqlite3.connect("data_users.db")
        cursor = db.cursor()

        cursor.execute("SELECT age FROM users WHERE login = ? AND age >= ?", [login, 18])
        if cursor.fetchone() is None:
            print("Ай ниид е Паспорт!")
        else:
            bet = int(input("Bet - "))
            number = random.randint(1, 100)

            balance = cursor.execute("SELECT balance FROM users WHERE login = ?", [login]).fetchone()[0]
            if balance < bet:
                print("Недостатньо коштів!")
            else:
                if number < 50:
                    cursor.execute("UPDATE users SET balance = balance - ? WHERE login = ?", [bet, login])
                    cursor.execute("UPDATE shop SET balance = balance + ?", [bet])

                    print("OK! Pokupka.")
                else:
                    cursor.execute("UPDATE users SET balance = balance + ? WHERE login = ?", [bet, login])
                    cursor.execute("UPDATE shop SET balance = balance - ?", [bet])

                    print("OK! Vozvrat!")
                db.commit()
    except sqlite3.Error as exc:
        print("Error: ", exc)
    finally:
        cursor.close()
        db.close()

registration()
log_in()