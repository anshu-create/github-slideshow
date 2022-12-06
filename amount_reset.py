#to sign default value to the bank amount 
file_name='E:\CMPSCI\PYTHON\RESULT\Bank_py\Bank_update.txt'
file_name_2 = 'E:\CMPSCI\PYTHON\RESULT\Bank_py\main_sheet.txt'
#to ask user to assignt he intial value
print("Enter the initial value :")
assign = float(input())
#to read the balance and print
with open(file_name) as file_object:
     balance = file_object.read()
#to write the assigned value in the main sheet
with open(file_name,'w') as file_object:
     file_object.write(str(assign))

#to print updated account statements
#to display date 
from datetime import date
today = date.today()
#to display current time 
import datetime
e = datetime.datetime.now()
current_time = e.strftime("%I:%M:%S %p")

import time
start_time = time.time()-0.102
process =" %s seconds " % (time.time() - start_time)
#to print statements


#to print date and time
with open(file_name_2,'a') as file_object:
     file_object.write('date: '+str(today)+"\t"+'time: '+str(current_time)+"\n")
#to write in the balance upadtes
with open(file_name_2,'a') as file_object:
     file_object.write('server_id:'+"\t"+str(id(balance))+"\n")
     file_object.write('balance[P]:'+"\t"+balance+"\n")
     file_object.write('balance reseted to '+str(assign)+' !'+"\n")
     file_object.write('server_acess_period:'+"\t"+str(process)+"\n")
     file_object.write('------------------------------------------------------')
     file_object.write("\n")
     






