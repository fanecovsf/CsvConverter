import PySimpleGUI as sg

#Layouts
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def conversorLayout():
    layout = [
        [sg.Push(), sg.Text('CSV Conversor', justification='center', font=('Arial', 14), size=(35,0), pad=(10,10)), sg.Push()],
        [sg.Push(), sg.Text('',key='-RES-'), sg.Push(), sg.Text('Select separator: ', font=('Arial', 10)), sg.Combo([';', '|', ',', '.', '/', '-'], default_value=',', readonly=False, key='-SEP-', size=(8,0))],
        [sg.Push(), sg.Button('Browse', font=('Arial', 10), size=(12,0)), sg.Button('Create time column', font=('Arial', 10), size=(18,0)), sg.Button('Generate metadata', font=('Arial', 10), size=(18,0)), sg.Button('Convert CSV', font=('Arial', 10), size=(12,0)), sg.Push()],
    ]

    return layout


def tableLayout(data, headings):

    layout = [
        [sg.Push(), sg.Table(data,
                             headings,
                             num_rows=24,
                             justification='center',
                             enable_events=True,
                             key='-TABLE-',
                             max_col_width=25,
                             def_col_width=20,
                             vertical_scroll_only=False,
                             ), sg.Push()],
        [sg.Push(), sg.Button('Menu', font=('Arial', 12), size=(17,0)), sg.Button('Select column types', font=('Arial', 12), size=(17,0)), sg.Push()],
    ]

    return layout

def timeLayout(columns):

    col_layout = [
        [sg.Text(col, size=(15, 1), key=f'-TEXT{i}-'), sg.Combo(['Day', 'Month', 'Year'], default_value='', size=(20, 1), key=f'-TYPE-{i}-', readonly=True)]
        for i, col in enumerate(columns)
    ]

    layout = [
        [sg.Text('Select date information columns:')],
        [sg.Column(col_layout, size=(400, 300), scrollable=True, vertical_scroll_only=True)],
        [sg.Push(), sg.Button('Generate', key='-CONV-', font=('Arial', 12), size=(15, 0), pad=(0, 10)), sg.FolderBrowse('Select folder', target='-PATH-', font=('Arial', 12), size=(15, 0)), sg.Push()],
        [sg.Push(), sg.Input('', key='-PATH-', size=(60,0)), sg.Push()]
    ]

    return layout

def columnsLayout(columns):
    col_layout = [
        [sg.Text(col, size=(15, 1)), sg.Combo(['TIME', 'DIMENSION', 'DATA'], default_value='', size=(20, 1), key=f'-TYPE-{i}-', readonly=True)]
        for i, col in enumerate(columns)
    ]

    layout = [
        [sg.Text('Select the types:')],
        [sg.Column(col_layout, size=(400, 300), scrollable=True, vertical_scroll_only=True)],
        [sg.Push(), sg.Button('Convert', key='-CONV-', font=('Arial', 12), size=(15, 0), pad=(0, 10)), sg.FolderBrowse('Select folder', target='-PATH-', font=('Arial', 12), size=(15, 0)), sg.Push()],
        [sg.Push(), sg.Input('', key='-PATH-', size=(60,0)), sg.Push()]
    ]

    return layout