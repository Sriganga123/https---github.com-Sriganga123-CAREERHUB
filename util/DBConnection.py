import mysql.connector as sql
class dbConnection:
    def open():
        try:
            conn = sql.connect(host="localhost", database="career2", user="root", password="sonamona624")
            stmt = conn.cursor()
            return conn, stmt
        except Exception as e:
            print(f"Database cannot connect: {e}")
            return None, None

    def close(conn):
        if conn:
            conn.close()