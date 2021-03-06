import PySimpleGUI as sg
from mainDatabase import *
from mainValidation import *
from mainConfiguration import popupPlace

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
    try:
        if isinstance(int(valArg['-boxNo-']), int):
            # status = database2.crud_stock(shouldUpdateOrInsert.INSERT, str(valArg['-location-']), str(valArg['-part-']), int(valArg['-boxNo-']))
            status = checkWhetherUpdateOrInsertInAddStock( str(valArg['-location-']), str(valArg['-part-']), int(valArg['-boxNo-']) )
            del database2
        if status:
            sg.popup('Insert done!', location=popupPlace)
        else:
            sg.popup('Insert Error!', location=popupPlace)

        clearFields2(winArg)    
    except ValueError:
        print("Could not convert data to an integer.")
    finally:
        pass
    

def clearFields2(winArg):
    print('clearing all fields from add field')
    winArg['-location-'].update('')
    winArg['-part-'].update('')
    winArg['-boxNo-'].update('')

