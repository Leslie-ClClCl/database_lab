import mysql.connector
from tkinter import *


def addCourseInfo(databaseHandle: mysql.connector.connect, info, outputBox: Text):
    databaseCursor = databaseHandle.cursor()
    for i in info:
        print(i)
    sql = "INSERT INTO Course(Cno, Cname, Cpno, Ccredit) VALUES (%s, %s, %s, %s) "
    try:
        databaseCursor.execute(sql, info)
        outputBox.insert(END, "%d 条记录插入成功\n" % databaseCursor.rowcount)
        databaseHandle.commit()
        databaseCursor.execute("select * from Student")
    except mysql.connector.Error as error:
        outputBox.insert(END, "插入错误, 错误信息： %s\n" % error)
    databaseCursor.close()