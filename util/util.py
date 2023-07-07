import os
import pandas as pd
import itertools

#Classes
#--------------------------------------------------------------------------------------------------------------------------------------------------------

class Util:
    def __init__(self):
        pass
        

    def saveMetaData(columns, columnTypes, members, path):
        fileMeta = os.path.join(path, 'x_meta.txt')

        with open(fileMeta, 'w') as file:
            file.write('#,TYPE,FIELD,MEMBERS\n')

            data_columns = [str(columns[i]) for i in range(len(columns)) if columnTypes[i] == 'DATA']
            row = f"1,DATA,DATA,\"{', '.join(data_columns)}\"\n"
            file.write(row)

            index = 2
            for i in range(len(columns)):
                field_type = columnTypes[i]
                field = str(columns[i]).upper()
                if field_type != 'DATA':
                    field_members = members[i]
                    if field_type != 'TIME':
                        field_members += ', All'  # Add 'All' to dimension members

                    row = f"{index},{field_type},{field},\"{field_members}\"\n"
                    file.write(row)
                    index += 1


    def transform_metadata_to_csv(metadata_file, csvFile):
        metadata = pd.read_csv(metadata_file, encoding='iso-8859-1')

        time_members = metadata.loc[metadata['TYPE'] == 'TIME', 'MEMBERS'].iloc[0].split(', ')
        dimensions = metadata.loc[metadata['TYPE'] == 'DIMENSION', 'MEMBERS'].str.split(', ')
        data_members = metadata.loc[metadata['TYPE'] == 'DATA', 'MEMBERS'].str.split(', ')
        field_names = metadata.loc[metadata['TYPE'] != 'TIME', 'FIELD'].tolist()

        num_rows = 1
        for dimension in dimensions:
            num_rows *= len(dimension)

        num_columns = len(metadata) - 2

        columns = ['#', 'DATA'] + field_names + ['DATA']
        table = pd.DataFrame(columns=columns, index=range(num_rows))

        row_num = 0
        for data_member in data_members:
            for dimension_values in itertools.product(*dimensions):
                table.loc[row_num, '#'] = row_num + 1
                table.loc[row_num, 'DATA'] = data_member[0]

                for i, value in enumerate(dimension_values):
                    table.loc[row_num, field_names[i]] = value

                time_data = []
                for time_member in time_members:
                    data = f'{data_member[0]}, {", ".join(dimension_values)}, {time_member}'
                    time_data.append(data)

                table.loc[row_num, 'DATA'] = ', '.join(time_data)
                row_num += 1

        table.to_csv(csvFile, index=False)


