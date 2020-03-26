import PySimpleGUI as sg

fontStockStatus="Helvetica 12 italic"

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
            [sg.Text('Stock Status', pad=((50,0),(0,0)), font=fontStockStatus )],
            [sg.Text(size=(10, 1))]+ [sg.Text(h, size=(different_column_size1[headings.index(h)], 1), pad=((0,17),(0,0)) ) for h in headings],
            [sg.Col(columm_layout, size=(750, 300), scrollable=False, pad=(0,0))],
            [sg.Submit('Export To Excel', pad=((380,0),(0,0)) ), sg.Cancel('Exit', pad=((10,0),(0,0)) )],
        ]
#Stock Status
# layout4 = table_main_heading + heading_status + header + input_rows