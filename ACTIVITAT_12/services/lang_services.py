from db.connection import Connection

def formate(lang):
    return {
        "id": lang[0],
        "name": lang[1]
    }

def get_languages():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT * FROM Language"
        cursor.execute(query)

        languages = cursor.fetchall()

        return {"ok": True, "languages": [formate(lang) for lang in languages]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()


def add_language(lang):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO Language (id, name) VALUES (%s)"
        values = (lang.id, lang.name)
        
        cursor.execute(query, values)

        conn.commit()

        return {"ok": True, "msg": "Language added"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def update_language(lang):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "UPDATE Language SET name = %s WHERE id = %s"
        values = (lang.name, lang.id)
        
        cursor.execute(query, values)

        conn.commit()

        return {"ok": True, "msg": "Language updated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def delete_language(lang_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "DELETE Language WHERE id = %s"
        values = (lang_id)
        
        cursor.execute(query, values)

        conn.commit()

        return {"ok": True, "msg": "Language deleted"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()