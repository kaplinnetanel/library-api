
from database.db_connection import get_connection
import mysql
import logging

logger = logging.basicConfig(filename='myapp.log', level=logging.INFO,format= "%(asctime)s %(levelname)s %(message)s" )

logger = logging.getLogger(__name__)

class BOOKDB:
    def create_book(self,titel:str,author:str,genre:str):
        conn = get_connection()
        cursor = conn.cursor()
        sql =("INSERT INTO books (titel,author,genre,is_available,borrowed_by_member_id)VALUES (%s,%s,%s,%s,%s);")
        cursor.execute(sql,(titel,author,genre,True,None))
        conn.commit()
        cursor.close()
        conn.close()
        conn.close()
        return "The book was created"
        
    def get_all_books(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary= True)
        logger.info("Sending a request to the database")
        cursor.execute("SELECT * FROM books;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_book_by_id(self,id):
        conn = get_connection()
        cursor = conn.cursor(dictionary= True)
        logger.info("Sending a request to the database")
        cursor.execute("SELECT * FROM books WHERE id = %s",(id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def update_book(self,id:int,body : dict):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql = """UPDATE books 
             SET title = %s, author = %s, genre = %s, is_available = %s, borrowed_by_member_id = %s 
             WHERE id = %s;"""
        cursor.execute(sql, (body["titel"],body["author"], body["genre"],body["is_available"], body["borrowed_by_member_id"],id))
        conn.commit()
        cursor.close()
        conn.close()

    def set_available(self,id : int , val ,number_id ):
        conn = get_connection()
        cursor = conn.cursor(dictionary= True)
        try:
            if val == "return":
                logger.info("Sending a request to the database")
                sql =""" UPDATE books 
                SET title =  is_available = True , borrowed_by_member_id = NULL
                WHERE id = %s;"""
                cursor.execute(sql,(id,))
                conn.commit()
                cursor.close()
                conn.close()

            elif val == "borrow":
                logger.info("Sending a request to the database")
                cursor.execute("SELECT is_active ,borrowed_by_member_id FROM books WHERE id = %s")
                active = cursor.fetchone()
                i_active = active[0]
                number = active[1]
                if i_active and number < 4:
                    sql =""" UPDATE books 
                    SET  is_available = False, borrowed_by_member_id = %s ,
                    WHERE id = %s;"""
                    cursor.execute(sql,(number_id,id))
                    conn.commit()
                    cursor.close()
                    conn.close()
                else:
                    raise ValueError("The book is already taken.") 
        except Exception as e:
            logger.error("Not sent to correct val")
            print(e)
    
    
    def count_total_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        cursor.execute("SELECT COUNT(*)FROM books ;")
        result = cursor.fetchone()
        count = result[0]
        cursor.close()
        conn.close()
        return count

    def count_available_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        cursor.execute("SELECT COUNT(*)FROM books WHERE is_available=True;")
        result = cursor.fetchone()
        count = result[0]
        cursor.close()
        conn.close()
        return count

    def count_borrowed_books(self): 
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        cursor.execute("SELECT COUNT(*)FROM books WHERE is_available=False;")
        result = cursor.fetchone()
        count = result[0]
        cursor.close()
        conn.close()
        return count

    def count_by_genre(self,genre:str):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql = "SELECT COUNT(*)FROM books WHERE genre=%s;"
        cursor.execute(sql,(genre,))
        result = cursor.fetchone()
        count = result[0]
        cursor.close()
        conn.close()
        return count

    def count_active_borrows_by_member(self,member_id):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql = "SELECT COUNT(*) FROM books WHERE active = True AND member_id = %s;"
        cursor.execute(sql,(member_id,))
        result = cursor.fetchone()
        count = result[0]
        cursor.close()
        conn.close()
        return count
