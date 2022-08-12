import pyodbc

def connect():    
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=KAL-COR-17;"
        "Database=attendance;"
        "Trusted_Connection=yes;"
    )
    return conn

def create_user(lastName, firstName, age, tck, photo_uuid, email, phone_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'insert into Workers(LastName,FirstName,Age,TCK,PhotoId,Email,PhoneNumber) values(?,?,?,?,?,?,?);',
        (lastName,firstName,age,tck,photo_uuid,email,phone_number)
        ) 
    conn.commit()   

def save_entrance(worker_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'insert into Entrances(worker_id) values(?);',
        (worker_id)           
        )
    conn.commit()
    print(f'worker with id:{worker_id} has ben detected and saved.')
    
    
def find_workerId(photo_uuid):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'select * from Workers where PhotoId=?',
        (photo_uuid)           
        )
    worker = cursor.fetchone()
    print(worker[0])
    return worker[0]
    
    