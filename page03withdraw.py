import PySimpleGUI as sg
from mainDatabase import *

fontWithdraw="Helvetica 12 italic"
cancelBtnYplus=50

database3 = database()
stocks = database3.getStocksFunction()
partsArr = []
locationsArr = []
for stock in stocks :
    if stock[0] not in locationsArr:
        locationsArr.append(stock[0])
    if stock[1] not in partsArr:
        partsArr.append(stock[1])
print("withdraw partsArr : ", partsArr)
print("withdraw locationsArr : ", locationsArr)
del database3

#withdraw
layout3 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
    [sg.Text('Withdraw Stock', pad=((100,0),(50,0)), font=fontWithdraw )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.Combo(partsArr,size=(80, 10), key='-withdrawPart-')],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),  sg.Combo(locationsArr,size=(80, 10), key='-withdrawLoc-')],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('', key='-withdrawBoxNo-', focus=True)],
    [sg.Submit('Update', pad=((450,0),(cancelBtnYplus,0)) ), sg.Cancel( pad=((10,0),(cancelBtnYplus,0)), key="Exit" )],
    ]


def withdrawClicked( winArg , valArg):
    print("withdraw from database clicked");

    # DO CODE FOR NEW FETCH FORM DATABASE AND REFRESH THE DROPDOWNS FOR NEW SELECTION TO WITHDRAW..................
    database3 = database()
    stocks = database3.getStocksFunction(True);
    partsArr = []
    locationsArr = []
    for stock in stocks :
        if stock[0] not in locationsArr:
            locationsArr.append(stock[0])
        if stock[1] not in partsArr:
            partsArr.append(stock[1])
    print("withdrawClicked + withdraw partsArr : ", partsArr)
    print("withdrawClicked + withdraw locationsArr : ", locationsArr)
    winArg['-withdrawLoc-'].update(values=locationsArr)
    winArg['-withdrawPart-'].update(values=partsArr)
    del database3

def clearFields3(winArg):
    winArg['-withdrawBoxNo-'].update('')
