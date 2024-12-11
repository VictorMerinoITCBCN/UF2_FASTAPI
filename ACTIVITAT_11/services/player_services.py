from db.connection import Connection

def formate_player(player):
    return {
        "id": player[0],
        "name": player[1],
        "win": player[2],
        "lose": player[3],
        "bestScore": {
            "id": player[4],
            "score": player[5],
            "date": player[6]
        }
    }

def get_player(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT 
            p.id,
            p.name,
            p.win,
            p.lose,
            bs.id,
            bs.score,
            bs.date 
        FROM Player as p
        JOIN Score bs ON p.bestScoreID = bs.id
        WHERE p.id = %s
        """
        values = (id ,)

        cursor.execute(query, values)
        player = cursor.fetchone()

        if not player:
            return {"ok": False, "error": "Player not found"}
        
        return {"ok": True, "player" : formate_player(player)}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()