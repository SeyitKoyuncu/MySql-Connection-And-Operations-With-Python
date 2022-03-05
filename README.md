# MySql-Connection-And-Operations-With-Python
In this repository, i try to explain sql connections and operations with python.


In this file, i have 4 basic funciton for mysql server and i will explain basicly this funcitons, also int he inside of the file (MySqlFunctionsWithPython.py) codes line nhave so much descriptions about their work. 


###### FUNCTION DESCRIPTIONS #########

Send(name,surname,mail,phone,password,username):
  
    In this funciton we take the datas, and add to the My Sql table.
    
takeData():
    
    In this function, we take datas from sql.
    
clearData(index):

     In there, we have index variable for choose the which row we want to delete in the sql. First we take all datas from sql with takeData funciton (i know if your project
     will be have so much data this method can't be effective but it can be developed.) then we assing to the list and take the indexth data then clear from sql to this data.
     
     
updateData(old_data,name,surname,mail,phone,username):

    This function take old data(in list) and the new datas, then update the sql datas which name is same as the old datas.
