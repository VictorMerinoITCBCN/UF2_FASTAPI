from db.connection import Connection

def formate(theme):
    return {
        "option" : theme[0]
    }

def get_themes():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT DISTINCT theme FROM word ORDER BY theme"

        cursor.execute(query)
        themes = cursor.fetchall()

        return [formate(theme) for theme in themes]
    except Exception as  e:
        return None
    finally:
        Connection.close()

def get_random_word(theme):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT word FROM word WHERE theme = %s ORDER BY RANDOM() LIMIT 1 "

        cursor.execute(query, (theme,))
        word = cursor.fetchone()

        return formate(word)
    except Exception as  e:
        return None
    finally:
        Connection.close()
