import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "secret", 
    database = "library_db"
    )
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    books = """CREATE TABLE if not exists books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titel varchar(50) NOT NULL,
        author varchar(50) NOT NULL,
        genre varchar(255) NOT NULL,
        is_available INT NOT NULL,
        borrowed_by_member_id INT);"""
    
    members = """CREATE TABLE members ( 
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name  VARCHAR(50) NOT NULL,
            email VARCHAR(255) UNIQUE,  
            name VARCHAR(255) NOT NULL, 
            is_active BOOL NOT NULL,
            total_borrows INT NOT NULL  );"""
    cursor.execute(books)
    cursor.execute(members)
    conn.commit()
    cursor.close()
    conn.close()




