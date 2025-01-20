# Task Overview:

''' You will develop a simple todo list application that saves tasks, allowing users to view and
manage their tasks. The app will include functionalities for adding new tasks, editing existing
tasks, and deleting tasks.

Allow users to:
▪ Add new tasks.
▪ Edit existing tasks.
▪ Remove tasks.
▪ List all task

Store Task Title - ex. Meeting at 9pm
Store Task status - New, In Progress, Completed, Cancelled
When Added the task will be by default in New state.'''

import mysql.connector as ms
con = ms.connect(host="localhost",user="root",password="")
if con.is_connected():
    print("Connection Successfully Build. \n")
cr = con.cursor()
try:
    cr.execute(' create database if not exists dbroutine')
    print("Database Successfully Created. \n")
    con.database='dbroutine'
except Exception as e:
    print(f"Error! Creating Database. {e} ")

try:
    cr.execute('''create table if not exists todotable (
               id int primary key auto_increment,
               task text,
               status enum('New','In Progress','Completed','Cancelled'))
                ''')  
    print(f"Table Successfully Created")

except Exception as e:
    print(f"Error! Creating Table. {e} ")

def add_task():
    task=input("Enter Your Appointment/Work. : ").strip()
    status='New'
    query="insert into todotable (`task`,`status`) values ('{}','{}')".format(task,status)
    cr.execute(query)
    con.commit()
    task_id=cr.lastrowid
    print(f"\n\t\t\t\t\t\t\t\tTask Uploaded Successfully!")
    update_task(task_id)
def show_all_task():
    query="select * from todotable"
    cr.execute(query)
    rec=cr.fetchall()
    if len(rec)>0:
        print(f"\t\tTaskID\t\tStatus\t\tTask\n" )
        for i in rec:
            print(f"\t\t{i[0]}\t\t{i[2]}\t\t{i[1]}")
        print("_______________________________________________________________________________________________________________________") 
    else:
        print("No Task Available!!!")        

def update_task(id=0):
    if id<=0:
        id=int(input("Enter Task ID: "))
    query="select * from todotable where id={}".format(id)
    cr.execute(query)
    rec=cr.fetchall()
    if len(rec)>0:
        print(f"\t\tTaskID\t\tStatus\t\tTask\n" )
        for i in rec:
            print(f"\t\t{i[0]}\t\t{i[2]}\t\t{i[1]}")
        print("_______________________________________________________________________________________________________________________") 
        print("What you want to update. \n 1. Task \n 2. Status ")
        task=input("what do you want to perform :  ")
        if task=='1':
            tsk = input("Enter task what you want update : ")
            query="update from todotable where id={}".format(id)
            cr.execute(query)
            con.commit()
            print("\n\t\t\tTask successfully updated!\n")
            search_id(id)
        elif task=='2':
            status=input("Enter status of your this task (e.g. In Progress, Completed, Cancelled )")
            query="UPDATE `todotable` SET `status` = '{}' WHERE `id` = {};".format(status,id)
            cr.execute(query)
            con.commit()
            print("\n\t\t\tStatus of your task has been successfully updated!\n")
            search_id(id)
        else:
            print("Invalid Input, Please enter valid input.")   
    else:
        print(f"No Task Found at task id {id}!!!")

def search_id(id=0):
    if id<=0:
        id=int(input("Enter Task ID: "))
    query="select * from todotable where id={}".format(id)
    cr.execute(query)
    rec=cr.fetchall()
    if len(rec)>0:
        print(f"\t\tTaskID\t\tStatus\t\tTask\n" )
        for i in rec:
            print(f"\t\t{i[0]}\t\t{i[2]}\t\t{i[1]}")
        print("_______________________________________________________________________________________________________________________")
    else:
        print(f"No Task Found at task id {id}!!!")    
          
def delete_task():
    id=int(input("Enter Task ID: "))
    update_task(id)
    query="delete from todotable where id={}".format(id)
    cr.execute(query)
    if cr.rowcount>0:
        permission=input("Do you want to delete this task (yes/no): ").lower()
        if permission=='yes':
            con.commit()
            print(f"\nSuccessfully, task id {id} has deleted as your permission. \n")
            show_all_task()
        else:
            print(f"Task id {id} has not deleted as your permission. ")   


def choice():
    print("\nChoice the option from the list.")
    print(" 1▪ Add new tasks.\n 2▪ Edit existing tasks.\n 3▪ Remove tasks.\n 4▪ List all task")
    task=input("Enter Your Task which task you want to perform:")
    if task=="1":
        print("1")
        add_task()
    elif task=="2":
        print("2")
        update_task(id=0)
    elif task=="3":
        print("3")
        delete_task()
    elif task=="4":
        print("4")
        show_all_task()
    else:
        print("Invalid Input, Please enter valid option from these.")                
choice()


