from glob import glob
import os;
import sqlite3;
import time;
import subprocess;
import threading;
from sqlite3 import Error
from subprocess import Popen

def UserExist(user_remark,DeviceConnection):
    user_data = [];
    V2U = GetV2rayUsers();
    for VU in V2U:
        if VU[1].lower() == user_remark.lower():
            user_data.append({'name':VU[1],'port':VU[2],'limit_user':DeviceConnection});
    if user_data:
        return user_data
    else:
        return False

def GetV2rayUsers():
    try:
        conn = sqlite3.connect(r"/etc/x-ui/x-ui.db")
        Lis = conn.execute(f"select id,remark,port from inbounds");
        return Lis
    except Error as e:
        print(e)

def GetInnerUsers():
    try:
        conn = sqlite3.connect(r"limiter.db")
        Lis = conn.execute(f"select * from limitation");
        return Lis.fetchall()
    except Error as e:
        print(e)

def create_inner__connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_inner_table(conn):
    sqlcreatetb = """ CREATE TABLE IF NOT EXISTS limitation (
                                        id integer PRIMARY KEY,
                                        name text,
                                        port text,
                                        limit_user text
                                    ); """
    try:
        c = conn.cursor()
        c.execute(sqlcreatetb)
    except Error as e:
        print(e)

def Execute_sqlcode(conn, sqlcode):
    try:
        c = conn.cursor()
        c.execute(sqlcode)
        conn.commit()
    except Error as e:
        print(e)

def is_Duplicate(conn, User_remark):
    try:
        Existence = conn.execute("select count(*) from limitation where name=\'%s\'" % User_remark ).fetchone();
        if Existence[0] > 0:
            return True
        else:
            return False
    except Error as e:
        print(e)

def User_Exist(conn, User_id):
    try:
        Existence = conn.execute("select count(*) from limitation where id=%s" % User_id).fetchone();
        if Existence[0] > 0:
            return True
        else:
            return False
    except Error as e:
        print(e)

def Delete_User(conn,User_id):
    try:
        if User_Exist(conn,User_id):
            if conn is None:
                print("Error! cannot create the database connection.")
                exit()
            else:
                sqlDeltu = f'DELETE FROM limitation where id={User_id}'
                Execute_sqlcode(conn, sqlDeltu)
    except Error as e:
        print(e)
def Inser_New_User(conn, Data_List):
    try:
        for all in Data_List:
            if is_Duplicate(conn,all['name'].lower()):
                print("Warning! User has been added before.")
                exit();
            sqlInsertu = 'INSERT INTO limitation (name,port,limit_user) VALUES(\"%s\",%s,%s)' % (all['name'].lower(),all['port'],all['limit_user'])
        if conn is None:
            print("Error! cannot create the database connection.")
        else:
            Execute_sqlcode(conn, sqlInsertu)
    except Error as e:
        print(e)

# def getSpecialUsers():
#     users_list = [];
#     u_remark = input("Enter V2Ray User Remark to limit connection: ");
#     if UserExist(u_remark):
#         u_limit_ = input("How many users can connect: ");
#         add_new_remarker = input("Wanna add new user (y/n): ");
#         users_list.append({'name':{UserExist['name']},'port':{UserExist['port']},'limitation':{u_limit_}});
#     else:
#         print({u_remark} + " doesn't exist...");
#     return users_list

def init():
    conn = create_inner__connection(r"limiter.db")
    if conn is None:
        print("Error! cannot create the database connection.")
    else:
        create_inner_table(conn)
    print("""
    Select One:
        1. Add New User to limit
        2. Delete User
        3. Show Limited User List
        4. Show V2RAY User List
        """);
    selectedItem = input("Please select from above: ");
    match selectedItem:
        case "1":
            entereduser = input("Please select V2ray User: ").lower();
            limitationUser = input("How many Devices can connect in the same time: ");
            if UserExist(entereduser, limitationUser):
                Inser_New_User(conn, UserExist(entereduser, limitationUser));
            else:
                print(entereduser," doesn't exists...");
                exit();
            os.system('nohup python3 main.py')
        case "2":
            for row in GetInnerUsers():
                print(row)
            selectedUser = input("Enter Index of User Listed above: ")
            Delete_User(conn,selectedUser)
        case "3":
            print('Total - Remark - Port')
            for row in GetInnerUsers():
                print(row)
        case "4":
            print('Total - Remark - Port')
            for row in GetV2rayUsers():
                print(row)
    
    
init();
