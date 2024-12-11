from db.connection import Connection

def formate_word(word):
    return {
        "id": word[0],
        "word": word[1]
    }

def get_words(theme, lang_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
          w.id,
          w.word 
        FROM Word as w 
        JOIN Theme t ON t.id = w.themeID
        WHERE UPPER(t.theme) = %s
        AND w.langID = %s 
        """
        values = (theme, lang_id)

        cursor.execute(query, values)

        words = cursor.fetchall()

        return {"ok": True, "words": [formate_word(word) for word in words]}

    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def get_random_word(theme, lang_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            w.id,
            w.word
        FROM Word as w
        JOIN Theme t ON t.id = w.themeID
        WHERE w.langID = %s
        AND UPPER(t.theme) = %s
        ORDER BY RANDOM() LIMIT 1
        """

        cursor.execute(query, (lang_id, theme))

        word = cursor.fetchone()

        return {"ok": True, "word": formate_word(word)}

    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()