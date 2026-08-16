import sqlite3
DB_NAME = "jobs.db"

ALLOWED_TABLES = {
    "applications",
    "companies",
    "notes"
}


def validate_table(table):
    if table not in ALLOWED_TABLES:
        raise ValueError(f"Invalid table: {table}")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            status TEXT NOT NULL
            )
        """,
        """
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (application_id)
                REFERENCES applications(id)
        ) 
        """
    ]

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            print('DB Init')

            # Execute a query to get the SQLite version
            query = 'SELECT sqlite_version();'
            cursor.execute(query)

            # Fetch and print the result
            result = cursor.fetchall()
            print('SQLite Version is {}'.format(result[0][0]))

            for query in queries:
                cursor.execute(query)

            conn.commit()
    except sqlite3.Error as error:
        print(f"Database initialization error -: {error}")

def insert(table, data):
    validate_table(table)

    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    values = tuple(data.values())

    query = f"""
        INSERT INTO {table} ({columns})
        VALUES ({placeholders})
    """

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()

            return cursor.lastrowid

    
    except sqlite3.Error as error:
        print(f"Insert error: ", {error})
        return None

def fetch_all(table, where=None, params=()):
    validate_table(table)

    query = f"SELECT * FROM {table}"

    if where:
        query += f" WHERE {where}"

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Fetch error: {error}")
        return []

def update(table, data, where, params=()):
    validate_table(table)

    set_caluse = ", ".join(
        f"{column} = ?"
        for column in data.keys()
    )

    values = tuple(data.values()) + tuple(params)

    query = f"""
        UPDATE {table}
        SET {set_caluse}
        WHERE {where}
    """

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()

            return cursor.rowcount

    except sqlite3.Error as error:
        print(f"Update error: {error}")
        return 0
    
def delete(table, where, params=()):
    validate_table(table)
    
    query = f"""
        DELETE FROM {table}
        WHERE {where}
    """

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

            return cursor.rowcount
    except sqlite3.Error as error:
        print(f"Delete error: {error}")
        return 0

def drop_tables(db, tables=None, drop_all=False):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()

            if drop_all:
                cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='table';"
                )

                tables = [
                    row[0]
                    for row in cursor.fetchall()
                    if row[0] != "sqlite_sequence"
                ]

            if tables:
                for table in tables:
                    cursor.execute(
                        f"DROP TABLE IF EXISTS {table}"
                    )
                    print(f"'{table}' table dropped.")

                conn.commit()
                print("Selected tables dropped successfully.")

            else:
                print("No tables to drop.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")



