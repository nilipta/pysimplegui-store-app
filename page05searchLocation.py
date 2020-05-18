import PySimpleGUI as sg
from mainDatabase import *

fontLocation="Helvetica 12 italic"
cancelBtnYplus=50
inputBoxXplus=((30,0),0)
#withdraw
layout5 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25) ) ],
    [sg.Text('Search Results : ', pad=((100,0),(50,0)), font=("Helvetica 20 bold") ), sg.Text('Location', pad=((10,0),(50,0)), font=fontLocation )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('', pad=inputBoxXplus, disabled=True, key='-PartSearch1-' )],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),  sg.InputText('', pad=inputBoxXplus, disabled=True, key='-LocSearch1-' )],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('', pad=inputBoxXplus, disabled=True, key='-BoxNoSearch1-' )],
    [sg.Submit('Update', pad=((450,0),(cancelBtnYplus,0)) ), sg.Cancel( pad=((10,0),(cancelBtnYplus,0)), key='Exit' )],
]

def handleLocationForm(winArg, searchItem):
    print("filling location serach page")
    # DO CODE FOR NEW FETCH FORM DATABASE AND REFRESH THE DROPDOWNS FOR NEW SELECTION TO WITHDRAW..................
    targetStock = 0
    databaseObj = database()
    stocks = databaseObj.getStocksFunction(True);
    del databaseObj

    print("database in handle location search  = ", stocks, "\n serach  = ", searchItem)

    for stock in stocks :
        if searchItem in stock:
            targetStock = stock
            break
    print("after loop = ", targetStock)
    winArg['-PartSearch1-'].update(targetStock[1])
    winArg['-LocSearch1-'].update(targetStock[0])
    winArg['-BoxNoSearch1-'].update(targetStock[2])


