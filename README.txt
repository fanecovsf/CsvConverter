## CSV File Converter

The CSV File Converter is a simple graphical application that allows you to convert a CSV file into a formatted metadata file and a flat CSV file. The metadata file contains information about the columns in the original CSV file, such as their types and members, while the flat CSV file is a converted version of the original CSV file based on the metadata.

Download link: https://drive.google.com/file/d/1zSQBOSKk-yJEmhXwX9-A3vJmBp9fUadH/view?usp=sharing

### Usage

1. **Initial Screen**

   Upon launching the application, you'll see the initial screen titled "CSV File Converter." The screen provides two buttons: "Browse" and "Open."

   - **Browse**: Clicking this button opens a file selection dialog. Choose the CSV file that you want to convert.

   - **Open**: After selecting a valid CSV file using the "Browse" button, click "Open" to proceed. If you haven't selected a file or selected an invalid file, a pop-up message will prompt you to select a valid file.

2. **CSV File Preview**

   After clicking "Open," a new screen will appear displaying a preview of the CSV file. The screen shows a table with a subset of the data from the CSV file. By default, the table displays the first 100 rows, but you can specify the number of rows to show.

   - **Number of rows**: You can input the desired number of rows to show in the pop-up window that appears after clicking "Open." If you leave it empty, it will display 100 rows.

   - **Table navigation**: You can scroll through the table vertically to view the data. The table also supports horizontal scrolling if the columns exceed the available width.

   - **Select column types**: Clicking this button allows you to specify the types for each column in the CSV file.

3. **Column Types Selection**

   In this screen, you need to assign types to each column in the CSV file. The following rules apply when selecting the types for the columns:

   - Quantity of Data Columns: At least one column must be assigned the "DATA" type. This type represents the data values in the CSV file.

   - Quantity of Time Columns: Only one column can be assigned the "TIME" type. This type is used to represent time-related data.

   - Quantity of Dimension Columns: At least one column must be assigned the "DIMENSION" type. This type is used to represent dimension-related data.

   - Selection Validation: The application validates the column types selected according to these rules. If the rules are not met, a pop-up message will inform you of the issue and prompt you to make the necessary adjustments.

   - Conversion: Once the column types have been assigned correctly, you can proceed with the conversion process by clicking the "Convert" button.

4. **Conversion Process**

   Once you click "Convert," the application will generate the metadata and flat CSV files based on the selected column types.

   - **Metadata file**: The metadata file contains information about the columns, including the column index, type, field name, and members. The file is saved as `x_meta.txt` in the selected folder.

   - **Flat CSV file**: The flat CSV file is a converted version of the original CSV file based on the metadata. It follows the specified column types and is saved as `x_datos_planos.csv` in the selected folder.

   - **Completion message**: After the conversion process is complete, a pop-up message will confirm that the metadata file and flat CSV file have been created and saved in the selected folder.

5. **Closing the Application**

   You can close the application at any time by clicking the close button (X) on the application window or by clicking the "Menu" button in the "CSV File Preview" or "Column Types Selection" screens.
