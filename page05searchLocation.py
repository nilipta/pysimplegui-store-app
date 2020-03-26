import PySimpleGUI as sg

fontLocation="Helvetica 12 italic"
cancelBtnYplus=50
inputBoxXplus=((30,0),0)
#withdraw
layout5 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25) ) ],
    [sg.Text('Search Results : ', pad=((100,0),(50,0)), font=("Helvetica 20 bold") ), sg.Text('Location', pad=((10,0),(50,0)), font=fontLocation )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('', pad=inputBoxXplus )],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),  sg.InputText('', pad=inputBoxXplus )],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('', pad=inputBoxXplus )],
    [sg.Submit('Update', pad=((450,0),(cancelBtnYplus,0)) ), sg.Cancel( pad=((10,0),(cancelBtnYplus,0)), key='Exit' )],
]

