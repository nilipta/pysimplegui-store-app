import PySimpleGUI as sg
from mainDatabase import *
from mainConfiguration import status_col_data_query

fontStockStatus="Helvetica 12 italic"

# sg.theme('DarkBlue12')
MAX_ROWS = 10
MAX_COL = 5
headings = ['Location', 'Part No.', 'No Of Boxes','Last Update Date', 'Last Update By']
# header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
different_column_size=[20,10,12,25,25]
different_column_size1=[15,7,12,20,25]
columm_layout =  [[sg.Text(str(i), size=(4, 1), justification='left')] + [sg.Input(size=(different_column_size[j], 1), pad=(
        1, 1), justification='right', key=(i, j), background_color='lightskyblue', disabled=True ) for j in range(MAX_COL)] for i in range(1, MAX_ROWS+1)]

layout4 = [
            [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
            [sg.Text('Stock Status', pad=((40,0),(0,0)), font=fontStockStatus )],
            [sg.Text(size=(10, 1))]+ [sg.Text(h, size=(different_column_size1[headings.index(h)], 1), pad=((0,17),(0,0)) ) for h in headings],
            [sg.Col(columm_layout, size=(750, 300), scrollable=False, pad=(0,0))],
            [sg.Button('Prev', pad=((60,20),(0,0))),sg.Button('Next', pad=((20,60),(0,0))), sg.Submit('Export To Excel', pad=((280,0),(0,0)) ), sg.Cancel('Exit', pad=((10,0),(0,0)) )],
        ]
#Stock Status
# layout4 = table_main_heading + heading_status + header + input_rows


def handleStatus(winArg , valArg):
    print("In status page : " )
    database4 = database()
    stocksdict = database4.executeQUery(status_col_data_query, True)
    stocks = stocksdict["status-table-data"]
    if len(stocks) <= 10:
        winArg['Next'].update(disabled=True)   
    #as total row count is 10, so 10 row copy from database object
    stocks = stocks[:10]  
    
    fillData(winArg, stocks)

    winArg['Prev'].update(disabled=True)            
    del database4
    
def nextPage(winArg, pageNO ):
    print("next page", pageNO)
    database4 = database()
    stocksDict = database4.executeQUery(status_col_data_query, False) #false coz no query to database
    stocks = stocksDict["status-table-data"]

    print("Total lines of data = ", int(len(stocks)) )
    calculateArrayDataPerPage(winArg, stocks, pageNO)

    winArg['Prev'].update(disabled=False)
    del database4

def prevPage(winArg, pageNO ):
    if pageNO is 0:
        winArg['Prev'].update(disabled=True)
    
    database4 = database()
    stocksDict = database4.executeQUery(status_col_data_query, False) #false coz no query to database
    stocks = stocksDict["status-table-data"]
    
    print("Total lines of data = ", int(len(stocks)) )
    calculateArrayDataPerPage(winArg, stocks, pageNO)

    winArg['Next'].update(disabled=False)
    del database4


def clearCells(winArg, index = 1): #1 coz its index starts from 1 in row section of table
    print("clear screen called", index)
    for i in range(index, 11):  #you know range till 10 means 11 right?
        for j in range(0,5):
            location = (i, j)
            try:            # try the best we can at reading and filling the table
                target_element = winArg[location]
                new_value = " "
                if target_element is not None:
                    target_element.update(new_value)
            except:
                pass
        print("i  = ", i )

def calculateArrayDataPerPage(winArg, stocks, pageNO):
    #as total row count is 10, so 10 row copy from database object
    IsToBeDoneRestCellsBlank = False 
    index_begin = pageNO*10
    index_end = index_begin

    if int((len(stocks))/10) > pageNO:
        winArg['Next'].update(disabled=False)   
        index_end = index_begin + 10
    elif int((len(stocks))/10) is pageNO:
        winArg['Next'].update(disabled=True)   
        index_end = index_begin + (int(len(stocks)/10)+1) #+1 coz you know the split range of array
        IsToBeDoneRestCellsBlank = True
    else:
        winArg['Next'].update(disabled=True)
        return   
    
    stocks = stocks[index_begin:index_end]  
    
    fillData(winArg, stocks)

    #rest cells should be blank
    if IsToBeDoneRestCellsBlank :
        clearCells(winArg, (int(len(stocks)) + 1) ) #fromCellIndexShouldBlank

def fillData(winArg, stocks):
    for i, row in enumerate(stocks):
        for j, item in enumerate(row):
            location = (i+1, j) #i+1 coz its index starts from 1 in row section of table
            try:            # try the best we can at reading and filling the table
                target_element = winArg[location]
                new_value = item
                if target_element is not None and new_value != '':
                    target_element.update(new_value)
            except:
                pass
