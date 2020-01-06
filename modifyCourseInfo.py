import mysql.connector


def queryCourseByCno(Cno, databaseHandle):
    print(Cno)
    databaseCursor = databaseHandle.cursor()
    sql = "SELECT * FROM Course WHERE Cno = %s"
    databaseCursor.execute(sql, (Cno,))
    info = databaseCursor.fetchone()
    print(info)
    return info


def modifyCourseInfo(databaseHandle: mysql.connector.connect, info):
    print(info)
    databaseCursor = databaseHandle.cursor()
    oldInfo = queryCourseByCno(info[0], databaseHandle)
    var = ("Cname", "Cpno", "Ccredit")
    modify = []
    for i in range(len(var)):
        sql = "UPDATE Course SET %s = %s WHERE Cno = %s" % (var[i],"%s","%s")
        if oldInfo[i+1] != info[i+1]:
            databaseCursor.execute(sql, (info[i + 1], info[0],))
            databaseHandle.commit()
            modify.append((oldInfo[i+1], info[i+1]))
    return modify
