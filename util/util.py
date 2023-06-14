import pandas as pd
import os
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

