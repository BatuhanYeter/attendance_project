from msilib.schema import Error
import pyodbc
import os

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
        conn.commit()
        print(f'worker with id:{employer_id} has ben detected and saved.')
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
        os.remove(f'{path}/{photo_uuid[0]}.jpg')
        
        # print(photo_uuid[0])
        
        cursor.execute(
            'delete from Employers where id=?',
            (id)        
            )
        print(cursor.rowcount)
        cursor.commit()
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

def findAttendacesById():
    pass

def saveAsCsv():
    pass