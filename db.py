import csv
from msilib.schema import Error
import pyodbc
import os
import time

def connect():    
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=KAL-COR-17;"
        "Database=attendance;"
        "Trusted_Connection=yes;"
    )
    return conn

def create_user(lastName, firstName, age, tck, photo_uuid, email, phone_number, address_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into Employers(LastName,FirstName,Age,TCK,PhotoId,Email,PhoneNumber,AddressId) values(?,?,?,?,?,?,?,?);',
            (lastName,firstName,age,tck,photo_uuid,email,phone_number,address_id)
            ) 
        conn.commit()   
        return 1
    except pyodbc.Error as err:
        return err
    
def save_entrance(employer_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into Entrances(employer_id) values(?);',
            (employer_id)           
            )
        print(f'worker with id:{employer_id} has ben detected and saved.')
        conn.commit()
        time.sleep(2)
    except pyodbc.Error as err:
        return err
        
    
def find_employerId(photo_uuid):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'select * from Employers where PhotoId=?',
            (photo_uuid)           
            )
        employer = cursor.fetchone()
        print(employer[0])
        return employer[0]
    except pyodbc.Error as err:
        return err
    
def fetchAllEmployers():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'select id, LastName, FirstName, Age, TCK, PhoneNumber from Employers;'         
            )
        employers = cursor.fetchall()
        return employers
    except pyodbc.Error as err:
        return err
            
def deleteEmployerById(id):
    try:
        conn = connect()
        cursor = conn.cursor()
        
        cursor.execute(
            'select PhotoId from Employers where id=?',
            (id)
        )
        photo_uuid = cursor.fetchone()
        path = "./images"
        
        
        if os.path.exists(f'{path}/{photo_uuid[0]}.jpg'):
            os.remove(f'{path}/{photo_uuid[0]}.jpg')
            # cursor.execute(
            #     'delete from Entrances where employer_id=?',
            #     (id)
            # )
            # cursor.commit()
            cursor.execute(
            'delete from Employers where id=?',
            (id)        
            )
            cursor.commit()
            
            return 1
        else:
            return "Something went wrong: No image found."
    except pyodbc.Error as err:
        return err    

def getAddresses():
    try:
        conn = connect()
        cursor = conn.cursor()
        
        cursor.execute(
            'Select * From Addresses'
        )
        data = cursor.fetchall()
        return data
    except pyodbc.Error as err:
        return err
    
def getAddressIdByName(name):
    try:
        conn = connect()
        cursor = conn.cursor()
        
        cursor.execute(
            'Select id From Addresses where Name=?',
            (name)
        )
        id = cursor.fetchone()
        return id[0]
    except pyodbc.Error as err:
        return err
    
def findByAddressId(id):
    try:
        conn = connect()
        cursor = conn.cursor()
        
        cursor.execute(
            'EXEC GetTempTableByAdressId @AddressId=?',
            (id)
        )
        cursor.commit()
        data = cursor.fetchall()
        print(data)
        return data
    except pyodbc.Error as err:
        return err

def fetchAttendanceById(id):
    try:
        conn = connect()
        cursor = conn.cursor()
        
        cursor.execute(
            'Select * From Entrances Where employer_id=?',
            (id)
        )
        
        data = cursor.fetchall()
        return data
    except pyodbc.Error as err:
        return err
    
def saveAsCsv(data):
    f = open('./attendance.csv', 'w')
    writer = csv.writer(f)
    print(data)
    for row in data:
        writer.writerow(row)
    f.close()