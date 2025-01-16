# Task Title: Build a Dynamic News Feed with Pagination.

''' Task Overview :- 
In this task, you will develop a simple news feed application where users can
add news title, description, news image path and save it.
Application should display option / menu to add news feed and list existing news feed.

> Select your choice
1. Add news details
2. List news
3. Exit app

After option 1 section app should ask
Enter News Title
Enter News details
Enter Photo path or url
On Selection of option 2 App should display all news added.'''

import mysql.connector as ms
con = ms.connect(host="localhost",user="root",password="")
if con.is_connected():
    print("Connection Successfully Build. \n")
cr = con.cursor()
try:
    cr.execute(' create database if not exists dbnews')
    print("Database Successfully Created. \n")
    con.database='dbnews'
except Exception as e:
    print(f"Error! Creating Database. {e} ")

try:
    cr.execute('''create table if not exists newstable (
               id int primary key auto_increment,
               title varchar(450),
               news text)
                ''')  
    print(f"Table Successfully Created")

except Exception as e:
    print(f"Error! Creating Table. {e} ")

def add_news():
    title=input("Enter News Title : ")
    news=input("Enter News in details : ").strip()
    query="insert into newstable (`title`,`news`) Values ('{}','{}')".format(title,news)
    cr.execute(query)
    con.commit()
    news_id=cr.lastrowid
    print(f"\n\t\t\t\t\t\t\t\tNews Uploaded Successfully!")
    sql="select * from newstable where id={} ".format(news_id)
    cr.execute(sql)
    rec=cr.fetchall()
    for i in rec:
        print(f"News ID: {i[0]}\n \t\t\t\t\t {i[1]}. \n{i[2]} " )
def show_all_news():
    query="select * from newstable"
    cr.execute(query)
    rec=cr.fetchall()
    if len(rec)>0:
        for i in rec:
            print(f"News ID: {i[0]}\n \t\t\t\t\t {i[1]}. \n{i[2]} " )
            print("\t\t\t\t\t\t\t\t***********************")
        print("_______________________________________________________________________________________________________________________") 
    else:
        print("No News Available!!!")       


def option():
    while True:
        print("\nChoice from these option which task you want perform-\n")
        print(" 1. Add News Details. \n 2. Show All News. \n 3. Exit. \n")
        task=input("Enter Your Choice: ")
        if task=='1':
            add_news()
        elif task=='2':
            show_all_news()
        elif task=='3':
            print('\nExiting from the app.....')
            break
        else:
            print("\nInvalid Input, Please Enter Valid Option.\n")
            option() 
        continue_choice = input("\n Do you want to perform another task? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print('Exiting the system...')
            break    
                

option()


