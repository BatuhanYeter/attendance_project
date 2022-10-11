import csv
from msilib.schema import Error
import pyodbc
import os
import time


def connect():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=LAPTOP-M3NVAC69;"
        "Database=attendance;"
        "Trusted_Connection=yes;"
    )
    return conn


def create_user(lastName, firstName, age, tck, photo_uuid, email, phone_number, address_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into Workers(LastName,FirstName,Age,TCK,PhotoUrl,Email,PhoneNumber,AddressId) values(?,?,?,?,?,?,?,?);',
            (lastName, firstName, age, tck, photo_uuid,
             email, phone_number, address_id)
        )
        conn.commit()
        return 1
    except pyodbc.Error as err:
        return err


def save_entrance(worker_id):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into Entrances(worker_id) values(?);',
            (worker_id)
        )
        print(f'worker with id:{worker_id} has ben detected and saved.')
        conn.commit()
        time.sleep(3)
    except pyodbc.Error as err:
        return err


def find_workerId(photo_uuid):
    path = "./media/"
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'select * from Workers where PhotoUrl=?',
            (f'{path}/{photo_uuid}')
        )
        worker = cursor.fetchone()
        print(worker[0])
        return worker[0]
    except pyodbc.Error as err:
        return err


def fetchWorkerByPhotoId(photo_uuid):
    path = "images"
    print(photo_uuid)
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'select * from Workers where PhotoUrl=?',
            (f'{path}/{photo_uuid}.jpg')
        )

        worker = cursor.fetchone()
        print("Fetched worker: ", worker)
        return worker
    except pyodbc.Error as err:
        return err


def fetchAllWorkers():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'select id, LastName, FirstName, Age, TCK, PhoneNumber from Workers;'
        )
        workers = cursor.fetchall()
        return workers
    except pyodbc.Error as err:
        return err


def deleteWorkerById(id):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            'select PhotoUrl from Workers where id=?',
            (id)
        )
        photo_uuid = cursor.fetchone()
        path = "./media"

        if os.path.exists(f'{path}/{photo_uuid[0]}.jpg'):
            os.remove(f'{path}/{photo_uuid[0]}.jpg')

            cursor.execute(
                'delete from Workers where id=?',
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
            'Select * From Entrances Where worker_id=?',
            (id)
        )

        data = cursor.fetchall()
        return data
    except pyodbc.Error as err:
        return err


def saveAsCsv(data):
    f = open('./attendance.csv', 'w')
    writer = csv.writer(f)
    # print(data)
    for row in data:
        writer.writerow(row)
    f.close()
