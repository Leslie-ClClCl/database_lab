import mysql.connector


def queryDept(databaseHandle: mysql.connector.connection):
    sql = "SELECT DISTINCT Sdept FROM Student"
    databaseCursor = databaseHandle.cursor()
    databaseCursor.execute(sql)
    temp = databaseCursor.fetchall()
    return temp


def gradeStatistics(databaseHandle, dept):
    databaseCursor = databaseHandle.cursor()
    sql1 = "SELECT SC.Cno, Cname, AVG(Grade), MAX(Grade), MIN(Grade) FROM Student, SC, Course\
        WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND Sdept=%s Group by SC.Cno ORDER BY SC.Cno"
    databaseCursor.execute(sql1, dept)
    info1 = list(databaseCursor.fetchall())
    infoTotal = []
    for courseNo in range(len(info1)):
        sql2 = "SELECT count(*)*100 FROM Student, SC, Course \
                WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND Sdept=%s \
                AND Grade>90 AND SC.Cno=%s"
        databaseCursor.execute(sql2, (dept[0], info1[courseNo][0], ))
        goodNum = databaseCursor.fetchall()[0][0]
        sql3 = "SELECT count(*) FROM Student, SC, Course \
                        WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND Sdept=%s \
                        AND Grade<60 AND SC.Cno=%s"
        databaseCursor.execute(sql3, (dept[0], info1[courseNo][0], ))
        badNum = databaseCursor.fetchall()[0][0]
        sql4 = "SELECT count(*) FROM Student, SC, Course \
                        WHERE Student.Sno=SC.Sno AND SC.Cno=Course.Cno AND Sdept=%s AND SC.Cno=%s"
        databaseCursor.execute(sql4, (dept[0], info1[courseNo][0], ))
        totalNum = databaseCursor.fetchall()[0][0]
        goodRate = goodNum / totalNum
        infoTotal.append(list(info1[courseNo]))
        infoTotal[courseNo].append(goodRate)
        infoTotal[courseNo].append(badNum)
    return infoTotal
