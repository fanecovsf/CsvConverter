import PySimpleGUI as sg
import pandas as pd

#Parameters
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#Layouts
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def conversorLayout():
    layout = [
        [sg.Push(), sg.Text('CSV file conversor', justification='center', font=('Arial', 14), size=(35,0), pad=(10,10)), sg.Push()],
        [sg.Push(), sg.Text('',key='-RES-'), sg.Push()],
        [sg.Push(), sg.Button('Browse', font=('Arial', 12), size=(12,0)), sg.Button('Open', font=('Arial', 12), size=(12,0)), sg.Push()],
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
                             #size=(50,50),
                             vertical_scroll_only=False,
                             ), sg.Push()],
        [sg.Push(), sg.Button('Menu', font=('Arial', 12), size=(12,0)), sg.Push()],
    ]

    return layout
