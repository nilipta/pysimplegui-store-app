import PySimpleGUI as sg


fontWithdraw="Helvetica 12 italic"
cancelBtnYplus=50

#withdraw
layout3 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
    [sg.Text('Withdraw Stock', pad=((100,0),(50,0)), font=fontWithdraw )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('')],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),  sg.InputText('')],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('')],
    [sg.Submit('Update', pad=((450,0),(cancelBtnYplus,0)) ), sg.Cancel( pad=((10,0),(cancelBtnYplus,0)), key="Exit" )],
    ]




