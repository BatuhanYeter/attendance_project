import pyodbc

def connect():    
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=KAL-COR-17;"
        "Database=attendance;"
        "Trusted_Connection=yes;"
    )
    return conn

def create_user(lastName, firstName, age):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'insert into Workers(LastName,FirstName,Age) values(?,?,?);',
        (lastName,firstName,age)
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
    
    
def find_workerId(firstName, lastName):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'select * from Workers where lastName=? and firstName=?',
        (lastName, firstName)           
        )
    worker = cursor.fetchone()
    print(worker[0])
    return worker[0]
    
    