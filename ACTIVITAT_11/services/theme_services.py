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