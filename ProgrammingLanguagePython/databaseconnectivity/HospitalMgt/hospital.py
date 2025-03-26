import mysql.connector as ms #import sql connector 
# connect with sql 
con = ms.connect(host="localhost",user="root",password="",database= "dbhospital")
cr = con.cursor()

# Voice Speaking
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 130)  # Speed of speech
engine.setProperty('volume',0.9 )  # Volume (0.0 to 1.0)

# The text you want to convert to speech
text = "Hello, User ! Welcome to Apna Nursing Home."

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()

class Patient:
    def __init__(self):
        pass
    def add_patient(self,name,age,gender,fees,mobile):
        # Write Query
        query = "insert into patient(`name`, `age`, `gender`, `fee`,`mobile_no`) values('{}',{},'{}',{},'{}')".format(name,age,gender,fees,mobile)
        # execute the query by cursor method variable.
        cr.execute(query)
        con.commit()#save the data in table..
        id=cr.lastrowid
        Patient.search_by_id(Patient,id)
        print("\n\t\t\t\tSuccesfully, Patient Id created!!! ")

    def view_patient_list(self):
        sql="select * from patient"
        cr.execute(sql)
        # rec=cr.fetchall()
        print("\n\t\t\t\t\t\tAll Patient List \n\t\t\t\t\t     --------------------- \n\nTNO\tPID\t\tNAME\t\t\tAGE\tGENDER\t\tFEES\t\t\tMOBILE\t\tCHECKUP_DATE")
        for x in cr:
            print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t{x[4]}\t\t{x[5]}\t\t\t{x[6]}\t{x[7]}")
        print(" ")
    def search_by_name(self,name):
        sql = "select * from patient where name like '%{}%'".format(name)
        cr.execute(sql)
        rec=cr.fetchall()
        if len(rec)>0:
            print("\n\t\t\t\t\t     List By Patient Name \n\t\t\t\t\t  ------------------------- \n\nTNO\tPID\t\tNAME\t\t\tAGE\tGENDER\t\tFEES\t\t\tMOBILE\t\tCHECKUP_DATE")
            for x in rec:
                print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t{x[4]}\t\t{x[5]}\t\t\t{x[6]}   {x[7]}")
        else:
            print(f"Patient Name: {name} is not found in our record.")        
    def search_by_id(self,token=0):
        sql = "select * from patient where Token={}".format(token)
        cr.execute(sql)
        rec=cr.fetchall()
        if len(rec)>0:
            print("\nTNO\tPID\t\tNAME\t\t\tAGE\tGENDER\t\tFEES\t\t\tMOBILE\t\tCHECKUP_DATE")
            for x in rec:
                print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t{x[4]}\t\t{x[5]}\t\t\t{x[6]}   {x[7]}")
        else:
            print(f"Patient Token {token} is not found in our record.")        
    def update_fee_record(self,fees,tkno):
        query="update patient set fee=fee+{} where Token={}".format(fees,tkno)
        cr.execute(query)
        con.commit()
        print(f"\n\t\t\t\t\t   Successfully, token id {tkno} patient fee data updated!")
        Patient.search_by_id(Patient,tkno)
    def delete_patient_rec(self,tkno):
        sql="delete from patient where Token={}".format(tkno)
        cr.execute(sql)
        if cr.rowcount>0:
            con.commit()
            Patient.view_patient_list(Patient)
            print(f"\n\t\t\t\t\t\tSuccessfully, token id {tkno} patient data removed!   ")
        else:
            print(f"Patient Token {tkno} is not found in our record.")    

