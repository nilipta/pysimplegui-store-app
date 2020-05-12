import PySimpleGUI as sg
from mainDatabase import *
from mainConfiguration import *

cancelBtnYplus = 50
fontAddStock="Helvetica 12 italic"

layout2 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
    [sg.Text('Add Stock', pad=((100,0),(50,0)), font=fontAddStock )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),   sg.InputText('', key="-location-", focus=True)],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('', key="-part-")],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('', key="-boxNo-")],
    [sg.Submit('Update', pad=((450,0),(cancelBtnYplus,0)) , key="-update2-"), sg.Cancel( pad=((10,0),(cancelBtnYplus,0)), key="Exit" )],
]

def addButtonClick(valArg, winArg):
    print("add to database clicked");
    database2 = database()
    status = False
    if isinstance(int(valArg['-boxNo-']), int):
        status = database2.crud_stock(shouldUpdateOrInsert.INSERT, str(valArg['-location-']), str(valArg['-part-']), int(valArg['-boxNo-']))
    del database2
    if status:
        sg.popup('Insert done!', location=popupPlace)
        clearFields2(winArg)    
    else:
        sg.popup('Insert Error!', location=popupPlace)
        
def clearFields2(winArg):
    winArg['-location-'].update('')
    winArg['-part-'].update('')
    winArg['-boxNo-'].update('')
