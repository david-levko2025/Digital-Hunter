import mysql.connector
from shared.core.config import settings
from shared.log.logger import log_event

class ConnectionTOSQL:
    def __init__(self):
        self.config ={
            'host': settings.NYSQL_HOST,
            'port': settings.NYSQL_PORT,
            'user': settings.NYSQL_USER,
            'password': settings.NYSQL_PASSWORD,
        }

        self.db_name = settings.NYSQL_DB

    def get_connection(self,include_db=True):
        config = self.config.copy()
        if include_db:
            config["database"] = self.db_name
            return mysql.connector.connect(**config)
        
    def init_db(self):
        conn = self.get_connection(include_db=False)
        cursor = conn.cursor()  # type: ignore
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
            cursor.execute(f"USE {self.db_name}")
            cursor.execute("""CREATE TABLE IF NOT EXISTS targets(
                                entity_id VARCHAR(255) PRIMARY KEY
                                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                signal_id VARCHAR(255)
                                reported_lat FLOAT
                                reported_lon FLOAT
                                signal_type VARCHAR(10)
                                priority_level INT
                                
                        """)
            cursor.execute("""CREATE TABLE IF NOT EXISTS attacks(
                                attack_id VARCHAR(255) PRIMARY KEY
                                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                entity_id VARCHAR(255)
                                weapon_type VARCHAR(255)
                                FOEIGEN KEY (entity_id) 
                                REFRENCES targets (entity_id)
                        """)
            cursor.execute("""CREATE TABLE IF NOT EXISTS damage(
                                attack_id VARCHAR(255) PRIMARY KEY
                                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                entity_id VARCHAR(255)
                                result VARCHAR(255)
                                FOEIGEN KEY (entity_id) 
                                REFRENCES attacks (entity_id)
                    """)
            conn.commit()  # type: ignore
            log_event("INFO","the database and 3 tabels inside sucessfully","database-manager")
        except Exception as e:
            log_event("ERROR",f"databse init error : {e}","database-manager")
            cursor.close()
            conn.close()  # type: ignore


    def get_target(self,entity_id):
        conn = self.get_connection()
        if not conn:
            return None
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM TARGETS WHERE entity_id = %s",(entity_id))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close() 

    def upsert_targerts(self,entity_id,lat,lon,priority,signal_type):
        conn = self.get_connection()
        if not conn:
            return 
        cursor = conn.cursor()
        try:
            query = """
                    INSERT INTO targets
                    (entity_id,lat,lon,priority,signal_type) VALUES
                    (%s, %s, %s, %s, %s)
        """
            cursor.execute(query,(entity_id,lat,lon,priority,signal_type))
            conn.commit()
        finally:
            cursor.close()
            conn.close() 

    def insert_attack(self,attack_id,entity_id,weapon_type):
        conn = self.get_connection()
        if not conn:
            return 
        cursor = conn.cursor()
        try:
            query = """
                    INSERT INTO attacks
                    (attack_id,entity_id,weapon_type) VALUES
                    (%s, %s, %s)
        """
            cursor.execute(query,(attack_id,entity_id,weapon_type))
            conn.commit()
        finally:
            cursor.close()
            conn.close() 

    def insert_damage_reports(self, attack_id,entity_id,result):
        conn = self.get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT attack_id FROM attacks WHERE attack_id = %s",(attack_id))
            if not cursor.fetchone():
                return False
            query = "INSERT INTO damage (attack_id,entity_id,result) VALUES (%s, %s, %s)"
            cursor.execute(query,(attack_id,entity_id,result))
            if result == "destroyed":
                cursor.execute("UPDATE targets SET result = 'destroyed' WHERE entity_id = %s",(entity_id))
                conn.commit()
                return True
        except Exception as e:
            log_event("ERROR",f"insert damage fail: {e}","database-manager")
            return False
        
        finally:
            cursor.close()
            conn.close()

            

