import psycopg2
from datetime import date

class database:
    connection = 0
    cursor = 0
    allStocks = []
    def __init__(self):
        try:
            self.connect()
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            # Print PostgreSQL Connection properties
            # print ( connection.get_dsn_parameters(),"\n")
            print("You are connected to - ", record,"\n")

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(self.connection):
                    self.cursor.close()
                    self.connection.close()
                    print("PostgreSQL connection is closed")
    def connect(self):
        self.connection = psycopg2.connect(user = "postgres",
                            password = "postgres",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "store")

        self.cursor = self.connection.cursor()

    def executeQUery(self, queryText):
        try:
            self.connect()
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

        # if(queryText.len() > 0):
        self.cursor.execute(queryText)
        record = self.cursor.fetchall()
        print("You are connected to - ", record,"\n")
        # else:
        #     # Print PostgreSQL version
        #     self.cursor.execute("SELECT version();")
        #     record = self.cursor.fetchone()
        try:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

        return record

    def getStocks(self, newRecord = False):
        if(len(self.allStocks) == 0 or newRecord is True):
            try:
                self.connect()
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

            # if(queryText.len() > 0):
            print ("going \n")
            self.cursor.execute("""SELECT * from stock""")
            record = self.cursor.fetchall()
            # else:
            #     # Print PostgreSQL version
            #     self.cursor.execute("SELECT version();")
            #     record = self.cursor.fetchone()
            try:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

            self.allStocks = record
            return self.allStocks

        return self.allStocks

    def insert_page2(self, loc, partNo, BoxNo):
        try:
            self.connect()
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

        postgres_insert_query = """ INSERT INTO stock (locations, part_number, box_number, type_tranx, created_by, is_active, created_date, remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (loc, partNo, BoxNo, 'IN', 'pa', 'true', date.today(), 'test')
        self.cursor.execute(postgres_insert_query, record_to_insert)

        self.connection.commit()
        
        self.cursor.execute('SELECT LASTVAL()')
        lastid = self.cursor.fetchone()[0]
        print("status : " , lastid)
        try:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        
        if lastid==None:
            return False
        else:
            return True