class Doctor:
    def __init__(self):
        pass
    def add_doctor(self,name,mobile,specilization):
        # Write Query
        query = "insert into doctor (`dr_name`, `specialization`, `contact_no`) values('{}','{}','{}')".format(name,specilization,mobile)
        # execute the query by cursor method variable.
        cr.execute(query)
        con.commit()#save the data in table..
        id=cr.lastrowid
        Doctor.search_by_id(Doctor,id)
        print("\n\t\t\t\t\tSuccesfully, Your Data Submitted!!!!")
    def view_doctor_list(self):
        sql="select * from doctor"
        cr.execute(sql)
        # rec=cr.fetchall()
        print("\n\t\t\t\t\t\tAll Doctor List \n\t\t\t\t\t     --------------------- \n\n\t\tID\tDR_ID\t\tDR_NAME\t\t\tSPECILIZATION\t\t\t\tMOBILE")
        for x in cr:
            print(f"\t\t{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t\t\t{x[4]}")
        print(" ")
    def search_by_id(self,id):
        sql = "select * from doctor where id={}".format(id)
        cr.execute(sql)
        rec=cr.fetchall()
        if len(rec)>0:
            print("\n\t\tID\tDR_ID\t\tDR_NAME\t\t\tSPECILIZATION\t\t\t\tMOBILE")
            for x in rec:
                print(f"\t\t{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t\t\t{x[4]}")
        else:
            print(f"Doctor ID {id} is not found in our record.")        
    def search_by_specilization(self,speci):
        sql = "select * from doctor where specialization like '%{}%';".format(speci)
        cr.execute(sql)
        rec=cr.fetchall()
        if len(rec)>0:
            print("\n\t\t\tList By Doctor Specilization \n\t\t\t       ------------------------- \n\n\t\tID\tDR_ID\t\tDR_NAME\t\t\tSPECILIZATION\t\t\t\tMOBILE")
            for x in rec:
                print(f"\t\t{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t\t\t{x[4]}")   
        else:
            print(f"Doctor Specilization {speci} is not found in our record.")        
    def delete_doctor_rec(self,id):
        sql="delete from doctor where id={}".format(id)
        cr.execute(sql)
        if cr.rowcount>0:
            con.commit()
            Doctor.view_doctor_list(Doctor)
            print(f"\n\t\t\t\t\t\tSuccessfully, doctor id {id} data removed! \n  ")
        else:
            print(f"Doctor ID {id} is not found in our record.")

class Appointment:
    def add_appointment(self,pid,did,dise_sym,refer_by):
        # Write Query
        query = "insert into appointment (`dr_id`, `pt_id`, `disease_symt`, `refer_by`) values({},{},'{}','{}')".format(did,pid,dise_sym,refer_by)
        # execute the query by cursor method variable.
        cr.execute(query)
        con.commit()#save the data in table..
        print("\n\t\t\t\t\tSuccesfully, Your Data Submitted!!!!")
    def view_appointment_list(self):
        sql="select * from appointment"
        cr.execute(sql)
        rec=cr.fetchall()
        print("\n\t\t     All Appointment List \n\t\t  ------------------------- \n")
        for i in rec:
            print(f"\n Appointment ID: {i[0]}\n Doctor ID: {i[1]}\n Patient ID: {i[2]}\n Disease Systums: {i[3]}\n Refer By: {i[4]}\n Prescription : {i[5]}")
        print("\n________________________________********************************________________________________\n")
    def search_by_appointment_id(self,aid):
        sql="select * from appointment where app_id={}".format(aid)  
        cr.execute(sql)
        rec=cr.fetchall()
        if len(rec)>0:
            for i in rec:
                print(f"\n\n Appointment ID: {i[0]}\n Doctor ID: {i[1]}\n Patient ID: {i[2]}\n Disease Systums: {i[3]}\n Refer By: {i[4]}\n Prescription : {i[5]}")
            print("\n________________________________********************************________________________________\n")
        else:
            print(f"Appointment ID {aid} is not found in our record.")    
    def search_by_patient_id(self,pid):
        sql="select * from appointment where pt_id={}".format(pid)
        cr.execute(sql)
        rec=cr.fetchall()
        if len(rec)>0:
            for i in rec:
                print(f"\n\n Appointment ID: {i[0]}\n Doctor ID: {i[1]}\n Patient ID: {i[2]}\n Disease Systums: {i[3]}\n Refer By: {i[4]}\n Prescription : {i[5]}")
            print("\n________________________________********************************________________________________\n")
        else:
             print(f"Patient ID {pid} is not found in our appointment record.")   
    def update_appointment(self,pid,prescripation):
        query="update appointment set prescription='{0}' where `pt_id`={1}".format(prescripation,pid)
        cr.execute(query)
        con.commit()
        Appointment.search_by_patient_id(Appointment,pid)
        print(f"\n\t\t\tSuccessfully, Patient id {pid} of patient data updated with prescription! \n")
    def delete_appointment_rec(self,id):
        sql="delete from appointment where app_id={}".format(id)
        cr.execute(sql)
        if cr.rowcount>0:
            con.commit()
            print(f"\n\t\t\tSuccessfully, appointment id {id} of patient data removed! ")
            Appointment.view_appointment_list(Appointment)
        else:
            print(f"Appointment ID {id} is not found in our record.")    
        

