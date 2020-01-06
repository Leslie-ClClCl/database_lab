import mysql.connector
from modifyStudentInfo import queryStudentBySno


def querySCBySno(Sno, databaseHandle):
    databaseCursor = databaseHandle.cursor()
    sql = "SELECT Student.Sno, Student.Sname, Course.Cno, Course.Cname, Grade \
        FROM Student,SC,Course WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND SC.Sno=%s"
    databaseCursor.execute(sql, (Sno,))
    info = databaseCursor.fetchall()
    print(info)
    return info


def queryStudentInfo(Sno, databaseHandle):
    info = [queryStudentBySno(Sno, databaseHandle), querySCBySno(Sno, databaseHandle)]
    return info
