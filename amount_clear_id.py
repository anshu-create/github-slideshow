#to clear all the bank statements on executing
file_name = 'E:\CMPSCI\PYTHON\RESULT\Bank_py\main_sheet.txt'
#to write the defaut statements
with open(file_name,'w') as file_object:
    file_object.write('Name: Anshuman Pattnaik')
    file_object.write("\n")
    file_object.write("user_id='anshumanpattnaik@ybl_sbi'")
    file_object.write("\n")
    file_object.write('-------------------UPDATE-SATEMENTS-------------------')
    file_object.write("\n")
#to print to know tha job has been done in the terminal
print('Account_update_statements_satus: cleared')