def options():
    while True:
        print("Choice from the option on which you want to perform task.")
        print("1. Patient Related.")
        print("2. Doctor Related.")
        print("3. Appointment Related.\n")
        while True:
            choice = input("Enter Your Choice: ")
            if choice == '1' or choice == 'patient':
                print("\nNow choice which task you perform on patient.")
                print("1. Add Patient.")
                print("2. View Patient.")
                print("3. Search Record.")
                print("4. Update Fees.")
                print("5. Delete Record.")
                while True: 
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        print("\n\t\t\t\t\tINSERT NEW PATIENT DATA.\n")
                        try:
                            while True:
                                try:
                                    pre_mobile = '+91'
                                    mobile = int(input("Enter Patient Mobile Number :- "))
                                    if mobile <1000000000  or mobile > 9999999999:
                                        print("Mobile number must have 10 digits or positive integer.")
                                        continue
                                    mobile = pre_mobile + str(mobile)
                                    print(mobile)
                                    break
                                except ValueError:
                                    print("Invalid number! Please enter a valid mobile number.")
                            while True:
                                try:
                                    static_var = 'Pt. '
                                    name = input("\nEnter Patient Name :- ").strip().capitalize()
                                    if not name:
                                        print("Name can't be empty.")
                                        continue
                                    if not name.isalpha():
                                        print("Name can't contain numeric or special character, only have alpha.")
                                        continue
                                    name = static_var + name
                                    break
                                except ValueError:
                                    print("Invalid input! Please enter name, it can't be empty.")
                            try:
                                sql = "select * from patient where mobile_no = '{0}' and name = '{1}'".format(mobile, name)
                                cr.execute(sql)
                                rec = cr.fetchall()
                                if cr.rowcount > 0:
                                    print("\n\t\t\t\tPatient already exists!")
                                    print("\nTNO\tPID\t\tNAME\t\t\tAGE\tGENDER\t\tFEES\t\t\tMOBILE\t\tCHECKUP_DATE")
                                    for x in rec:
                                        print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t{x[4]}\t\t{x[5]}\t\t\t{x[6]}\t{x[7]}")
                                else:
                                    while True:
                                        try:
                                            age = int(input("Enter Patient Age :- "))
                                            if age <= 0:
                                                print("Age must be a positive integer.")
                                                continue
                                            break
                                        except ValueError:
                                            print("Invalid input! Please enter a valid number for age.")
                                    while True:
                                        ls = ['Male', 'Female', 'Other']
                                        try:
                                            gender = input("Enter Patient Gender(Male/Female/Other) :- ").strip().capitalize()
                                            if gender not in ls:
                                                print("Gender must be 'Male', 'Female', or 'Other'")
                                                continue
                                            break
                                        except ValueError:
                                            print(f"Invalid input! Please enter a valid gender {ls}.")
                                    while True:
                                        try:
                                            fees = int(input("Enter Patient Fees :- "))
                                            if fees < 0:
                                                print("Fees cannot be negative.")
                                                continue
                                            break
                                        except ValueError:
                                            print("Invalid input! Please enter a valid number for fees.")
                                    Patient.add_patient(Patient, name, age, gender, fees, mobile)
                                    try:
                                        while True:
                                            try:
                                                print("\n\t\t\t\t    Create Appointment of this patient. \n")
                                                tkno=int(input("\nEnter the patient token number(TNO) given above (e.g., 1,2,3) :- "))
                                                if tkno<0:
                                                    print("Token No. must be positive integer and strat from 1,2 so on.. ")
                                                    continue
                                                break
                                            except ValueError as ve:
                                                print("Invalid Input! Please enter valid number for token no. {ve}")
                                        while True:
                                            try:
                                                disease_symt=input("Enter Disease Symptoms of Patient: ")
                                                if not disease_symt:
                                                    print("Disease Symptoms Can't be empty. ")
                                                    continue
                                                break
                                            except ValueError as ve:
                                                print(f"Error {ve}")
                                        while True:
                                            try:
                                                id=int(input("\nEnter the doctor id (e.g., 1,2,3) :- "))
                                                if tkno<0:
                                                    print("Doctor id must be positive integer and strat from 1,2 so on.. ")
                                                    continue
                                                break
                                            except ValueError as ve:
                                                print("Invalid Input! Please enter valid number for token no. {ve}")            
                                        refer_by = input("Enter Reference By : ").capitalize().split()
                                        if not refer_by:
                                            refer_by="Self"	    
                                        Appointment.add_appointment(Appointment,tkno,id,disease_symt,refer_by)  
                                        Appointment.search_by_patient_id(Appointment,tkno)  
                                        

                                    except Exception as e:
                                        print(f"Something went wrong! {e}")

                            except ValueError:
                                print("Patient already existed.....\nToken already exists, it must be unique")
                        except Exception as e:
                            print(f"<--------- NOT SUBMITTED ---------> Error: {e}")
                    elif choice == '2':
                        print("\n\t\t\t\t\tSHOW PATIENT DATA.\n")
                        Patient.view_patient_list(Patient)
                    elif choice == '3':
                        print("\nChoice! By which, you want to search the record: ")
                        print("1. By Name.")
                        print("2. By Token ID.")
                        choice = input("Enter Your Choice: ")
                        while True:
                            if choice == '1':
                                print("\n\t\t\t\t\tSEARCH PATIENT DATA BY PATIENT NAME.\n")
                                try:
                                    while True:
                                        try:
                                            name = input("\nEnter the patient Name to check all details :- ").strip()
                                            if not name:
                                                print("Name can't be empty.")
                                                continue
                                            Patient.search_by_name(Patient, name)
                                            break
                                        except ValueError:
                                            print("Invalid input! Please enter name, it can't be empty.")
                                except Exception as e:
                                    print(f"Something went wrong! Error: {e}")
                            elif choice == '2':
                                print("\n\t\t\t\t\tSEARCH PATIENT DATA BY PATIENT TOKEN ID.\n")
                                try:
                                    while True:
                                        tkno = int(input("\nEnter the patient token number (e.g., 1,2,3 ) to check all records of the patient. :- "))
                                        if tkno < 0:
                                            print("Token No. must be positive integer and start from 1,2,3 so on.")
                                            continue
                                        break
                                    Patient.search_by_id(Patient, tkno)
                                except Exception as e:
                                    print(f"Something went wrong! Error: {e}")
                            else:
                                print("Input valid choice.")
                                choice = input("Enter your choice again: ")
                                continue
                            break
                    elif choice == '4':
                        print("\n\t\t\t\t\tFEES UPDATE OF PATIENT BY PATIENT TOKEN ID.\n")
                        try:
                            while True:
                                try:
                                    tkno=int(input("\nEnter the patient token number (e.g., 1,2,3) you want to update fees :- "))
                                    if tkno<0:
                                        print("Token No. must be positive integer and strat from 1,2 so on.. ")
                                        continue
                                    sql = "select * from patient where Token = {}".format(tkno)
                                    cr.execute(sql)
                                    rec=cr.fetchall()
                                    if len(rec)>0:
                                        Patient.search_by_id(Patient,tkno)
                                        while True:
                                            try:
                                                fees=int(input("Enter the patient addition fees :- "))
                                                if fees<0:
                                                    print("Fees cannot be negative. ")
                                                    continue
                                                Patient.update_fee_record(Patient,fees,tkno)
                                                break
                                            except ValueError as ve:
                                                print("Invalid input! Please enter a valid number for fees {ve}.")
                                    else:
                                        print(f"Token id {tkno} is not found in our record")
                                        continue
                                    break            
                                except ValueError as ve:
                                    print("Invalid Input! Please enter valid number for token no. {ve}")

                        except Exception as e:
                            print("Something went wrong! {e} ")
                    elif choice == "5":
                        print("\n\t\t\t\t\tDELETE DATA OF PATIENT BY PATIENT TOKEN ID.\n")
                        try:
                            while True:
                                tkno=int(input("\nEnter the token no. (e.g., 1,2,3) of the patient which record you want to delete :- "))
                                if tkno<0:
                                    print("Token No. must be positive integer and start from 1,2 so on ")
                                    continue
                                Patient.delete_patient_rec(Patient,tkno)
                                break
                        except ValueError:
                            print("Invalid Input! Please enter valid number for token no.")
                    else:
                        print("Invalid input! Please enter a valid choice.")
                        continue
                    break
            elif choice == '2':
                print("DOCTOR RELATED TASK.")
                print("\nNow choice which task you perform on doctor.")
                print("1. Add Doctor.")
                print("2. View Doctor.")
                print("3. Search Doctor.")
                print("4. Delete Record.")
                while True:
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        print("\n\t\t\t\t\tINSERT NEW DOCTOR DATA.\n")
                        try:
                            
                            while True:
                                try:
                                    pre_mobile = '+91'
                                    mobile = int(input("Enter Mobile Number :- "))
                                    if mobile <1000000000  or mobile > 9999999999:
                                        print("Mobile number must have 10 digits or positive integer.")
                                        continue
                                    mobile = pre_mobile + str(mobile)
                                    print(mobile)
                                    break
                                except ValueError:
                                    print("Invalid number! Please enter a valid mobile number.")
                            while True:
                                try:
                                    static_var = 'Dr. '
                                    name = input("\nEnter Doctor Name :- ").strip().capitalize()
                                    if not name:
                                        print("Name can't be empty.")
                                        continue
                                    if not name.isalpha():
                                        print("Name can't contain numeric or special character, only have alpha.")
                                        continue
                                    name = static_var + name
                                    break
                                except ValueError:
                                    print("Invalid input! Please enter name, it can't be empty.")
                            try:
                                sql = "select * from doctor where contact_no = '{0}' and dr_name = '{1}'".format(mobile, name)
                                cr.execute(sql)
                                rec = cr.fetchall()
                                if cr.rowcount > 0:
                                    print("Doctor Detail already exists!")
                                    print("\nID\tDR_ID\t\tDR_NAME\t\t\tSPECILIZATION\t\t\tMOBILE")
                                    for x in rec:
                                        print(f"{x[0]}\t{x[1]}\t{x[2]}\t\t{x[3]}\t{x[4]}")
                                else:
                                    while True:
                                        try:
                                            specilization = input("Enter Doctor Specilization:- ")
                                            doctor_specializations = ["General Physician","General Surgeon","Cardiologist","Neurologist","Orthopedic Surgeon","Pediatrician",
                                                                      "Gynecologist/Obstetrician","Dermatologist","Ophthalmologist","ENT Specialist","Psychiatrist","Endocrinologist",
                                                                      "Gastroenterologist","Pulmonologist","Nephrologist","Urologist","Oncologist","Rheumatologist","Allergist/Immunologist",
                                                                      "Hematologist","Radiologist","Anesthesiologist","Pathologist","Plastic Surgeon","Vascular Surgeon",
                                                                      "Sports Medicine Specialist","Geriatrician","Neonatologist","Infectious Disease Specialist",
                                                                      "Palliative Care Specialist"]
                                            if not specilization:
                                                print("Specilization can't be empty. ")
                                                continue
                                            if specilization not in doctor_specializations: 
                                                print(f"Specilization must from {doctor_specializations} :")
                                                continue
                                            break
                                        except ValueError:
                                            print(f"Invalid input! Please enter a valid specilization.")
                                    Doctor.add_doctor(Doctor,name,mobile,specilization)
                            except ValueError:
                                print("Patient already existed.....\nToken already exists, it must be unique")
                        except Exception as e:
                            print(f"<--------- NOT SUBMITTED ---------> Error: {e}")
                    elif choice == '2':
                        print("SHOW DOCTOR LIST.")
                        Doctor.view_doctor_list(Doctor)
                    elif choice == '3':
                        print("\nChoice, by which you want to search the record: ")
                        print("1. By Specilization.")
                        print("2. By ID.")
                        choice = input("Enter Your Choice: ")
                        if choice == '1':
                            print("\n\t\t\t\t\tSEARCH DOCTOR DATA BY DOCTOR SPECILIZATION.\n")
                            try:
                                while True:
                                    try:
                                        specilization = input("\nEnter the doctor specilization to check all details :- ").strip()
                                        if not specilization:
                                            print("specilization can't be empty.")
                                            continue
                                        Doctor.search_by_specilization(Doctor,specilization)
                                        break
                                    except ValueError as ve:
                                        print(f"Invalid input! Please enter name, it can't be empty. {ve}")
                            except Exception as e:
                                print(f"Something went wrong! Error: {e}")
                        elif choice == '2':
                            print("\n\t\t\t\t\tSEARCH DOCTOR DATA BY DOCTOR ID.\n")
                            try:
                                while True:
                                    id = int(input("\nEnter the doctor id to check all details of the doctor. (start with e.g., 1, 2 and so on) :- "))
                                    if id < 0:
                                        print("id must be positive integer.")
                                        continue
                                    break
                                Doctor.search_by_id(Doctor, id)
                            except Exception as e:
                                print(f"Something went wrong! Error: {e}")
                        else:
                            print("Input valid choice.")
                    elif choice == "4":
                        print("\n\t\t\t\t\tDELETE DOCTOR RECORDS FROM DOCTOR LIST BY IT'S DOCTOR ID.\n")
                        try:
                            while True:
                                id=int(input("\nEnter the id (e.g., 1,2,3) of the doctor which record you want to delete :- "))
                                if id<0:
                                    print("id must be positive integer and start from 1,2 so on ")
                                    continue
                                Doctor.delete_doctor_rec(Doctor,id)
                                break
                        except ValueError as ve:
                            print(f"Invalid Input! Please enter valid number for id. {ve}")
                    else:
                        print("Invalid input!, Please enter valid choice.")
                        continue
                    break
            elif choice == '3':
                print("Appointment Related")
                print("\nNow choice which task you perform on appointment.")
                print("1. Add Appointment.")
                print("2. View Appointment list.")
                print("3. Search Appointment.")
                print("4. Update Appointment.")
                print("5. Delete Record.")
                while True:
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        print("\n\t\t\t\t\tADD APPOINTMENT BY TOKEN ID OF PATIENT TO DOCTOR (if patient not register firstly register). \n")
                        try:
                            while True:
                                try:
                                    tkno=int(input("\nEnter the patient token number(TNO) (e.g., 1,2,3) :- "))
                                    if tkno<0:
                                        print("Token No. must be positive integer and strat from 1,2 so on.. ")
                                        continue
                                    sql = "select * from patient where Token = {}".format(tkno)
                                    cr.execute(sql)
                                    rec=cr.fetchall()
                                    # print(rec)
                                    if len(rec)>0:
                                        while True:
                                            try:
                                                disease_symt=input("Enter Disease Symptoms of Patient: ")
                                                if not disease_symt:
                                                    print("Disease Symptoms Can't be empty. ")
                                                    continue
                                                break
                                            except ValueError as ve:
                                                print(f"Error {ve}") 
                                        while True:
                                            try:
                                                did=int(input("\nEnter the doctor id (e.g., 1,2,3) :- "))
                                                if did<0:
                                                    print("doctor id must be positive integer and strat from 1,2 so on.. ")
                                                    continue
                                                sql = "select * from doctor where id = {}".format(did)
                                                cr.execute(sql)
                                                rec=cr.fetchall()
                                                if len(rec)>0:
                                                    try:    
                                                        refer_by = input("Enter Reference By : ").capitalize()
                                                        Appointment.add_appointment(Appointment,tkno,did,disease_symt,refer_by)
                                                        Appointment.search_by_patient_id(Appointment,tkno)
                                                    except ValueError as ve:
                                                        print(f"error {ve}")
                                                else:
                                                    print(f"Doctor id {did} does not exist.")  
                                                    continue       
                                            except ValueError as ve:
                                                print(f"Invalid Input! Please enter valid number for token no. {ve}")
                                            break    
                                    else:
                                        print("This token id does not exist in your records may be it wrong or firstly you have to creaate patient token id.")   
                                        continue        
                                except ValueError as ve:
                                    print("Invalid Input! Please enter valid number for token no. {ve}")
                                break 	    
                        except Exception as e:
                            print(f"Something went wrong! {e}")

                    elif choice == '2':
                        print("\n\t\tSHOW APPOINTMENT LIST.\n")
                        Appointment.view_appointment_list(Appointment)
                    elif choice == '3':
                        print("\nChoice, by which you want to search the record: ")
                        print("1. By Appointment ID.")
                        print("2. By Token ID.")
                        choice = input("Enter Your Choice: ")
                        if choice == '1':
                            print("\n\t\tSHOW APPOINTMENT DATA BY APPOINTMENT ID.\n")
                            try:
                                while True:
                                    aid = int(input("\nEnter the appointment id to check all details of the regarding appointment . (start with e.g., 1, 2 and so on) :- "))
                                    if aid < 0:
                                        print("id must be positive integer.")
                                        continue
                                    break
                                Appointment.search_by_appointment_id(Appointment,aid)
                            except Exception as e:
                                print(f"Something went wrong! Error: {e}")
                        elif choice == '2':
                            print("\n\t\tSHOW APPOINTMENT DATA BY TOKEN ID OF PATIENT.\n")
                            try:
                                while True:
                                    pid = int(input("\nEnter the token id of patient to check all details of the regarding appointment . (start with e.g., 1, 2 and so on) :- "))
                                    if pid < 0:
                                        print("id must be positive integer.")
                                        continue
                                    break
                                Appointment.search_by_patient_id(Appointment,pid)
                            except Exception as e:
                                print(f"Something went wrong! Error: {e}")
                        else:
                            print("Input valid choice.")
                    elif choice == '4':
                        print("\n\t\tDOCTOR UPDATE APPOINTMENT WITH ADD  PRESCRIPTION BY TOKEN ID OF PATIENT.\n")
                        try:
                            while True:
                                try:
                                    pid=int(input("\nEnter the patient id (e.g., 1,2,3) for add prescription:- "))
                                    if pid<0:
                                        print("Patient id must be positive integer and strat from 1,2 so on.. ")
                                        continue
                                    sql="select * from patient where Token = {} ".format(pid)
                                    sql1="select * from appointment where pt_id = {} ".format(pid)
                                    cr.execute(sql) 
                                    rec=cr.fetchall()
                                    if len(rec)>0:
                                        cr.execute(sql1)
                                        rec=cr.fetchall()
                                        for i in rec:
                                            print(f"\nPatient Disease Systums: {i[3]} \n")
                                        while True:
                                            try:
                                                presc=input("Enter prescription for the patient: ")
                                                if not presc :
                                                    print("Add Prescription")
                                                    continue
                                                Appointment.update_appointment(Appointment,pid,presc)
                                                break
                                            except ValueError as ve:
                                                print(f"Invalid input! Please enter a valid pid for prescrition{ve}.")
                                    else:
                                        print(f"Token Id {pid} does not exist in the records.")  
                                        continue          
                                except ValueError as ve:
                                    print(f"Invalid Input! Please enter valid number for patient id {ve}")
                                break    
                        except ValueError as ve:
                            print(f"Something went wrong! {ve} ")
                    elif choice == "5":
                        print("\n\t\tDELETE APPOINTMENT RECORD OF PATIENT BY APPOINTMENT ID.\n")
                        try:
                            while True:
                                aid=int(input("\nEnter the appointment id (e.g., 1,2,3) of the patient appointment which record you want to delete :- "))
                                if aid<0:
                                    print("appointment id must be positive integer and start from 1,2 so on ")
                                    continue
                                Appointment.delete_appointment_rec(Appointment,aid)
                                break
                        except ValueError as ve:
                            print(f"Invalid Input! Please enter valid number for id. {ve}")
                    else:
                        print("Invalid input!, Please enter valid choice.")
                        continue
                    break
            else:
                print("Invalid input!, Please enter valid choice.")
                continue
            break
        continue_choice = input("Do you want to perform another task?(yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print('Exiting the system...')
            break

options()    



        
        


class Animal:
    def sound(self):
        pass  # Placeholder method, doesn't do anything yet

# Create an instance of Animal
animal = Animal()

# Calling the method doesn't do anything for now
animal.sound()



