from mainConfiguration import SearchPattern
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
    print("Search partsArr : ", partsArr)
    print("Search locationsArr : ", locationsArr)
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