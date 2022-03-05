import pandas as pd
import pyodbc 

#use this funciton for add datas to sql
def user_information_send(name,surname,mail,phone,password,username):
    server = '***'  #pls write to yout sql server name
    database = '***' #your database name to which you want to add the information
        
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    cursor.execute('SELECT * FROM ****') #write your table name to ****

    info = []

    info.append(name)
    info.append(surname)
    info.append(mail)
    info.append(phone)
    info.append(password)
    info.append(username)
    
    #write your table name to ****
    cursor.execute(''' INSERT INTO **** (uName,uPass,name,surname,eMail,phone) 
                VALUES
                (?,?,?,?,?,?)''',(info[5],info[4],info[0],info[1],info[2],info[3])
                )

    cnxn.commit()

#take datas from sql
def take_data():
    server = '***'  #pls write to yout sql server name
    database = '***' #your database name to which you want to add the information
        
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    #Name is my variable in my sql table you can change whatever you want 
    cursor.execute('SELECT Name FROM ****') #write your table name to ****

    data = cursor.fetchall()
    # data[1][1] meaning is first row and first column in sql courses

    #create list for take data in sql
    list_data = []

    b  = 0

    #taking datas from sql
    for i in data:
        list_data.append(data[b])
        b = b + 1
    #return all data for use other python files
    return list_data  

#this index for choosing which data we want to delete from sql
def clear_data(index):

    #CREATE LIST AND ASSING THE SQL DATA WITH USE TAKE DATA FUNCTION
    data = []
    data = take_data()

    #take clearing data from all sql datas in data variable
    clearing_data = str(data[index][0])
    #change spaces to nothing
    clearing_data = clearing_data.replace(" ", "") 

    server = '***'  #pls write to yout sql server name
    database = '***' #your database name to which you want to add the information
    
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    #write your table name to ****
    statement= """DELETE FROM **** WHERE uName = ?"""

    cursor.execute(statement,(clearing_data,))

    cnxn.commit()

#take old data and new datas from user and then replace this datas from sql
def update_data(old_data,name,surname,mail,phone,username):
    #connect server
    server = '***'  #pls write to yout sql server name
    database = '***' #your database name to which you want to add the information

    #connet cursor
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()


    #write your table name to ****
    #update to datas in sql
    sql = """UPDATE **** SET uName = ? WHERE uName = ?"""
    cursor.execute(sql,(username,)+(old_data[1],))  

    sql = """UPDATE ****  SET name = ? WHERE name = ?"""
    cursor.execute(sql,(name,)+(old_data[3],)) 

    sql = """UPDATE ****  SET surname = ? WHERE surname = ?"""
    cursor.execute(sql,(surname,)+(old_data[4],)) 

    sql = """UPDATE ****  SET eMail = ? WHERE eMail  = ?"""
    cursor.execute(sql,(mail,)+(old_data[5],)) 

    sql = """UPDATE ****  SET phone = ? WHERE phone  = ?"""
    cursor.execute(sql,(phone,)+(old_data[6],)) 

 

    cnxn.commit()

#add informations to your sql table
user_information_send("Seyit", "KOYUNCU", "blabla@gmail.com", "123456789", "Seyit1234", "SeyitK")

clear_data(3) #delte 3. data from sql

data = take_data() #take all datas from sql

#replace old datas and new datas from sql
old_data = ["Seyit", "KOYUNCU", "blabla@gmail.com", "123456789", "Seyit1234", "SeyitK"]
update_data(old_data, "newSeyit", "newKOYUNCU", "newblabla@gmail.com", "new123456789", "newSeyit1234", "newSeyitK")
