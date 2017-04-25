import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use credentials to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

# find a workbook by name and open the first sheet
# make sure you use the right name here.
sheet = client.open("test_data").sheet1

# extract and print all records
list_of_all_records = sheet.get_all_records()
print(list_of_all_records)

# extract and print all sheet values
list_of_all_values = sheet.get_all_values()
print(list_of_all_values)

# extract and print all first row values
list_of_row_1_values = sheet.row_values(1)
print(list_of_row_1_values)

# extract and print all first columne values
list_of_columne_1_values = sheet.col_values(1)
print(list_of_columne_1_values)

# extract and print all values of celle 1x1
list_of_cell_1_1 = sheet.cell(1, 1).value
print(list_of_cell_1_1)

# delete row #1 and extract and print all values
list_of_hashes = sheet.update_cell(1, 1, "Enter data into sheet")
print(list_of_cell_1_1)

# delete row #1 and extract and print all values
row = ["A","new","row"]
index = 1
list_of_new_row = sheet.insert_row(row, index)
print(list_of_new_row)

# delete row #1 and extract and print all values
list_of_delete_row_1 = sheet.delete_row(1)
print(list_of_delete_row_1)

# count all rows
list_of_count_rows = sheet.row_count
print(list_of_count_rows)
