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
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),   sg.InputText('', key="-location-")],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('', key="-part-")],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('', key="-boxNo-")],
    [sg.Submit('Update', pad=((450,0),(cancelBtnYplus,0)) , key="-update2-"), sg.Cancel( pad=((10,0),(cancelBtnYplus,0)), key="Exit" )],
]

def addButtonClick(valArg, winArg):
    print("add to database clicked");
    database1 = database()
    status = database1.insert_page2(str(valArg['-location-']), str(valArg['-part-']), str(valArg['-boxNo-']))
    del database1
    if status:
        sg.popup('Insert done!', location=popupPlace)
        winArg['-location-'].update('')
        winArg['-part-'].update('')
        winArg['-boxNo-'].update('')
        