import psycopg2
from datetime import date
from mainConfiguration import shouldUpdateOrInsert as crud_op, stock_table_all_data_query

class database:
    connection = 0
    cursor = 0
    allStocks = []
    allStatusStocks = []
    allStockTableStocks = []
    def __init__(self):
        try:
            self.connect()

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(self.connection):
                self.cursor.close()
                self.connection.close()
                # print("PostgreSQL connection is closed")
    def connect(self):
        self.connection = psycopg2.connect(user = "postgres",
                            password = "postgres",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "store")

        self.cursor = self.connection.cursor()

    def executeQUery(self, queryText, newRecord = False):
        returningDictObj = {}
        if(len(database.allStatusStocks) == 0 or len(database.allStockTableStocks) == 0 or newRecord is True):
            try:
                self.connect()
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)
            
            recordLocal = 0
            try:
                if(len(queryText) > 0):
                    self.cursor.execute(queryText)
                    recordLocal = self.cursor.fetchall()
                    # print("You are connected to - ", recordLocal,"\n")
                    if len(recordLocal):
                        # save data for status table if only 5 column of data we received
                        if len(recordLocal[0]) is 5:
                            database.allStatusStocks = recordLocal
                        elif len(recordLocal[0]) > 5:
                            database.allStockTableStocks = recordLocal
                
                    self.cursor.close()
                    self.connection.close()
                    # print("PostgreSQL connection is closed")
            except (Exception, psycopg2.Error) as error :
                print ("Error while Fetching query from PostgreSQL", error)
            
            returningDictObj['status-table-data'] = database.allStatusStocks
            returningDictObj['all-table-data'] = database.allStockTableStocks
            returningDictObj['query-result'] = recordLocal
            return returningDictObj

        #if all data are available no need to take from database        
        returningDictObj['status-table-data'] = database.allStatusStocks
        returningDictObj['all-table-data'] = database.allStockTableStocks
        returningDictObj['query-result'] = 0
        return returningDictObj

    def getStocksFunction(self, newRecord = False):
        if(len(self.allStocks) == 0 or newRecord is True):
            try:
                self.connect()
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

            # if(queryText.len() > 0):
            print ("going \n")
            self.cursor.callproc('usp_get_stock')
            record = self.cursor.fetchall()
            # print("Fetched : ", record)
            try:
                self.cursor.close()
                self.connection.close()
                # print("PostgreSQL connection is closed")
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

            self.allStocks = record
            return self.allStocks

        return self.allStocks

    def crud_stock(self, insertOrUpdate, _location, _part_number, _box_no, _IN_or_OUT = "IN", _id = 0):
        try:
            self.connect()
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

        lastid = None        
        
        # print ("checking ::: ", _location, _part_number, _box_no);
        if crud_op.INSERT is insertOrUpdate:
            lastid = self.cursor.callproc('usp_crud_stock', ("I", 0, _location , _part_number, _box_no, "no remark", _IN_or_OUT, "pa") )
            print("status : " , lastid)
            
        elif crud_op.UPDATE is insertOrUpdate:
            lastid = self.cursor.callproc('usp_crud_stock', ("U", _id, _location , _part_number, _box_no, "no remark", _IN_or_OUT, "pa") )
            print("status : " , lastid)

        self.connection.commit()

        try:
            self.cursor.close()
            self.connection.close()
            # print("PostgreSQL connection is closed")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        
        if lastid==None:
            return False
        else:
            return True



