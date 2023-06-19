import os
import pandas as pd
import csv

#Parameters
#--------------------------------------------------------------------------------------------------------------------------------------------------------


#Classes
#--------------------------------------------------------------------------------------------------------------------------------------------------------

class Util:
    def __init__(self):
        pass
        

    def saveMetaData(columns, columnTypes, members, path):
        fileMeta = os.path.join(path, 'x_meta.txt')

        with open(fileMeta, 'w') as file:
            file.write('#,TYPE,FIELD,MEMBERS\n')

            for i in range(len(columns)):
                field_type = columnTypes[i]
                field = str(columns[i]).upper()
                field_members = members[i]
                row = f"{i + 1},{field_type},{field},\"{field_members}\"\n"
                file.write(row)


    def transform_metadata_to_csv(metadata_file, csvFile):
        metadata = pd.read_csv(metadata_file, encoding='iso-8859-1')

        # Obter o número de colunas e linhas da tabela
        num_columns = len(metadata) + 1  # Número de linhas no arquivo de metadados
        num_rows = metadata[metadata['TYPE'].isin(['DIMENSION', 'DATA'])]['MEMBERS'].apply(lambda x: len(x.split(','))).prod()

        # Criar a tabela vazia
        columns = ['#', 'DATA'] + metadata[metadata['TYPE'] == 'DIMENSION']['FIELD'].tolist() + ['DATA']
        table = pd.DataFrame(columns=columns, index=range(num_rows))

        # Preencher os dados na tabela
        row_num = 0
        for i, row in metadata.iterrows():
            field_type = row['TYPE']
            field_name = row['FIELD']
            members = row['MEMBERS'].split(',')

            if field_type == 'DIMENSION':
                for member in members:
                    table.loc[row_num, '#'] = row_num + 1
                    table.loc[row_num, 'DATA'] = members[0]
                    table.loc[row_num, field_name] = member
                    table.loc[row_num, 'DATA'] = ','.join([f'dados_{j+1}' for j in range(len(metadata[metadata['TYPE'] == 'TIME']['MEMBERS'].tolist()))])
                    row_num += 1
            elif field_type == 'DATA':
                for member in members:
                    table.loc[row_num, '#'] = row_num + 1
                    table.loc[row_num, 'DATA'] = members[0]
                    table.loc[row_num, field_name] = member
                    table.loc[row_num, 'DATA'] = ','.join([f'dados_{j+1}' for j in range(len(metadata[metadata['TYPE'] == 'TIME']['MEMBERS'].tolist()))])
                    row_num += 1

        table.to_csv(csvFile, index=False)


