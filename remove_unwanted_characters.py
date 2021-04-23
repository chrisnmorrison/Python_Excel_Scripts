import pandas as pd

# select filename of spreadsheet
excel_file = 'my_spreadsheet.xlsx'
# read an excel file into a dataframe variable
df = pd.read_excel(excel_file)

# Prints top two rows - testing to ensure file is loaded correctly
print(df.head(2))

# will iterate through all cells
for col in df.columns:
    # using regex, check for any non-character or non-number values. If they exist, remove them.
    df[col] = df[col].str.replace(r'\W', "")

# export to new Excel file. In case of errors, not a good idea to overwrite the original before testing!
df.to_excel("removed_characters.xlsx")
