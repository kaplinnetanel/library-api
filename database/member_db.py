from database.db_connection import get_connection
import logging

logger = logging.getLogger(__name__)


class MemberDB:

    def create_member(self,data):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql = """INSERT INTO members (name,email,is_active,total_borrows)
        VALUES (%s,%s,%s,%s);"""
        cursor.execute(sql,(data["name"],data["email"],True,0))
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_members(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary= True)
        logger.info("Sending a request to the database")
        cursor.execute("SELECT * FROM members;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
    def get_member_by_id(self,id) :
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        logger.info("Sending a request to the database")
        cursor.execute("SELECT * FROM members WHERE id = %s;",(id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def update_member(self, id, data):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql = "UPDATE members SET name = %s, email = %s WHERE id = %s;"
        cursor.execute(sql, (data["name"], data["email"], id))
        conn.commit()
        cursor.close()
        conn.close()

    def deactivate_member(self,id):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql =  "UPDATE members SET is_active=False WHERE id = %s; "
        cursor.execute(sql,(id))
        conn.commit()
        cursor.close()
        conn.close()

    def activate_member(self,id) :
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql =  "UPDATE members SET is_active=True WHERE id = %s; "
        cursor.execute(sql,(id,))
        conn.commit()
        cursor.close()
        conn.close()

    def increment_borrows(self,id) :
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql1 = "SELECT total_borrows FROM members WHERE id = %s;"
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        if result:
            t_borrows = result[0] + 1 
            sql =  "UPDATE members SET total_borrows = %s WHERE id = %s; "
            cursor.execute(sql,(t_borrows,id))
            conn.commit()
        cursor.close()
        conn.close()

    def  count_active_members(self) :
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        sql1 = "SELECT count(*) FROM members WHERE is_active=True;"
        resolt = cursor.fetchone()
        active  =  resolt + 1 
        cursor.close()
        conn.close()
        return active
    
    def get_top_member(self):
        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Sending a request to the database")
        cursor.execute("SELECT MAX(total_borrows) FROM members;")
        best_borrows = cursor.fetchone()
        b_borrows = best_borrows[0]
        if not b_borrows:
            cursor.close()
            conn.close()
            return None

        sql = "SELECT * FROM members WHERE total_borrows = %s;"
        cursor.execute(sql,(b_borrows,))
        b = cursor.fetchone()
        cursor.close()
        conn.close()
        return b




