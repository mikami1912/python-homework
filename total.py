from import_csv import import_csv
import csv

filename = "orders.csv"
data = import_csv(filename)
code = data.extract_data_col(0)

print(code)

comapre_value = False
for i in range(1,len(code)-1):
    for j in range(i+1,len(code)):
        print("compare ",code[i], "with ", code[j], " ", code[i] == code[j])

