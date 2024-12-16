from db.connection import Connection

def formate_theme(theme):
    return {
        "id": theme[0],
        "theme": theme[1]
    }

def get_themes(lang_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT id, theme FROM Theme WHERE langID = %s"

        cursor.execute(query, (lang_id, ))
        themes = cursor.fetchall()

        return {"ok": True, "themes": [formate_theme(theme) for theme in themes]}

    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def create_theme(theme):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        INSERT INTO Theme (langID, theme)
        VALUES (%s, %s)
        """

        values = (theme.lang_id, theme.theme)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Theme created"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def update_theme(theme):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        UPDATE Theme SET 
        langID = %s
        theme = %s
        WHERE id = %s
        """

        values = (theme.lang_id, theme.theme, theme.id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Theme updated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def delete_theme(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        DELETE FROM Theme WHERE id = %s
        """

        values = (id, )

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Theme deleted"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()