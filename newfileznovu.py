import sqlite3

with sqlite3.connect("database_learn_2.db") as db:
    cursor = db.cursor()
    '''
    cursor.execute("""CREATE TABLE data_new(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firm VARCHAR,
    model VARCHAR,
    content TEXT
    )""")
    '''

    values = [
        ("APPLE", "IPHONE14", "New model ..."),
        ("Samsung", "S22", "Good model ..."),
        ("Nokia", "C41", "Woker model ....")
    ]

    cursor.executemany("INSERT INTO data_new(firm, model, content) VALUES(?, ?, ?)", values)

    cursor.execute("SELECT * FROM data_new")
    #print(cursor.fetchone())
    #print(cursor.fetchone())
    #print(cursor.__next__())
    #print(cursor.fetchall())
    #print(cursor.fetchmany(4))

    # variant 2
    '''
    for data in cursor.execute("SELECT * FROM data_new"):
        print(data)
        print(data[1])
        print(data[2])
    '''
    # variant 3
    for data in cursor.execute("SELECT firm, model FROM data_new"):
        print(data)
