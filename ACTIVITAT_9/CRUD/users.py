from db_connect.Connection import Connection

def formate(user):
    return {
        "id": user[0],
        "name": user[1],
        "last_name": user[2],
        "age": user[3],
        "email": user[4],
        "phone": user[5]
}

def get_all():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)

        users = cursor.fetchall()

        return {"ok": True, "users": [formate(user) for user in users]}
    except Exception as e:
        return {"ok": False, "Error": f"{e}"}
    finally:
        Connection.close()

def get(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE id = %s"

        cursor.execute(query, (id,))
        user = cursor.fetchone()

        return {"ok": True, "user": formate(user)}
    except Exception as e:
        return {"ok": False, "Error": f"{e}"}
    finally:
        Connection.close()

def create(user):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO users (name, last_name, age, email, phone) VALUES (%s, %s, %s, %s, %s) RETURNING id"
        values = (user.name, user.last_name, user.age, user.email, user.phone)

        cursor.execute(query, values)
        id = cursor.fetchone()[0]
        conn.commit()

        return {"ok": True, "id": id}
    except Exception as e:
        return {"ok": False, "Error": f"{e}"}
    finally:
        Connection.close()    

def update(id, user):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "UPDATE users SET name = %s, last_name = %s, age = %s, email = %s, phone = %s WHERE id = %s"
        values = (user.name, user.last_name, user.age, user.email, user.phone, id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "response": f"Usuari amb id: {id} actualitzat"}
    except Exception as e:
        return {"ok": False, "Error": f"{e}"}
    finally:
        Connection.close()    

def alter(id, columns):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "UPDATE users SET "
        values = []

        for column in columns:
            query += f"{column.key} = %s,"
            values.append(column.value)
        
        query = query.rstrip(",")
        query += "WHERE id = %s"
        values.append(id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": f"Usuari amb id: {id} modificat"}
    except Exception as e:
        return {"ok": False, "Error": f"{e}"}
    finally:
        Connection.close()    
    
def delete(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()

        return {"ok": True, "msg": f"Usuari amb id: {id} eliminat"}
    except Exception as e:
        return {"ok": False, "Error": f"{e}"}
    finally:
        Connection.close() 