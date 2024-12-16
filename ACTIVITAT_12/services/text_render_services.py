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

def get_text_renders():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT DISTINCT base FROM TextRender"
        cursor.execute(query)

        bases = cursor.fetchall()

        return {"ok": True, "text_renders": [base[0] for base in bases]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def create_text_render(text_render):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        INSERT INTO TextRender (langID, base, text)
        VALUES (%s, %s, %s)
        """

        values = (text_render.lang_id, text_render.base, text_render.text)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Text created"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def update_text_render(text_render):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        UPDATE TextRender SET
        langID = %s,
        base = %s,
        text = %s
        WHERE id = %s
        """

        values = (text_render.lang_id, text_render.base, text_render.text, text_render.id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Text updated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def delete_text_render(base):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        DELETE FROM TextRender WHERE base = %s
        """

        values = (base, )

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Text deleted"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()