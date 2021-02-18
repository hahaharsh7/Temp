from csv import writer, reader

class CSVWriter:
    
    def __init__(self,file_name, headers):
        self.file_name = file_name
        with open(file_name, "w+") as my_empty_csv:
            csv_writer = writer(my_empty_csv)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(headers)
            

    
    def write(self, list_of_elem):
        # Open file in write mode
        with open(self.file_name, 'w+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
        
    def append(self, list_of_elem):
        # Open file in append mode
        with open(self.file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)

    def read(self):
        list_of_rows = []
        # read csv file as a list of lists
        with open(self.file_name, 'r+') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Pass reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
        return list_of_rows