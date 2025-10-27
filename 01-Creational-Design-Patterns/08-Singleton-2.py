class DatabaseConnection:
    _instance = None

    def __new__(cls, db_name, host, port):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_name, host, port):
        if not hasattr(self, '_initialized') or not self._initialized:
            self._db_name = db_name
            self._host = host
            self._port = port
            self._connection = self._initialize_connection()
            self._initialized = True

    def _initialize_connection(self):
        connection_string = f"Connected to {self._db_name} at {self._host}:{self._port}"
        return connection_string

    def get_connection(self):
        return self._connection

    def close_connection(self):
        print(f"Connection to {self._db_name} closed.")
        DatabaseConnection._instance = None
        self._initialized = False

    def __str__(self):
        return f"DatabaseConnection(db_name={self._db_name}, host={self._host}, port={self._port})"

if __name__ == "__main__":

    db1 = DatabaseConnection("MyDatabase", "localhost", 5432)
    print(db1.get_connection())

    db2 = DatabaseConnection("AnotherDatabase", "localhost", 5432)
    print(db2.get_connection())

    print(db1 is db2)
    print(db1)
    print(db2)

    db1.close_connection()

    db3 = DatabaseConnection("AnotherDatabase", "localhost", 5432)
    print(db3.get_connection())