#to make a program where it will update the amount a person has
file_name='E:\CMPSCI\PYTHON\RESULT\Bank_py\Bank_update.txt'
#to display the amount currently in bank 
with open(file_name) as file_object:
    balance= file_object.read()
    balance_2= balance
    balance = float(balance) #to convert string t float
    print('Current balance: '+str(balance))
er=0 # to decode error in the main_sheet.txt
#to ask wheter to credit or debit
print('press [1] for deposit or [2] for debit')
choice = int(input())
pass_file='hello'
#condition begins
if choice == 1:
 print('Enter password:')
 pass_file_1=input()
 if pass_file_1 == pass_file:
    print('Amount to be credited:')
    amt=float(input())
    balance+=amt
    #write the latest amount in the balance sheet
    with open(file_name,'w') as file_object:
        file_object.write(str(balance))
    print('Current balance[N]: '+str(balance))
 else:
    er=1
    print('Password Invalid')
#condition for the debit
elif choice == 2:
 print('Enter password:')
 pass_file_1=input()
 if pass_file_1 == pass_file:
    print('Amount to be debited:')
    amt=float(input())
    if amt > balance:
        er=1
        print('Balnace Not Enough!')
    else :
        balance=balance-amt
        print('Sucessfully debited '+str(amt)+'!') 
        #write the latest amount in the balance sheet
        with open(file_name,'w') as file_object:
           file_object.write(str(balance))
        print('Current balance[N]: '+str(balance))
 else :
    er=1
    print('Password Invalid')
#condition for non valid input 
else :
    er=1
    print('Invalid Input!')

if er == 0:
 #to print updated account statements 
 #to display date 
  from datetime import date
  today = date.today()
 #to display current time 
  import datetime
  e = datetime.datetime.now()
  current_time = e.strftime("%I:%M:%S %p")
  #to print processing time of a program
  import time
  start_time = time.time() - 0.112
  process = "%s seconds " % (time.time() - start_time)
 #to print statements


 #to print date and time
  file_name_2 = 'E:\CMPSCI\PYTHON\RESULT\Bank_py\main_sheet.txt'

  with open(file_name_2,'a') as file_object:
     file_object.write('date: '+str(today)+"\t"+'time: '+str(current_time)+"\n")
 #to write in the balance upadtes

  with open(file_name_2,'a') as file_object:
     file_object.write('server_id:'+"\t"+str(id(balance))+"\n")
     file_object.write('balance[P]:'+"\t"+balance_2+"\n")
     file_object.write('balance update:'+"\t"+str(float(balance)-float(balance_2))+"\n")
     file_object.write('balance[N]:'+"\t"+str(balance)+"\n")
     file_object.write('server_acess_period:'+"\t"+str(process)+"\n")
     file_object.write('------------------------------------------------------')
     file_object.write("\n")

else:
 #to print updated account statements 
 #to display date 
  from datetime import date
  today = date.today()
 #to display current time 
  import datetime
  e = datetime.datetime.now()
  current_time = e.strftime("%I:%M:%S %p")
  #to print processing time of a program
  import time
  start_time = time.time()-0.105
  process =" %s seconds " % (time.time() - start_time)
 #to print statements


 #to print date and time
  file_name_2 = 'E:\CMPSCI\PYTHON\RESULT\Bank_py\main_sheet.txt'

  with open(file_name_2,'a') as file_object:
     file_object.write('date: '+str(today)+"\t"+'time: '+str(current_time)+"\n")
    
    
  with open(file_name_2,'a') as file_object:
        file_object.write('server_id:'+"\t"+str(id(balance))+"\n")
        file_object.write('balance[P]:'+"\t"+balance_2+"\n")
        file_object.write('Error in processing !'+"\n")
        file_object.write('server_acess_period:'+"\t"+str(process)+"\n")
        file_object.write('------------------------------------------------------')
        file_object.write("\n")






