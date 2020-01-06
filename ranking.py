import mysql.connector


def queryCourseByDept(databaseHandle: mysql.connector.connection, dept):
    sql = "SELECT DISTINCT Cname,SC.Cno FROM Course,Student,SC WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND Sdept=%s"
    databaseCursor = databaseHandle.cursor()
    databaseCursor.execute(sql, dept)
    info = databaseCursor.fetchall()
    return info


def ranking(databaseHandle: mysql.connector.connection, dept):
    sql1 = "SELECT Student.Sno,Sname, AVG(Grade) PG From Student, SC, Course \
        Where Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND Sdept=%s Group BY Student.Sno ORDER BY PG DESC"
    databaseCursor = databaseHandle.cursor()
    databaseCursor.execute(sql1,dept)
    info = databaseCursor.fetchall()
    for item in info:
        sql2 = "SELECT Cname, Grade"
    return info
    pass
