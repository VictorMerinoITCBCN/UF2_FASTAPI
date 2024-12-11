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