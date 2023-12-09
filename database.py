from sqlite3 import connect


class Database():
    def __init__(self) -> None:
        self.db = connect('demo.db')
        self.cursor = self.db.cursor()

        self.tableCreate = """CREATE TABLE uagyz(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    message TEXT,
                                    time VARCHAR(255)
                            )"""
        
        self.insertUagys = """INSERT INTO uagyz(message, time) VALUES(?, ?)"""

        self.selectUagyz = "SELECT id, message, time FROM uagyz WHERE time = ?"
        
        self.selectAll = "SELECT id, message, time FROM uagyz"

        self.delete = "DELETE FROM uagyz WHERE id = ?"


    def createTable(self):
        self.cursor.execute( self.tableCreate)
        print("created uagyz table")

    def InsertData(self, msg, time):
        self.cursor.execute(self.insertUagys, (msg, time))
        self.db.commit()

    def Fetch(self, times: str):
        data = self.cursor.execute(self.selectUagyz, (times, ))  
         
        result_data = [[i[0], i[1]] for i in data] 

        return result_data   

    def FetchAll(self):
        data = self.cursor.execute(self.selectAll)  
         
        result_data = [[i[0], i[1], i[2]] for i in data] 

        return result_data    
    
    def Delete(self, id):
        self.cursor.execute(self.delete, (id, ))
        self.db.commit()
        
    
    
    

    

               

if __name__ == "__main__":
    db = Database()
    db.createTable()