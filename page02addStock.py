import PySimpleGUI as sg

layout2 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
    [sg.Text('Add Stock', pad=((100,0),(50,0)) )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),  sg.InputText('')],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('')],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('')],
    [sg.Submit('Update', pad=((380,0),(20,0)) ), sg.Cancel( pad=((10,0),(20,0)) )],
    [sg.Cancel('Exit', pad=((650,0),(60,0)))]
    ]