import mysql.connector

class MysqlDB:
    def __init__(self,host,user,password,database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
           
    def select(self,select_sql = '',values=None):  
        try:
            # 查询操作
            self.cursor.execute(select_sql,values)#("SELECT * FROM your_table")
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"select error:{e}")
            return False 

    def insert(self,insert_sql='',values=None):
        # 插入操作
        """ insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
        values = ("value1", "value2") """
        try:
            self.cursor.execute(insert_sql,values)
            return True
        except Exception as e:
            print(f"insert error:{e}")
            return False

    def update(self,update_sql='',values=None):
        """# 更新操作
        update_query = "UPDATE your_table SET column1 = %s WHERE column2 = %s"
        new_value = "new_value"
        old_value = "value2" """
            
        try:            
            self.cursor.execute(update_sql,values)
            return True
        except Exception as e:
            print(f"update error:{e}")
            return False
            
    def delete(self,delete_sql = '',values=None):
        """ delete_query = "DELETE FROM your_table WHERE column1 = %s"
        value_to_delete = "value1" """
        try:
            self.cursor.execute(delete_sql,values)
            return True
        except Exception as e:
            print(f"delete error:{e}")
            return False     
    
    def start_transaction(self):
        self.conn.start_transaction()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close() 
        self.conn.close()
