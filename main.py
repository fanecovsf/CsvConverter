import PySimpleGUI as sg
import pandas as pd
import os
import layouts

#Parameters
#--------------------------------------------------------------------------------------------------------------------------------------------------------

THEME = 'Dark2'

APP_NAME = 'CSV Conversor'

#Windows
#--------------------------------------------------------------------------------------------------------------------------------------------------------

class WindowPattern:
    def __init__(self):
        self.theme = THEME
        pass

#Initial screen
class Conversor(WindowPattern):
    def __init__(self):
        super().__init__()

        window = sg.Window(APP_NAME, layout=layouts.conversorLayout())

        fullPath = ''

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Browse':
                fullPath = sg.popup_get_file('Select file')
                if fullPath:
                    fileName = os.path.basename(fullPath)
                    window['-RES-'].update(fileName)

            if event == 'Open':
                if fullPath == '':
                    sg.popup('Select a valid file.', no_titlebar=True)

                else:
                    rows = sg.popup_get_text('Number of rows to show (Empty will bring 1000 rows):')
                    try:
                        rows = int(rows)
                    except:
                        rows = 1000

                    df = pd.read_csv(fullPath, sep=';', encoding='UTF-8')
                    df = df.head(rows)
                    data = df.values.tolist()
                    df.columns = [col.strip() for col in df.columns]
                    columns = list(df.columns)

                    window.disable()
                    DataframeEditor(data, columns)
                    window.enable()
                    window.bring_to_front()
                    


class DataframeEditor(WindowPattern):
    def __init__(self, data, columns):
        super().__init__()

        window = sg.Window(APP_NAME, layout=layouts.tableLayout(data, columns), size=(1000,480))

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED or event == 'Menu':
                window.close()
                break


#Execution
#--------------------------------------------------------------------------------------------------------------------------------------------------------
Conversor()
