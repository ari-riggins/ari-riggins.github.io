import csv

filename = "finalData.csv"

fields = []
rows = []

# Read the file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    # print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
 
#  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     # parsing each column of a row
#     for col in row:
#         print("%10s"%col,end=" "),
#     print('\n')

jsCode = "var dataArray = [];"
jsCode += '\n'
jsCode += "var nameArray = [];"
jsCode += '\n'
# generate javascript code from this
count = 0
for field in fields:
    jsCode += "nameArray[" + str(count) + "] = " + field + ";"
    # jsCode += "var field" + str(count) + " = " + field + ";"
    jsCode += '\n'
    count = count + 1

# count = 1
# for row in rows:
#     jsCode += "dataArray[0][" + str(count) + "] = " + row[0] + ";"
#     count = count + 1
#     jsCode += '\n'
    # jsCode += "var name" + str(count) + " = " + row[0] + ";"

#Actually just make an array instead and parse this in the javascript lol

count = 0
# countCol = 0
# for row in rows:
#     # parsing each column of a row
#     for col in row:
#         info = "info = const " + str(count) + " = {" + rows[count][0] + ":" + col + ";"
#         jsCode += info
#         jsCode += '\n'
#         # jsCode += "dataArray[" + str(count) + "] = dataArray[" + str(count) + "] +"
#         jsCode += "dataArray[" + str(count) + "] = info;"
#         jsCode += '\n'
#         countCol += 1
#     count += 1


# for row in rows:
#     colCount = 0
#     # info = "dataArray[" + str(count) + "] = {"
#     for col in row:
#         # jsCode += "info = "
#         jsCode += "dataArray[" + str(count) + "] = " + col + ";"
#         count += 1
#         jsCode += '\n'
# print(jsCode)

# jsCode += '\n'
# for field in fields:
#     for row in fields:
#         info = "info = const " + str(count) + " = {" + field + ":" + row + ";"
#         jsCode += info
#         jsCode += '\n'
#         # jsCode += "dataArray[" + str(count) + "] = dataArray[" + str(count) + "] +"
#         jsCode += "dataArray[" + str(count) + "] = info;"
#         jsCode += '\n'

# print(jsCode)

#this kinda works!
for row in rows:
    info = "dataArray[" +str(count) + "] = " + str(row) + ";"
    jsCode += info
    jsCode += '\n'
    count += 1

print(jsCode)

# for row in rows:
#     count = 0
#     for col in row:
#         info = "info = const " + str(count) + " = {" + rows[count][0] + ":"
#         for row in row:
#             info += col + ", "
#         count += 1
#     info += "}"
#     print(info)


