from db.connection import Connection

def get_keys(lang_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT character FROM Letter WHERE langID = %s"
        
        cursor.execute(query, (lang_id, ))

        keys = cursor.fetchall()

        return {"ok": True, "keys": keys}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def add_key(key):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO Key (langID, character) VALUES (%s, %s)"
        values = (key.lang_id, key.character)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Key added"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def update_key(key):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "UPDATE Key SET langID = %s, character = %s WHERE id = %s"
        values = (key.lang_id, key.character, key.id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Key updated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def delete_key(key_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "DELETE FROM Key WHERE id = %s"
        values = (key_id, )

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Key deleted"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()