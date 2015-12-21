import csv
f = open("orders.csv", 'rU')
csvreader = csv.reader(f)
orders = list(csvreader)
sum_orders = []
static = {"<1.000.000" :0, "1.000.000<x<2.000.000" :0, "2.000.000<x<3.000.000" :0, ">3.000.000" :0}


for items in orders[1:len(orders)]:
    items[4] = items[4].replace(",","")
    sum_orders.append(int(items[4]))
   
for i in sum_orders:
    if i > 3000000:
        static[">3.000.000"] += 1
    elif i > 2000000:
             static["2.000.000<x<3.000.000"] += 1
    elif i > 1000000:
             static["1.000.000<x<2.000.000"] += 1
    else: static["<1.000.000"] += 1
                            
print(static)
        
    




