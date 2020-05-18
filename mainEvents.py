from page01Home import * 
from page02addStock import * 
from page03withdraw import * 
from page04status import * 
from page05searchLocation import * 
from page06searchPart import * 
from mainValidation import *
import PySimpleGUI as sg

from mainConfiguration import *

window = sg.Window('VAS store', layout, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False )
windowNo=1
window2 = sg.Window('VAS store Add', layout2, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False )
window3 = sg.Window('VAS store', layout3, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False )
window4 = sg.Window('VAS store', layout4, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False )
window5 = sg.Window('VAS store', layout5, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False )
window6 = sg.Window('VAS store', layout6, size=(800, 480), no_titlebar=True, auto_size_buttons=True, location=(0,50), resizable=False )

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
    global window5
    global window6
    #add stock
    event2=0
    values2=0
    #withdraw
    event3=0
    values3=0
    #stock status
    event4=0
    values4=0
    #location search
    event5=0
    values5=0
    #part number search
    event6=0
    values6=0

    # local flags
    withdrawRefresh = False
    statusRefresh = False
    statusTablePageNumber = 0
    nextPageUpdate = False
    prevPageUpdate = False
    isSwitchedToHome = False 
    readyForAddAnother = False ##unused now
    fillLocationPageData = False
    fillLocationPageSearchItem = ' '
    fillPartNoPageData = False
    fillPartNoPageDataSearchItem = ' '

    while True:             # Event Loop
        # functions are cllaed
        if withdrawRefresh is True:
            withdrawClicked(window3, event3)
            withdrawRefresh = False
        if statusRefresh is True:
            handleStatus(window4, event4)
            statusRefresh = False
        if nextPageUpdate is True:
            nextPage(window4, statusTablePageNumber )
            nextPageUpdate = False
        if prevPageUpdate is True:
            prevPage(window4, statusTablePageNumber )
            prevPageUpdate = False
        if fillLocationPageData is True:
            handleLocationForm(window5, fillLocationPageSearchItem)
            fillLocationPageData = False
            fillLocationPageSearchItem = ' '
        if fillPartNoPageData is True:
            handlePartNoForm(window6, fillPartNoPageDataSearchItem)
            fillPartNoPageData = False
            fillPartNoPageDataSearchItem = ' ' 

        #---------------------HOME SCREEN--------------------------------------#

        if windowNo==1:
            event, values = window.read()    # returns every 500 ms
            event2 = 0
            event3 = 0
            event4 = 0
            event5 = 0
            event6 = 0

            if event in (None, 'Quit'):
                print('X pressed')

            elif event == 'Add Stock':
                windowNo=2
                window.TKroot.focus_force() 
                window.refresh()

            elif event == 'Withdraw Stock':
                window3.UnHide()
                # print('Withdraw sock')
                windowNo=3
                window.TKroot.focus_force() 
                window.refresh()
                window3.refresh()
                withdrawRefresh = True

            elif event == 'Search':
                result = handleSearch(values['-MainSearchId-'])
                if SearchPattern.UNDEFINED == result:
                    sg.popup('Enter proper partno / location', custom_text=("Close"), button_color=("black","red"), location=popupPlace )
                if SearchPattern.LOCATION == result:
                    window5.UnHide()
                    windowNo=5
                    fillLocationPageData = True
                    fillLocationPageSearchItem = (values['-MainSearchId-'])
                if SearchPattern.PARTNO == result:
                    window6.UnHide()
                    windowNo=6
                    fillPartNoPageData = True
                    fillPartNoPageDataSearchItem = (values['-MainSearchId-'])
            elif event == 'Stock Status':
                print("open status screen")
                statusTablePageNumber = 0
                windowNo=4
                window.refresh()
                statusRefresh = True
            
            elif event in (None, 'Exit'):
                if sg.PopupYesNo('Do you really want to quit?', location=popupPlace ) == 'Yes':
                    break
                else:
                    continue

            isSwitchedToHome = True


        #--------------------- ADD SCREEN --------------------------------------#
        if windowNo==2:

            if isSwitchedToHome:
                window2.UnHide()
                window2.refresh()
                isSwitchedToHome = False

            event2, values2 = window2.read(timeout=100)    # returns every 500 ms

            if event2 == 'Exit':
                print('win2 hide')
                clearFields2(window2)
                window2.Hide()
                event2=0
                values2=0
                windowNo=1
                window.refresh()

            elif event2 == '-update2-':
                addButtonClick(values2, window2)
                window2.Hide()
                event2=0
                values2=0
                windowNo=1
                window.refresh()
                # values2=0
  

        #--------------------- UPDATE SCREEN --------------------------------------#
        if windowNo==3:
            event3, values3 = window3.read(timeout=100)    # returns every 500 ms

            if event3 == 'Exit':
                print('win3 hide')
                clearFields3(window3)
                window3.Hide()
                event3=0
                values3=0
                windowNo=1
                window.refresh()
                window3.refresh()
            elif event3 == '-update3-':
                withdrawHandle(values3, window3)
                values3=0
        
        #--------------------- STATUS SCREEN --------------------------------------#
        if windowNo==4:
            if isSwitchedToHome:
                window4.UnHide()
                window4.refresh()
                isSwitchedToHome = False

            event4, values4 = window4.read(timeout=50)    # returns every 500 ms

            if event4 == 'Exit':
                print('win4 hide')
                window4.Hide()
                event4=0
                values4=0
                windowNo=1
                window.refresh()
                window4.refresh()
            elif event4 == 'Next':
                statusTablePageNumber+=1
                nextPageUpdate = True
            elif event4 == 'Prev':
                if statusTablePageNumber > 0:  
                    statusTablePageNumber-=1
                    prevPageUpdate = True        
        #--------------------- SEARCH SCREEN --------------------------------------#
        if windowNo==5:
            event5, values5 = window5.read(timeout=100)    # returns every 500 ms

            if event5 == 'Exit':
                print('win5 hide')
                window5.Hide()
                event5=0
                values5=0
                windowNo=1
                window.refresh()
                window5.refresh()
            
        #--------------------- SEARCH SCREEN --------------------------------------#
        if windowNo==6:
            event6, values6 = window6.read(timeout=100)    # returns every 500 ms
            if event6 == 'Exit':
                print('win6 hide')
                window6.Hide()
                event6=0
                values6=0
                windowNo=1
                window.refresh()
                window6.refresh()

def closeAll():
    global windowNo
    global window
    global window1
    global window2
    global window3
    global window4
    global window5
    global window6

    window2.close()
    window3.close()
    window4.close()
    window5.close()
    window6.close()
    window.close()                