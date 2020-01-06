import mysql.connector


def querySCBySnoCno(Sno, Cno, databaseHandle):
    databaseCursor = databaseHandle.cursor()
    sql = "SELECT Student.Sno, Student.Sname, Course.Cno, Course.Cname, Grade FROM Student,SC,Course WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND SC.Sno=%s AND SC.Cno=%s"
    databaseCursor.execute(sql, (Sno, Cno,))
    info = databaseCursor.fetchone()
    return info


def modifySCInfo(databaseHandle: mysql.connector.connect, info):
    print(info)
    databaseCursor = databaseHandle.cursor()
    sql = "UPDATE SC SET Grade = %s WHERE Sno = %s AND Cno = %s"
    databaseCursor.execute(sql, (info[2], info[0], info[1],))

