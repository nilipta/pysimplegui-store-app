import PySimpleGUI as sg
from mainDatabase import *


database1 = database()
stocks = database1.getStocksFunction(True)
partAddressArr = []
for stock in stocks :
    if stock[0] not in partAddressArr:
        partAddressArr.append(stock[0])
    if stock[1] not in partAddressArr:
        partAddressArr.append(stock[1])
print("home: ", partAddressArr)
del database1
layout = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
     [sg.T()],
    # [sg.Button('Search' , size=(20, 2), pad=((100,20),0)), sg.Input("location/part No.",do_not_clear=False, size=(80, 10), key='-MainSearchId-' ), [sg.Combo(['choice 1', 'choice 2'])]],
    [sg.Button('Search' , size=(20, 2), pad=((100,20),0)), sg.Combo(partAddressArr,size=(80, 10), key='-MainSearchId-')],
     [sg.T()],
     [sg.T()],
     [sg.T()],
     [sg.T()],
     [sg.T()],
     [sg.Button('Add Stock', size=(30, 3)), 
      sg.Button('Withdraw Stock', size=(30, 3)), 
      sg.Button('Stock Status', size=(30, 3))],
    [sg.Submit(tooltip='Click to submit this form', pad=((620,0),(50,0))), sg.Cancel('Exit', pad=(0,(50,0)))]
    ]


'''
        layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
                [sg.Input(key='-IN-')],
                [sg.Button('Show'), sg.Button('Exit')]]

        window = sg.Window('Window Title', layout)

        while True:  # Event Loop
            event, values = window.read()       # can also be written as event, values = window()
            print(event, values)
            if event is None or event == 'Exit':
                break
            if event == 'Show':
                # change the "output" element to be the value of "input" element
                window['-OUTPUT-'].update(values['-IN-'])
                # above line can also be written without the update specified
                window['-OUTPUT-'](values['-IN-'])
'''