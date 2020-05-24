from mainConfiguration import SearchPattern, shouldUpdateOrInsert, stock_table_all_data_query
from mainDatabase import *

def handleSearch(arg):

    databaseobj = database()
    stocks = databaseobj.getStocksFunction()
    partsArr = []
    locationsArr = []
    for stock in stocks :
        if stock[0] not in locationsArr:
            locationsArr.append(stock[0])
        if stock[1] not in partsArr:
            partsArr.append(stock[1])
    # print("Search partsArr : ", partsArr)
    # print("Search locationsArr : ", locationsArr)
    del databaseobj

    try:
        if( 0 == len(arg) ):
            return SearchPattern.UNDEFINED
        elif ( arg in partsArr) :
            return SearchPattern.PARTNO
        elif ( arg in locationsArr) :
            return SearchPattern.LOCATION
        else:
            return SearchPattern.UNDEFINED
    except():
        return SearchPattern.UNDEFINED

def checkWhetherUpdateOrInsertInAddStock(locationArg, partArg, boxNoArg):
    # print("Add page wants to check if this part number exist in location")
    databaseObj2 = database()
    # checking if location argument is unique or available in database
    # index  will say about the location in object returningDictObj['all-table-data']
    queryString = "select count (stock_id), stock_id from stock where locations='{0}' and part_number='{1}' group by stock_id".format(locationArg, partArg)
    stocks = databaseObj2.executeQUery(queryString, True)
    try:
        if stocks['query-result']:
            if( stocks['query-result'][0][0] > 0 ):
                databaseObj2.crud_stock(crud_op.UPDATE, locationArg, partArg, boxNoArg, "IN", stocks['query-result'][0][1])
        else:
            databaseObj2.crud_stock(crud_op.INSERT, locationArg, partArg, boxNoArg)
    except:
        print("Error while stocks['query-result']")
        del databaseObj2
        return False

    del databaseObj2
    return True

def checkWhetherWithdrawInWithdrawStock(locationArg, partArg, boxNoArg):
    # print("withdraw page wants to check if this box no can be withdrawn")
    databaseObj3 = database()
    # checking if location argument is unique or available in database
    # index  will say about the location in object returningDictObj['all-table-data']
    queryString = "select box_number from stock where locations='{0}' and part_number='{1}'".format(locationArg, partArg)
    stocks = databaseObj3.executeQUery(queryString, True)
    try:
        if stocks['query-result']:
            if( stocks['query-result'] > 0 ):
                databaseObj3.crud_stock(crud_op.INSERT, locationArg, partArg, boxNoArg, "OUT")
    except:
        print("Error while stocks['query-result']")
        del databaseObj3
        return False

    del databaseObj3
    return True