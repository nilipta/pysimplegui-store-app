from page01Home import * 
from page02addStock import * 
from page03withdraw import * 
from page04status import * 
import PySimpleGUI as sg

window = sg.Window('VAS store', layout, size=(800, 480), no_titlebar=False, auto_size_buttons=True, location=(0,0), resizable=True)
windowNo=1
window2 = sg.Window('VAS store', layout2, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False)
window3 = sg.Window('VAS store', layout3, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False)
window4 = sg.Window('VAS store', layout4, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False)

# print(sg.Window.get_screen_size())
# window.Maximize()

def continueReading():
    #while infinite loop
    global windowNo
    global window
    global window1
    global window2
    global window3
    global window4
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

def closeAll():
    global windowNo
    global window
    global window1
    global window2
    global window3
    global window4

    window2.close()
    window3.close()
    window4.close()
    print('at last')
    window.close()                