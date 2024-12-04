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
