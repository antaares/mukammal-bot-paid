import sqlite3





class Database:
    #  the constructor of the class
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db
    


    # the property that returns the connection to the database
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
    

    # the method that executes the query
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    


    
    




    # create a table of Users in the database
    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            full_name TEXT
            );
            """
        self.execute(sql, commit=True)

    # create a table of Groups in the database
    def create_table_groups(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Groups (
            id INTEGER PRIMARY KEY,
            owner_id INTEGER
            );
            """
        self.execute(sql, commit=True)
    


    def create_table_black_list(self):
        sql = """
        CREATE TABLE IF NOT EXISTS black_list (
            id INTEGER PRIMARY KEY,
            chat_id INTEGER,
            word TEXT
            );
            """
        self.execute(sql, commit=True)
    

    


    # create a table of Scheduler's Job-id in the database
    def create_table_scheduler(self):
        sql = """
        CREATE TABLE IF NOT EXISTS scheduler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id TEXT UNIQUE,
            user_id INTEGER
            );
            """
        self.execute(sql = sql, commit=True)
    


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    

    # add a user to the database
    def add_user(self, user_id: int, full_name: str):
        sql = "INSERT OR IGNORE INTO users (id, full_name) VALUES (?, ?)"
        self.execute(sql, (user_id, full_name), commit=True)
    


    # add a group to the database
    def add_group(self, group_id: int, owner_id: int):
        sql = "INSERT OR IGNORE INTO Groups (id, owner_id) VALUES (?, ?)"
        self.execute(sql, (group_id, owner_id,), commit=True)

    def get_group(self, group_id: int):
        sql = "SELECT owner_id FROM Groups WHERE id = ?"
        res = self.execute(sql, (group_id,), fetchone=True)
        if res:
            return res
        return None
    
    def update_group(self, group_id: int, owner_id: int):
        sql = "UPDATE Groups SET owner_id = ? WHERE id = ?"
        self.execute(sql, (owner_id, group_id,), commit=True)

    

    # add a job_id to the database
    def add_job_id(self, user_id: int):
        sql = "INSERT INTO scheduler (job_id, user_id) VALUES (?, ?)"
        job_id = self.unique_id(user_id)
        self.execute(sql, (job_id, user_id), commit=True)
    

    #  delete job_id from the database
    def delete_job_id(self, user_id: int):
        sql = "DELETE FROM scheduler WHERE user_id = ?"
        self.execute(sql, (user_id,), commit=True)

    def get_user_job(self, user_id: int):
        sql = "SELECT job_id FROM scheduler WHERE user_id = ?"
        res = self.execute(sql, (user_id,), fetchone=True)
        if res:
            return res[0]
        return None

    # get a user from the database
    def all(self):
        sql = "SELECT id FROM users"
        all = self.execute(sql, fetchall=True)
        return [item[0] for item in all]


    # get a group from the database
    def all_groups(self):
        sql = "SELECT id FROM Groups"
        all = self.execute(sql, fetchall=True)
        return [item[0] for item in all]
    

    def get_groups_by_admin(self, user_id: int, ):
        sql = "SELECT id FROM Groups WHERE owner_id = ?"
        all = self.execute(sql, (user_id,), fetchall=True)
        return [item[0] for item in all]
    



    def add_black_word(self, chat_id: int, word: str):
        sql = """INSERT OR IGNORE INTO black_list (chat_id, word) VALUES (?, ?)"""
        self.execute(sql, (chat_id, word), commit=True)
    
    def get_black_list(self, chat_id: int):
        sql = """SELECT word FROM black_list WHERE chat_id = ?"""
        response = self.execute(sql, (chat_id,), fetchall=True)
        if response:
            return [item[0] for item in response]
        return None
    
    def delete_black_word(self, chat_id: int, word: str):
        sql = """DELETE FROM black_list WHERE chat_id = ? AND word = ?"""
        self.execute(sql, (chat_id, word), commit=True)
    

    def delete_black_words(self, chat_id: int):
        sql = """DELETE FROM black_list WHERE chat_id = ?"""
        self.execute(sql, (chat_id,), commit=True)
        




    # create unique job_id
    def unique_id(self, user_id: int):
        return f"id{user_id}"
    
