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


    def createFlatCsv(csv_file_path, mainPath):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Determine the number of columns and rows
        num_rows = len(df)

        # Create the table as a pandas DataFrame
        table = pd.DataFrame(columns=['#', 'DATA'] + df.columns)

        # Fill in the table with data from the CSV file
        for i in range(num_rows):
            row = [str(i + 1), df.iloc[i, 0]] + df.iloc[i, 1:].tolist()
            table.loc[i] = row

        # Save the table to a new CSV file
        flat_csv_file = os.path.join(mainPath, 'x_datos_planos.csv')
        table.to_csv(flat_csv_file, index=False)

        print(f"CSV conversion completed. Output file: {flat_csv_file}")


    def createFlatCsv2(csv_file_path, meta_file_path, mainPath):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Read the metadata file to determine the table structure
        meta_df = pd.read_csv(meta_file_path, encoding='ISO-8859-1')

        # Determine the number of columns and rows
        num_columns = len(meta_df)
        num_rows = len(meta_df.iloc[0]['MEMBERS'])

        print(num_rows)

        # Create the table as a pandas DataFrame
        table = pd.DataFrame(columns=['#', 'DATA'] + list(meta_df['FIELD']))

        # Fill in the table with data from the CSV file
        for i in range(num_rows):
            row = [str(i + 1), df.iloc[i, 0]] + list(meta_df['MEMBERS'])
            table.loc[i] = row

        # Save the table to a new CSV file
        flat_csv_file = os.path.join(mainPath, 'x_datos_planos.csv')
        table.to_csv(flat_csv_file, index=False)

        print(f"CSV conversion completed. Output file: {flat_csv_file}")


