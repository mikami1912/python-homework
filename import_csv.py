import csv
class import_csv():
    def __init__(self, filename):
        self.name = filename
        f = open(self.name, 'rU')
        csvreader = csv.reader(f)
        self.listdata = list(csvreader)
        
        
    def extract_data_col(self, col):
        col_data = []
        for items in self.listdata[1:len(self.listdata)]:
            col_data.append(items[col])
        return col_data
    
    
        
