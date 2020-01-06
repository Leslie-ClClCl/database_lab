import mysql.connector


def queryStudentBySno(Sno, databaseHandle):
    print(Sno)
    databaseCursor = databaseHandle.cursor()
    sql = "SELECT * FROM Student WHERE Sno = %s"
    databaseCursor.execute(sql, (Sno,))
    info = databaseCursor.fetchone()
    print(info)
    return info


def modifyStudentInfo(databaseHandle: mysql.connector.connect, info):
    print(info)
    databaseCursor = databaseHandle.cursor()
    oldInfo = queryStudentBySno(info[0], databaseHandle)
    var = ("Sname", "Ssex", "Sage", "Sdept", "Scholarship")
    modify = []
    for i in range(len(var)):
        sql = "UPDATE Student SET %s = %s WHERE Sno = %s" % (var[i],"%s","%s")
        if oldInfo[i+1] != info[i+1]:
            databaseCursor.execute(sql, (info[i + 1], info[0],))
            databaseHandle.commit()
            modify.append((oldInfo[i+1], info[i+1]))
    return modify
