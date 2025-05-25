"""
Database_transfer.py
====================

Started: 24.04.25
Updated: 30.04.25
====================
"""
import sqlite3 
import os 
from datetime import datetime

from dependencies.Tools import Record  

class Database_transfer(): 
    """
    Used to perform operations related to the database.
    """
    def __init__(self, path_to_db:str):
        self.db_path = path_to_db
        self._db_connection = None 
        self._cursor = None

        ### creating tables if is doesnt exist 
        if len(self._get_all_tables()) == 0:
            print("No tables found")
            print("Creating tables...")
            self._quick_create()
            self._display_tables1()

        ### getting the user
        self.user = None 
        if self.get_record("User", "user_name", "user1") != None: 
            self.user = self.get_record("User", "user_name", "user1")
    # -----------------------------
    
    def _connect(self) -> None:
        '''
        Established a connection to the database
        '''
        self._db_connection = sqlite3.connect(self.db_path)
        self._cursor = self._db_connection.cursor()
        print(f"\nConnected to database, '{self.db_path}'")
        
    def _terminate(self) -> None: 
        '''
        Terminates the connection with the database
        '''
        self._cursor.close()        
        self._db_connection.close()
        print("\nConnection terminated")
        
    def _display_tables(self) -> None: 
        '''
        View all records in a specific table
        ''' 
        self._connect()
        query = """
            SELECT name FROM sqlite_schema
            WHERE type='table'
            ORDER BY name
        """

        self._cursor.execute(query)
        all_tables = self._cursor.fetchall()
        self._terminate()
        print(f"\nAll tables in '{self.db_path}'")
        print(all_tables)
        # print(t[0] for t in all_tables)
        for t in all_tables[:-1]:
            print(f"- {t[0]}")
        
    def _display_tables1(self) -> None: 
        '''
        View all records in a specific table
        ''' 
        self._connect()
        query = """
            SELECT name FROM sqlite_schema
            WHERE type='table'
        """
        self._cursor.execute(query)
        all_tables = self._cursor.fetchall()
        print(f"\nAll tables in '{self.db_path}'")
      
        # ---help from chatgpt--- 
        # Step 2: For each table, get the list of columns
        for table in all_tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")
            self._cursor.execute(f"PRAGMA table_info({table_name});")
            columns = self._cursor.fetchall()
            print("Columns:")
            # print(columns)
            for col in columns:
                # col[1] is column name, col[2] is data type
                print(f"  {col[1]} ({col[2]})")

        self._terminate()
    
    
    def _quick_create(self) -> None: 
        '''
        Reads a SQL script from a .sql file and creates
        the tables that are in that file.
        '''
        self._connect()
        database_file = "dependencies/_schema.sql"
        # database_file = "_schema.sql"
        
        if self._db_connection is None or self._cursor is None:
            print("\nDatabase not connected. Establishing connection...")
        else:         
            if (os.path.exists(database_file)): 
                print("\nCreating tables...")
                tables = open(database_file, "r").read()
                print(tables)
                self._cursor.executescript(tables)
                print("\nTables created")

                ### create user 
                self.insert_record_auto("User", ("user1", "password1"))

                ### get user 
                user = self.get_record("User", "user_name", "user1")
                print(f"User created \n- {user}\n")
                
                self._display_tables()
                
            else:
                print(f"\nFile not found '{database_file}'")
                self._terminate()
    # -----------------------------
    
    ### INSERT
    def insert_record_auto(self, table:str, record:tuple) -> None: 
        '''
        Adds a new record to a specific table. 
        Also checks the length of the 'record' tuple.
        Used for auto-incremented keys
        '''
        self._connect()
        record_lengths = {
            1: f"INSERT INTO {table} VALUES (null, ?)", 
            2: f"INSERT INTO {table} VALUES (null, ?, ?)", 
            3: f"INSERT INTO {table} VALUES (null, ?, ?, ?)", 
            4: f"INSERT INTO {table} VALUES (null, ?, ?, ?, ?)", 
            5: f"INSERT INTO {table} VALUES (null, ?, ?, ?, ?, ?)", 
            6: f"INSERT INTO {table} VALUES (null, ?, ?, ?, ?, ?, ?)"
        }
        insert_op = (record_lengths[len(record)])
        
        self._cursor.execute(insert_op, record)
        self._db_connection.commit()
        self._terminate()
    # -----------------------------
    
    ### READ 
    def _get_all_tables(self) -> list: 
        '''
        View all records in a specific table
        ''' 
        self._connect()
        query = """
            SELECT name FROM sqlite_schema
            WHERE type='table'
            ORDER BY name
        """

        self._cursor.execute(query)
        all_tables = self._cursor.fetchall()
        self._terminate()
        return all_tables 
    

    def get_all_records(self, table:str) -> None | list: 
        '''
        View all records in a specific table
        ''' 
        self._connect()
        self._cursor.execute(f"SELECT * FROM {table}")
        all_records = self._cursor.fetchall()
        self._terminate()
        all_records.reverse()
        return all_records
    
    def get_record(self, table:str, attribute_name:str, attribute_value:str | int) -> any: 
        '''
        Finds a returns a record with a specific attribute-value from a specific table
        '''
        self._connect()
        self._cursor.execute(f"SELECT * FROM {table} WHERE {attribute_name} = ?", (attribute_value,))
        record = self._cursor.fetchone()
        self._terminate()
        return record 
    
    def get_records(self, table:str, attribute_name:str, attribute_value) -> any: 
        '''
        Finds a returns records with a specific attribute-value from a specific table
        '''
        self._connect()
        query = f"""
        SELECT * FROM {table} 
        WHERE {attribute_name}=?
        """
        self._cursor.execute(query, (attribute_value,))
        records = self._cursor.fetchall()
        records.reverse()
        self._terminate()
        return records 
    
    # overload 
    # def get_records1(self, table:str, attribute_name:str, attribute_value, num_of_videos) -> any: 
    #     '''
    #     Finds a returns records with a specific attribute-value from a specific table
    #     '''
    #     self._connect()
    #     query = f"""
    #     SELECT * FROM {table} 
    #     WHERE {attribute_name}=?
    #     """
    #     self._cursor.execute(query, (attribute_value,))
    #     records = self._cursor.fetchall()
    #     # print(num_of_videos)
    #     # print(records)
    #     records.reverse()

    #     # print(records[0:num_of_videos])
    #     self._terminate()

    #     return records[0:num_of_videos] 

    # def get_fav_videos(self, table:str, attribute_name:str, attribute_value, is_fav) -> any: 
    # def get_fav_videos(self, table:str, attribute_name:str, attribute_value) -> any: 
    #     '''
    #     Finds a returns records with a specific attribute-value from a specific table
    #     '''
    #     self._connect()
    #     query = f"""
    #     SELECT * FROM {table} 
    #     WHERE {attribute_name}=? AND is_favorite=True
    #     """
    #     self._cursor.execute(query, (attribute_value,))
    #     records = self._cursor.fetchall()
    #     records.reverse()
    #     self._terminate()
    #     return records 
    
    def get_fav(self, table:str, attribute_name:str, attribute_value) -> any: 
        '''
        Finds a returns records with a specific attribute-value from a specific table
        '''
        self._connect()
        query = f"""
        SELECT * FROM {table} 
        WHERE {attribute_name}=? AND is_favorite=True
        """
        self._cursor.execute(query, (attribute_value,))
        records = self._cursor.fetchall()
        records.reverse()
        self._terminate()
        return records 
    
    # ------------------------------------
    
    ### UPDATE 
    def update(self, 
               table:str, 
               pk_col:str, 
               pk_value: int | str, 
               cols:list, 
               values:list
               ) -> None:
        self._connect()

        ### creating a query 
        query = f"UPDATE {table} SET {cols[0]}=?"
        for col in cols[1::]:
            query += f", {col}=?"
        query += f" WHERE {pk_col}=?"
      
        values.append(pk_value)  
        self._cursor.execute(query, tuple(values)) 
        self._db_connection.commit()
        print("***Updated successfully***")
        self._terminate()
    # ------------------------------------
        
    ### DELETE 
    def delete(self, table:str, attribute_name:str, attribute_value:str | int) -> None:
        ### Save record to text file 
        file_name = "_deleted.del" # hide this file? 
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M")
        record = self.get_record(table, attribute_name, attribute_value)
        line = 40 * "-"
        Record.append_to_file(file_name, f"{formatted_date}\n")
        Record.append_to_file(file_name, f"{record}\n")
        Record.append_to_file(file_name, f"{line}\n\n")

        ### Delete record 
        self._connect()
        self._cursor.execute(f"DELETE FROM {table} WHERE {attribute_name} = ?", (attribute_value,))
        self._db_connection.commit()
        print("***Deleted successfully***")
        self._terminate()
    # ------------------------------------
  
# ====================================================
# END 
# ====================================================
