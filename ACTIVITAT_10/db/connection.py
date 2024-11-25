import psycopg2

class Connection:

    _connection = None

    @staticmethod
    def connect():
        try:
            Connection._connection = psycopg2.connect(
                host = "localhost",
                port = "5432",
                dbname = "words",
                user = "admin",
                password = "super"
            )
        except Exception as e:
            print(f"Error connecting the data base: {e}")

    @staticmethod
    def get():
        if not Connection._connection: Connection.connect()
        return Connection._connection
    
    @staticmethod
    def close():
        if Connection._connection:
            Connection._connection.close()
            Connection._connection = None