#!/usr/bin/env python
'''
Example of (almost) all widgets, that you can use in PySimpleGUI.
'''

import PySimpleGUI as sg

# sg.theme('Dark Red')
# sg.theme('Default1')

layout = [
    [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
     [sg.T()],
    [sg.Button('Search' , size=(20, 2), pad=((100,20),0)), sg.Input("location/part No.",do_not_clear=False, size=(80, 10))],
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


# sg.theme('DarkBlue12')
MAX_ROWS = 10
MAX_COL = 5
headings = ['Location', 'Part No.', 'No Of Boxes','Last Update Date', 'Last Update By']
# header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
different_column_size=[20,10,12,25,25]
different_column_size1=[15,7,12,20,25]
columm_layout =  [[sg.Text(str(i), size=(4, 1), justification='left')] + [sg.Input(size=(different_column_size[j], 1), pad=(
        1, 1), justification='right', key=(i, j), background_color='lightskyblue') for j in range(MAX_COL)] for i in range(1, MAX_ROWS+1)]

layout4 = [
            [sg.Text('VAS store', size=(100, 1), pad=(0, (30,0)), justification='center', font=("Helvetica", 25))],
            [sg.Text('Stock Status', pad=((50,0),(0,0)) )],
            [sg.Text(size=(10, 1))]+ [sg.Text(h, size=(different_column_size1[headings.index(h)], 1), pad=((0,17),(0,0)) ) for h in headings],
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
        # sg.theme('Dark Brown 2')
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