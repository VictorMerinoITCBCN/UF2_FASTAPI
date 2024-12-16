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

def get_players():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT * FROM Player"

        cursor.execute(query)

        players = cursor.fetchall()

        return {"ok": True, "players": [formate_player(player) for player in players]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def add_player(player):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO Player (name) values (%s)"
        values = (player.name)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Player added"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def update_player(player):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        UPDATE Player SET 
        name = %s,
        win = %s, 
        lose = %s, 
        bestScoreID = %s 
        WHERE id = %s
        """
        values = (player.name, player.win, player.win, player.best_score_id, player.id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Player updated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def delete_player(player_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "DELETE Player WHERE id = %s"

        cursor.execute(query, (player_id, ))
        conn.commit()

        return {"ok": True, "msg": "Player updated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()