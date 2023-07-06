import PySimpleGUI as sg
import pandas as pd
import os
import layouts
from util.util import Util
import time
import datetime

#Parameters
#--------------------------------------------------------------------------------------------------------------------------------------------------------

THEME = 'DarkTeal12'

APP_NAME = 'CSV Conversor'

STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + '\static'

ICON = STATIC_PATH + '\icon.ico'

#Windows
#--------------------------------------------------------------------------------------------------------------------------------------------------------

class WindowPattern:
    def __init__(self):
        self.theme = sg.theme(THEME)

        pass

#Initial screen
class Conversor(WindowPattern):
    def __init__(self):
        super().__init__()

        window = sg.Window(APP_NAME, layout=layouts.conversorLayout(), icon=ICON)

        fullPath = ''

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Browse':
                fullPath = sg.popup_get_file('Select file', icon=ICON)
                if fullPath:
                    fileName = os.path.basename(fullPath)
                    window['-RES-'].update(fileName)

            if event == 'Create time column':
                if fullPath == '':
                    sg.popup('Select a valid file.', no_titlebar=True)

                else:

                    df = pd.read_csv(fullPath, sep=';', encoding='UTF-8')
                    dfFull = df
                    fullData = df.values.tolist()
                    data = df.values.tolist()
                    df.columns = [col.strip() for col in df.columns]
                    columns = list(df.columns)

                    window.hide()
                    TimeColumn(columns, dfFull)
                    window.un_hide()
                    window.bring_to_front()

            if event == 'Open':
                if fullPath == '':
                    sg.popup('Select a valid file.', no_titlebar=True)

                else:
                    rows = sg.popup_get_text('Number of rows to show (Empty will bring 100 rows):', icon=ICON)
                    try:
                        rows = int(rows)
                    except:
                        rows = 100

                    df = pd.read_csv(fullPath, sep=';', encoding='UTF-8')
                    fullData = df.values.tolist()
                    if len(df) < rows:
                        rows = len(df)
                    else:
                        pass
                    df = df.head(rows)
                    data = df.values.tolist()
                    df.columns = [col.strip() for col in df.columns]
                    columns = list(df.columns)

                    window.hide()
                    DataframeEditor(data=data,fullData=fullData, columns=columns, fullPath=fullPath)
                    window.un_hide()
                    window.bring_to_front()


class TimeColumn(WindowPattern):
    def __init__(self, columns, df):
        super().__init__()

        window = sg.Window(APP_NAME, layout=layouts.timeLayout(columns), icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == '-CONV-':
                column_types = [self.value[f'-TYPE-{i}-'] for i in range(len(columns))]

                if column_types.count('Day') == 0 and column_types.count('Month') == 0 and column_types.count('Year') == 0:
                    sg.popup('Must select at least a "Year" column.', no_titlebar=True)

                elif column_types.count('Year') == 0:
                    sg.popup('Must select at least one "Year" column.', no_titlebar=True)

                elif column_types.count('Day') > 1 or column_types.count('Month') > 1 or column_types.count('Year') > 1:
                    sg.popup('Please select only one column for each type.', no_titlebar=True)

                else:
                    columnTimeList = []
                    for i, col in enumerate(columns):
                        combo_value = self.value[f'-TYPE-{i}-']

                        match combo_value:
                            case 'Day':
                                columnTimeList.insert(0, col)

                            case 'Month':
                                columnTimeList.insert(1, col)

                            case 'Year':
                                columnTimeList.insert(2, col)

                    
                
                print(columnTimeList)
                #df.to_csv(os.path.join(self.value['-PATH-'], 'time_column_file.csv'), index=False, sep=',')

                    #print(f'Column {col} selected: {combo_value}')
                    


class DataframeEditor(WindowPattern):
    def __init__(self, data, fullData, columns, fullPath):
        super().__init__()

        window = sg.Window(APP_NAME, layout=layouts.tableLayout(data, columns), size=(1000,480), icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED or event == 'Menu':
                window.close()
                break

            if event == 'Select column types':
                window.disable()
                ColumnTypes(columns, fullData, initialCsvPath=fullPath)
                window.enable()
                window.bring_to_front()


class ColumnTypes(WindowPattern):
    def __init__(self, columns, data, initialCsvPath):
        super().__init__()

        window = sg.Window(APP_NAME, layout=layouts.columnsLayout(columns), icon=ICON)

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED or event == 'Close':
                window.close()
                break

            if event == '-CONV-':
                if self.value['-PATH-'] == '':
                    sg.popup('Select a valid folder.', no_titlebar=True)

                else:
                    column_types = [self.value[f'-TYPE-{i}-'] for i in range(len(columns))]
                    members = [', '.join(set([str(row[i]) for row in data])) for i in range(len(columns))]

                    if column_types.count('') > 0:
                        sg.popup('Must select one of the 3 available types for the column.')

                    elif column_types.count('TIME') > 1:
                        sg.popup('Must be just 1 "Time" column selected. Please, try again.', no_titlebar=True)

                    elif column_types.count('DATA') < 1:
                        sg.popup('Must be at least 1 "Data" column selected. Please, try again.', no_titlebar=True)

                    elif column_types.count('DIMENSION') < 1:
                        sg.popup('Must be at least 1 "Dimension" column selected. Please, try again.', no_titlebar=True)

                    else:

                        if self.value['-METAONLY-'] == True:
                            Util.saveMetaData(columns, column_types, members, self.value['-PATH-'])
                            sg.popup(f'Metadata file created at {self.value["-PATH-"]}.', no_titlebar=True)
                            break

                        else:
                            Util.saveMetaData(columns, column_types, members, self.value['-PATH-'])
                            time.sleep(3)

                            metaPath = os.path.join(self.value['-PATH-'], 'x_meta.txt')

                            Util.transform_metadata_to_csv(metaPath, os.path.join(self.value['-PATH-'], 'x_datos_planos.csv'))

                            sg.popup(f'Metadata file and flat csv created at {self.value["-PATH-"]}.', no_titlebar=True)
                            window.close()
                            break
