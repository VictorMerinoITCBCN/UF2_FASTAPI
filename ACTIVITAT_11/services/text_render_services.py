from db.connection import Connection

def get_text_render(base, lang):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT text FROM TextRender WHERE base = %s AND langID = %s"
        values = (base, lang)

        cursor.execute(query, values)

        text = cursor.fetchone()

        if not text:
            return {"ok": False, "error": f"Text with base: {base} in lang: {lang} not found"}
        
        return {"ok": True, "text": text[0]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()