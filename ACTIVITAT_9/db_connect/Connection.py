import psycopg2 

class Connection:

    _connection = None

    @staticmethod
    def connect():
        try:
            Connection._connection = psycopg2.connect(
                database="postgres",
                host="localhost",
                user="victor",
                password="super",
                port="5432"
            )
        except Exception as e:
            print(f"Error conectant a la base de dades: {e}")

    @staticmethod
    def get():
        if not Connection._connection: Connection.connect()
        return Connection._connection
    
    @staticmethod
    def close():
        if Connection._connection:
            Connection._connection.close()
            Connection._connection = None
        else: print("No hi ha cap connexió")