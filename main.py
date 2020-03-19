#!/usr/bin/env python
'''
Example of (almost) all widgets, that you can use in PySimpleGUI.
'''

import PySimpleGUI as sg

# sg.theme('Dark Red')
# sg.theme('Default1')
# sg.set_options(text_color='black', background_color='#A6B2BE', text_element_background_color='#A6B2BE')
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'),
                    initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'),
                    initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layoutX = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('(Almost) All widgets in one Window!', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text')],
    [sg.Frame(layout=[
        [sg.CBox('Checkbox', size=(10, 1)),
         sg.CBox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
         sg.Radio('My second Radio!', "RADIO1")]], title='Options', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
     sg.MLine(default_text='A second multi-line', size=(35, 3))],
    [sg.Combo(('Combobox 1', 'Combobox 2'),default_value='Combobox 1', size=(20, 1)),
     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.OptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     sg.Frame('Labelled Group', [[
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
         sg.Col(column1)]])
    ],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Button('Set'), sg.Text('Your Folder', size=(15, 1), justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

layout = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
     [sg.T()],
    [sg.Button('Search' , size=(20, 2), pad=((100,20),0)), sg.InputText('Default Folder', size=(80, 3))],
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

#withdraw
layout3 = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
    [sg.Text('Withdraw Stock', pad=((100,0),(50,0)) )],
    [sg.T()],
    [sg.T()],
    [sg.Text('Part Number', size=(15, 2), pad=((100,0),0)), sg.InputText('')],
    [sg.Text('Location', size=(15, 2), pad=((100,0),0)),  sg.InputText('')],
    [sg.Text('Number of Boxes', size=(15, 2), pad=((100,0),0)), sg.InputText('')],
    [sg.Submit('Update', pad=((380,0),(20,0)) ), sg.Cancel( pad=((10,0),(20,0)) )],
    [sg.Cancel('Exit', pad=((650,0),(60,0)))]
    ]

MAX_ROWS = 10
MAX_COL = 5
headings = ['Location', 'Part No.', 'No Of Boxes','Last Update Date', 'Last Update By']
# header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
columm_layout =  [[sg.Text(str(i), size=(4, 1), justification='left')] + [sg.Input(size=(18, 1), pad=(
        1, 1), justification='right', key=(i, j)) for j in range(MAX_COL)] for i in range(1, MAX_ROWS+1)]

layout4 = [
            [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
            [sg.Text('Stock Status', pad=((50,0),(0,0)) )],
            [sg.Text(size=(10, 1))]+ [sg.Text(h, size=(15,1), pad=((0,17),(0,0)) ) for h in headings],
            [sg.Col(columm_layout, size=(750, 300), scrollable=False, pad=(0,0))],
            [sg.Submit('Export To Excel', pad=((380,0),(0,0)) ), sg.Cancel('Exit', pad=((10,0),(0,0)) )],
        ]
#Stock Status
# layout4 = table_main_heading + heading_status + header + input_rows


windowNo = 0
# print(sg.Window.get_screen_size())
window = sg.Window('VAS store', layout, size=(800, 480), no_titlebar=False, auto_size_buttons=True, location=(0,0), resizable=True)
windowNo=1
window2 = sg.Window('VAS store', layout2, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False)
window3 = sg.Window('VAS store', layout3, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False)
window4 = sg.Window('VAS store', layout4, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False)
# window.Maximize()

#add stock
event2=0
values2=0
#withdraw
event3=0
values3=0
#stock status
event4=0
values4=0
while True:             # Event Loop
    if windowNo==1:
        event, values = window.read()    # returns every 500 ms
    elif windowNo==2:
        event2, values2 = window2.read(timeout=100)    # returns every 500 ms
        # event, values = window.read(timeout=300)    # returns every 500 ms
        # event, values = window.read()    # returns every 500 ms
    elif windowNo==3:
        event3, values3 = window3.read(timeout=100)    # returns every 500 ms
    elif windowNo==4:
        event4, values4 = window4.read(timeout=100)    # returns every 500 ms
    if event in (None, 'Quit'):
        print('X pressed')
        # break
    if event == 'Add Stock':
        window2.UnHide()
        # print('add sock')
        windowNo=2
        window.refresh()
        window2.refresh()
    if event == 'Withdraw Stock':
        window3.UnHide()
        # print('Withdraw sock')
        windowNo=3
        window.refresh()
        window3.refresh()
    if event == 'Stock Status':
        window4.UnHide()
        # print('Withdraw sock')
        windowNo=4
        window.refresh()
        window4.refresh()
    if event2 == 'Exit':
        print('win2 hide')
        window2.Hide()
        event2=0
        values2=0
        windowNo=1
        window.refresh()
        window2.refresh()
    if event3 == 'Exit':
        print('win3 hide')
        window3.Hide()
        event3=0
        values3=0
        windowNo=1
        window.refresh()
        window3.refresh()
    if event4 == 'Exit':
        print('win4 hide')
        window4.Hide()
        event4=0
        values4=0
        windowNo=1
        window.refresh()
        window4.refresh()
    if event in (None, 'Exit'):
        if sg.PopupYesNo('Do you really want to quit?', location=(330, 250) ) == 'Yes':
            break
        else:
            continue
    if windowNo==2 or windowNo==3 or windowNo==4:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            if sg.PopupYesNo('Do you really want to quit?', location=(330, 250)) == 'Yes':
                break
            else:
                continue

window2.close()
window3.close()
window4.close()
print('at last')
window.close()