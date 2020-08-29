from datetime import datetime
from csv import writer

startTime = datetime.now()

message = input("How many times do you want to print 'Hello World'? ")
n = int(message)
for i in range(n):
    print("Hello World!")

time = datetime.now() - startTime
print("It took " ,time, "seconds to run this program.")

def append_list_as_row(file_name, list_of_elem): 
    with open(file_name, 'a+', newline ='') as write_obj: 
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

row_contents = [n,time]
append_list_as_row('hm_1a.csv',row_contents)



    