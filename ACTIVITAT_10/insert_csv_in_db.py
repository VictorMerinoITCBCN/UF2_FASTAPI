import pandas as pd
from db.connection import Connection

def get_entries(csv_path):
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="list")

def insert_entries(entries):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO word (word, theme) VALUES"
        values = []

        for i in range(len(entries["WORD"])):
            query += "(%s, %s),"
            values.append(entries["WORD"][i])
            values.append(entries["THEME"][i])

        query = query.rstrip(",")
        
        cursor.execute(query, values)
        conn.commit()

        print(f"Added  {len(entries["WORD"])} words")

    except Exception as e:
        print(f"Error: {e}")

entries = get_entries("words.csv")
insert_entries(entries)