from tkinter import ttk
import tkinter.messagebox
from AddStudentInfo import *
from modifyStudentInfo import *
from addCourseInfo import *
from modifyCourseInfo import *
from addSCInfo import *
from modifySCInfo import *
from gradeStatistics import *
from queryStudentInfo import queryStudentInfo

import mysql.connector

from ranking import queryCourseByDept, ranking


def deptList(databaseHandle: mysql.connector.connect):
    pass


def addStudentInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doProcess():
        Sno = int(SnoBox.get())
        Sname = SnameBox.get()
        Ssex = SsexBox.get()
        Sage = int(SageBox.get())
        Sdept = SdeptBox.get()
        Scholarship = ScholarshipBox.get()
        print((Sno, Sname, Ssex, Sage, Sdept, Scholarship))
        if addStudentInfo(databaseHandle, (Sno, Sname, Ssex, Sage, Sdept, Scholarship), outputBox):
            print("success")

    top = Toplevel(root)
    top.title(funcName)
    titleFrame = Frame(top)
    titleLabel = Label(titleFrame, text=funcName, font=('黑体', '30'))
    infoFrame = Frame(top, bg='#ececec')
    SnoFrame = Frame(infoFrame, bg='#ececec')
    SnoLabel = Label(SnoFrame, text='学号', bg='#ececec')
    SnoBox = Entry(SnoFrame, width=15)
    SnameFrame = Frame(infoFrame, bg='#ececec')
    SnameLabel = Label(SnameFrame, text='姓名', bg='#ececec')
    SnameBox = Entry(SnameFrame, width=15)
    SsexFrame = Frame(infoFrame, bg='#ececec')
    SsexLabel = Label(SsexFrame, text='性别', bg='#ececec')
    var1 = StringVar()
    SsexBox = ttk.Combobox(SsexFrame, textvariable=var1, values=['男', '女', ], width=5)
    SageFrame = Frame(infoFrame, bg='#ececec')
    SageLabel = Label(SageFrame, text='年龄', bg='#ececec')
    SageBox = Entry(SageFrame, width=5)
    SdeptFrame = Frame(infoFrame, bg='#ececec')
    SdeptLabel = Label(SdeptFrame, text='系别', bg='#ececec')
    SdeptBox = Entry(SdeptFrame, width=8)
    ScholarshipFrame = Frame(infoFrame, bg='#ececec')
    ScholarshipLabel = Label(ScholarshipFrame, text='奖学金', bg='#ececec')
    var2 = StringVar()
    ScholarshipBox = ttk.Combobox(ScholarshipFrame, textvariable=var2, values=['是', '否', ], width=5)
    buttonFrame = Frame(top, bg='#ececec')
    uploadButton = ttk.Button(buttonFrame, text='新增', width=10, command=doProcess)
    exitButton = ttk.Button(buttonFrame, text='退出', width=10, command=closeThisWindow)
    outputFrame = Frame(top)
    outputBox = Text(outputFrame, width=100, bd=2, height=30, relief=RIDGE)

    titleFrame.pack(side='top', fill=X, padx=10)
    infoFrame.pack(side='top', fill=X, padx=5)
    buttonFrame.pack(side='top', fill=X, padx=5)
    outputFrame.pack(side='top', fill=X, padx=10)
    titleLabel.pack(side='top')
    SnoFrame.pack(side='left', ipadx=5, pady=10)
    SnoLabel.pack(side='top', ipadx=5, pady=10)
    SnoBox.pack(side='bottom', ipadx=5, pady=10)
    SnameFrame.pack(side='left', ipadx=5, pady=10)
    SnameLabel.pack(side='top', ipadx=5, pady=10)
    SnameBox.pack(side='bottom', ipadx=5, pady=10)
    SsexFrame.pack(side='left', ipadx=5, pady=10)
    SsexLabel.pack(side='top', ipadx=5, pady=10)
    SsexBox.pack(side='bottom', ipadx=5, pady=10)
    SageFrame.pack(side='left', ipadx=5, pady=10)
    SageLabel.pack(side='top', ipadx=5, pady=10)
    SageBox.pack(side='bottom', ipadx=5, pady=10)
    SdeptFrame.pack(side='left', ipadx=5, pady=10)
    SdeptLabel.pack(side='top', ipadx=5, pady=10)
    SdeptBox.pack(side='bottom', ipadx=5, pady=10)
    ScholarshipFrame.pack(side='left', ipadx=5, pady=10)
    ScholarshipLabel.pack(side='top', ipadx=5, pady=10)
    ScholarshipBox.pack(side='bottom', ipadx=5, pady=10)
    uploadButton.pack(side='left', padx=100, pady=10)
    exitButton.pack(side='right', padx=100, pady=10)

    outputBox.pack(side='top', padx=10, pady=10)

    # top.geometry('1000x750+30+30')
    top.mainloop()


def modifyStudentInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doQuery():
        try:
            Sno = int(queryBox.get())
            info = queryStudentBySno(Sno, databaseHandle)
            SnoBox.config(state=NORMAL)  # 将Sno输入框的状态设为有效，以便插入信息
            SnoBox.delete(0, END)
            SnoBox.insert(END, info[0])
            SnoBox.config(state='disabled')  # 将Sno输入框的状态设为无效，避免修改学号
            SnameBox.delete(0, END)
            SnameBox.insert(END, info[1])
            SsexBox.delete(0, END)
            SsexBox.insert(END, info[2])
            SageBox.delete(0, END)
            SageBox.insert(END, info[3])
            SdeptBox.delete(0, END)
            SdeptBox.insert(END, info[4])
            ScholarshipBox.delete(0, END)
            ScholarshipBox.insert(END, info[5])
            pass
        except mysql.connector.Error as error:
            outputBox.insert(END, "查询失败! %s\n" % error)
        except:
            outputBox.insert(END, "查询失败!\n")

    def doModify():
        try:
            Sno = int(SnoBox.get())
            Sname = SnameBox.get()
            Ssex = SsexBox.get()
            Sage = int(SageBox.get())
            Sdept = SdeptBox.get()
            Scholarship = ScholarshipBox.get()
            modify = modifyStudentInfo(databaseHandle, (Sno,Sname,Ssex,Sage,Sdept,Scholarship))
            modifyNum = len(modify)
            outputBox.insert(END, "恭喜你, 成功修改了 %d 项:\n" % modifyNum)
            for i in range(modifyNum):
                outputBox.insert(END, "    %s --> %s\n" % (modify[i][0],modify[i][1]))
        except mysql.connector.Error as error:
            outputBox.insert(END, "更新错误, 错误信息： %s\n" % error)
    top = Toplevel(root)
    top.title(funcName)

    titleFrame = Frame(top)
    titleFrame.pack(side='top', fill=X, padx=10)
    queryFrame = Frame(top)
    queryFrame.pack(side='top', fill=X, pady=10)
    modifyFrame = Frame(top)
    modifyFrame.pack(side='top', fill=X, pady=10, padx=10)
    outputFrame = Frame(top)
    outputFrame.pack(side='top', fill=X, padx=10)

    titleLabel = Label(titleFrame, text='修 改 学 生 信 息', font=('圆体-简', '30'), bg='#eaeaea')
    titleLabel.pack(side='top', fill=X, padx=10)
    queryLabelFrame = Frame(queryFrame)
    queryLabel = Label(queryLabelFrame, text='请输入学号:', font=('黑体', '15', 'bold'),bg='#efefef')
    querySubFrame = Frame(queryFrame, bg='#ececec')
    queryBox = Entry(querySubFrame)
    queryButton = ttk.Button(querySubFrame, text='查询', command=doQuery)
    exitButton = ttk.Button(querySubFrame, text='退出', command=closeThisWindow)
    queryLabelFrame.pack(side='top', fill=X, padx=10)
    queryLabel.pack(side='left', fill=X)
    querySubFrame.pack(side='top', fill=X, padx=10, ipady=10)
    queryBox.pack(side='left', fill=X, padx=10)
    exitButton.pack(side='right', padx=10)
    queryButton.pack(side='right', padx=10)

    modifyLabelFrame = Frame(modifyFrame)
    modifyLabel = Label(modifyLabelFrame, text='符合条件的信息:', bg='#efefef', font=('黑体', '15', 'bold'))
    modifysubFrame = Frame(modifyFrame, bg='#ececec')
    SnoFrame = Frame(modifysubFrame, bg='#ececec')
    SnoLabel = Label(SnoFrame, text='学号', bg='#ececec')
    SnoBox = Entry(SnoFrame, width=15, state='disabled')
    SnameFrame = Frame(modifysubFrame, bg='#ececec')
    SnameLabel = Label(SnameFrame, text='姓名', bg='#ececec')
    SnameBox = Entry(SnameFrame, width=15)
    SsexFrame = Frame(modifysubFrame, bg='#ececec')
    SsexLabel = Label(SsexFrame, text='性别', bg='#ececec')
    var1 = StringVar()
    SsexBox = ttk.Combobox(SsexFrame, textvariable=var1, values=['男', '女', ], width=5)
    SageFrame = Frame(modifysubFrame, bg='#ececec')
    SageLabel = Label(SageFrame, text='年龄', bg='#ececec')
    SageBox = Entry(SageFrame, width=5)
    SdeptFrame = Frame(modifysubFrame, bg='#ececec')
    SdeptLabel = Label(SdeptFrame, text='系别', bg='#ececec')
    SdeptBox = Entry(SdeptFrame, width=8)
    ScholarshipFrame = Frame(modifysubFrame, bg='#ececec')
    ScholarshipLabel = Label(ScholarshipFrame, text='奖学金', bg='#ececec')
    var2 = StringVar()
    ScholarshipBox = ttk.Combobox(ScholarshipFrame, textvariable=var2, values=['是', '否', ], width=5)
    modifyButtonFrame = Frame(modifyFrame, bg='#ececec')
    modifyButton = ttk.Button(modifyButtonFrame, text='修改', command=doModify)
    modifyLabelFrame.pack(side='top', fill=X)
    modifyLabel.pack(side='left', fill=X)
    modifysubFrame.pack(side='top', fill=X)
    SnoFrame.pack(side='left', ipadx=5, pady=10)
    SnoLabel.pack(side='top', ipadx=5, pady=3)
    SnoBox.pack(side='bottom', ipadx=5, pady=3)
    SnameFrame.pack(side='left', ipadx=5, pady=10)
    SnameLabel.pack(side='top', ipadx=5, pady=3)
    SnameBox.pack(side='bottom', ipadx=5, pady=3)
    SsexFrame.pack(side='left', ipadx=5, pady=10)
    SsexLabel.pack(side='top', ipadx=5, pady=3)
    SsexBox.pack(side='bottom', ipadx=5, pady=3)
    SageFrame.pack(side='left', ipadx=5, pady=10)
    SageLabel.pack(side='top', ipadx=5, pady=3)
    SageBox.pack(side='bottom', ipadx=5, pady=3)
    SdeptFrame.pack(side='left', ipadx=5, pady=10)
    SdeptLabel.pack(side='top', ipadx=5, pady=3)
    SdeptBox.pack(side='bottom', ipadx=5, pady=3)
    ScholarshipFrame.pack(side='left', ipadx=5, pady=10)
    ScholarshipLabel.pack(side='top', ipadx=5, pady=3)
    ScholarshipBox.pack(side='bottom', ipadx=5, pady=3)
    modifyButtonFrame.pack(side='top', fill=X)
    modifyButton.pack(side='right', fill=X, padx=10, pady=5)

    outputBox = Text(outputFrame, width=100, bd=2, height=30, relief=RIDGE)
    outputBox.pack(side='top', padx=10, pady=10)
    # top.geometry('1000x750+30+30')
    top.mainloop()

    pass


def addCourseInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doProcess():
        Cno = int(CnoBox.get())
        Cname = CnameBox.get()
        Cpno = int(CpnoBox.get())
        Ccredit = int(CcreditBox.get())
        if addCourseInfo(databaseHandle, (Cno, Cname, Cpno, Ccredit), outputBox):
            print("success")

    top = Toplevel(root)
    top.title(funcName)
    titleFrame = Frame(top)
    titleLabel = Label(titleFrame, text=funcName, font=('黑体', '30'))
    infoFrame = Frame(top, bg='#ececec')
    CnoFrame = Frame(infoFrame, bg='#ececec')
    CnoLabel = Label(CnoFrame, text='课程号', bg='#ececec')
    CnoBox = Entry(CnoFrame, width=5)
    CnameFrame = Frame(infoFrame, bg='#ececec')
    CnameLabel = Label(CnameFrame, text='课程名', bg='#ececec')
    CnameBox = Entry(CnameFrame, width=15)
    CpnoFrame = Frame(infoFrame, bg='#ececec')
    CpnoLabel = Label(CpnoFrame, text='先行课程号', bg='#ececec')
    CpnoBox = Entry(CpnoFrame, width=5)
    CcreditFrame = Frame(infoFrame, bg='#ececec')
    CcreditLabel = Label(CcreditFrame, text='学分', bg='#ececec')
    CcreditBox = Entry(CcreditFrame, width=5)
    buttonFrame = Frame(top, bg='#ececec')
    uploadButton = ttk.Button(buttonFrame, text='新增', width=10, command=doProcess)
    exitButton = ttk.Button(buttonFrame, text='退出', width=10, command=closeThisWindow)
    outputFrame = Frame(top)
    outputBox = Text(outputFrame, width=50, bd=2, height=15, relief=RIDGE)

    titleFrame.pack(side='top', fill=X, padx=10)
    infoFrame.pack(side='top', fill=X, padx=5)
    buttonFrame.pack(side='top', fill=X, padx=5)
    outputFrame.pack(side='top', fill=X, padx=10)
    titleLabel.pack(side='top')
    CnoFrame.pack(side='left', ipadx=5, pady=10)
    CnoLabel.pack(side='top', ipadx=5, pady=10)
    CnoBox.pack(side='bottom', ipadx=5, pady=10)
    CnameFrame.pack(side='left', ipadx=5, pady=10)
    CnameLabel.pack(side='top', ipadx=5, pady=10)
    CnameBox.pack(side='bottom', ipadx=5, pady=10)
    CpnoFrame.pack(side='left', ipadx=5, pady=10)
    CpnoLabel.pack(side='top', ipadx=5, pady=10)
    CpnoBox.pack(side='bottom', ipadx=5, pady=10)
    CcreditFrame.pack(side='left', ipadx=5, pady=10)
    CcreditLabel.pack(side='top', ipadx=5, pady=10)
    CcreditBox.pack(side='bottom', ipadx=5, pady=10)
    uploadButton.pack(side='left', padx=70, pady=10)
    exitButton.pack(side='right', padx=70, pady=10)
    outputBox.pack(side='top', padx=0, pady=10)

    # top.geometry('1000x750+30+30')
    top.mainloop()


def modifyCourseInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doQuery():
        try:
            Cno = int(queryBox.get())
            info = queryCourseByCno(Cno, databaseHandle)
            CnoBox.config(state=NORMAL)  # 将Sno输入框的状态设为有效，以便插入信息
            CnoBox.delete(0, END)
            CnoBox.insert(END, info[0])
            CnoBox.config(state='disabled')  # 将Sno输入框的状态设为无效，避免修改学号
            CnameBox.delete(0, END)
            CnameBox.insert(END, info[1])
            CpnoBox.delete(0, END)
            CpnoBox.insert(END, info[2])
            CcreditBox.delete(0, END)
            CcreditBox.insert(END, info[3])
        except mysql.connector.Error as error:
            outputBox.insert(END, "查询失败! %s\n" % error)
        except TypeError:
            outputBox.insert(END, "未找到相关信息! \n")

    def doModify():
        try:
            Cno = CnoBox.get()
            Cname = CnameBox.get()
            Cpno = CpnoBox.get()
            Ccredit = int(CcreditBox.get())
            modify = modifyCourseInfo(databaseHandle, (Cno, Cname, Cpno, Ccredit))
            modifyNum = len(modify)
            outputBox.insert(END, "恭喜你, 成功修改了 %d 项:\n" % modifyNum)
            for i in range(modifyNum):
                outputBox.insert(END, "    %s --> %s\n" % (modify[i][0],modify[i][1]))
        except mysql.connector.Error as error:
            outputBox.insert(END, "更新错误, 错误信息： %s\n" % error)
    top = Toplevel(root)
    top.title(funcName)

    titleFrame = Frame(top)
    titleFrame.pack(side='top', fill=X, padx=10)
    queryFrame = Frame(top)
    queryFrame.pack(side='top', fill=X, padx=10)
    modifyFrame = Frame(top)
    modifyFrame.pack(side='top', fill=X, padx=10)
    outputFrame = Frame(top)
    outputFrame.pack(side='top', fill=X, padx=10)

    titleLabel = Label(titleFrame, text=funcName, font=('黑体', '30'))
    titleLabel.pack(side='top', fill=X, padx=10)

    queryLabel = Label(queryFrame, text='请输入课程号:')
    querySubFrame = Frame(queryFrame)
    queryBox = Entry(querySubFrame)
    queryButton = Button(querySubFrame, text='查询', command=doQuery)
    exitButton = Button(querySubFrame, text='退出', command=closeThisWindow)
    queryLabel.pack(side='top', fill=X, padx=10)
    querySubFrame.pack(side='top', fill=X, padx=10)
    queryBox.pack(side='left', fill=X, padx=10)
    exitButton.pack(side='right', padx=10)
    queryButton.pack(side='right', padx=10)

    modifyLabel = Label(modifyFrame, text='符合条件的信息')
    modifysubFrame = Frame(modifyFrame)
    CnoFrame = Frame(modifysubFrame, bg='#ececec')
    CnoLabel = Label(CnoFrame, text='课程号', bg='#ececec')
    CnoBox = Entry(CnoFrame, width=15, state='disabled')
    CnameFrame = Frame(modifysubFrame, bg='#ececec')
    CnameLabel = Label(CnameFrame, text='课程名', bg='#ececec')
    CnameBox = Entry(CnameFrame, width=15)
    CpnoFrame = Frame(modifysubFrame, bg='#ececec')
    CpnoLabel = Label(CpnoFrame, text='先行课程号', bg='#ececec')
    CpnoBox = Entry(CpnoFrame, width=5)
    CcreditFrame = Frame(modifysubFrame, bg='#ececec')
    CcreditLabel = Label(CcreditFrame, text='学分', bg='#ececec')
    CcreditBox = Entry(CcreditFrame, width=8)
    modifyButtonFrame = Frame(modifyFrame)
    modifyButton = Button(modifyButtonFrame, text='修改', command=doModify)
    modifyLabel.pack(side='left', fill=X, padx=10)
    modifysubFrame.pack(side='top', fill=X, padx=10)
    CnoFrame.pack(side='left', ipadx=5, pady=10)
    CnoLabel.pack(side='top', ipadx=5, pady=10)
    CnoBox.pack(side='bottom', ipadx=5, pady=10)
    CnameFrame.pack(side='left', ipadx=5, pady=10)
    CnameLabel.pack(side='top', ipadx=5, pady=10)
    CnameBox.pack(side='bottom', ipadx=5, pady=10)
    CpnoFrame.pack(side='left', ipadx=5, pady=10)
    CpnoLabel.pack(side='top', ipadx=5, pady=10)
    CpnoBox.pack(side='bottom', ipadx=5, pady=10)
    CcreditFrame.pack(side='left', ipadx=5, pady=10)
    CcreditLabel.pack(side='top', ipadx=5, pady=10)
    CcreditBox.pack(side='bottom', ipadx=5, pady=10)
    modifyButtonFrame.pack(side='top', fill=X, padx=10)
    modifyButton.pack(side='right', fill=X, padx=10)

    outputBox = Text(outputFrame, width=100, bd=2, height=30, relief=RIDGE)
    outputBox.pack(side='top', padx=10, pady=10)
    # top.geometry('1000x750+30+30')
    top.mainloop()


def addSCInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doProcess():
        Sno = int(SnoBox.get())
        Cno = CnoBox.get()
        Grade = int(GradeBox.get())
        if addSCInfo(databaseHandle, (Sno, Cno, Grade), outputBox):
            print("success")

    top = Toplevel(root)
    top.title(funcName)
    titleFrame = Frame(top)
    titleLabel = Label(titleFrame, text=funcName, font=('黑体', '30'))
    infoFrame = Frame(top, bg='#ececec')
    SnoFrame = Frame(infoFrame, bg='#ececec')
    SnoLabel = Label(SnoFrame, text='学号', bg='#ececec')
    SnoBox = Entry(SnoFrame, width=15)
    CnoFrame = Frame(infoFrame, bg='#ececec')
    CnoLabel = Label(CnoFrame, text='课程号', bg='#ececec')
    CnoBox = Entry(CnoFrame, width=5)
    GradeFrame = Frame(infoFrame, bg='#ececec')
    GradeLabel = Label(GradeFrame, text='课程成绩', bg='#ececec')
    GradeBox = Entry(GradeFrame, width=10)
    buttonFrame = Frame(top, bg='#ececec')
    uploadButton = ttk.Button(buttonFrame, text='新增', width=10, command=doProcess)
    exitButton = ttk.Button(buttonFrame, text='退出', width=10, command=closeThisWindow)
    outputFrame = Frame(top)
    outputBox = Text(outputFrame, width=50, bd=2, height=15, relief=RIDGE)

    titleFrame.pack(side='top', fill=X, padx=10)
    infoFrame.pack(side='top', fill=X, padx=5, ipadx=10)
    buttonFrame.pack(side='top', fill=X, padx=5)
    outputFrame.pack(side='top', fill=X, padx=10)
    titleLabel.pack(side='top')
    SnoFrame.pack(side='left', ipadx=5, pady=10, padx=5)
    SnoLabel.pack(side='top', ipadx=5, pady=5)
    SnoBox.pack(side='bottom', ipadx=5, pady=5)
    CnoFrame.pack(side='left', ipadx=5, pady=10, padx=5)
    CnoLabel.pack(side='top', ipadx=5, pady=5)
    CnoBox.pack(side='bottom', ipadx=5, pady=5)
    GradeFrame.pack(side='left', ipadx=5, pady=10, padx=5)
    GradeLabel.pack(side='top', ipadx=5, pady=5)
    GradeBox.pack(side='bottom', ipadx=5, pady=5)
    uploadButton.pack(side='left', padx=50, pady=10)
    exitButton.pack(side='right', padx=50, pady=10)
    outputBox.pack(side='top', padx=0, pady=10)

    # top.geometry('1000x750+30+30')
    top.mainloop()


def modifySCInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doQuery():
        try:
            Sno = int(querySnoBox.get())
            Cno = queryCnoBox.get()
            info = querySCBySnoCno(Sno, Cno, databaseHandle)
            SnoBox.config(state=NORMAL)  # 将Sno输入框的状态设为有效，以便插入信息
            SnoBox.delete(0, END)
            SnoBox.insert(END, info[0])
            SnoBox.config(state='disabled')  # 将Sno输入框的状态设为无效，避免修改学号
            SnameBox.config(state=NORMAL)  # 将Sname输入框的状态设为有效，以便插入信息
            SnameBox.delete(0, END)
            SnameBox.insert(END, info[1])
            SnameBox.config(state='disabled')  # 将Sname输入框的状态设为无效，避免修改姓名
            CnoBox.config(state=NORMAL)  # 将Cno输入框的状态设为有效，以便插入信息
            CnoBox.delete(0, END)
            CnoBox.insert(END, info[2])
            CnoBox.config(state='disabled')  # 将Cno输入框的状态设为无效，避免修改课程号
            CnameBox.config(state=NORMAL)  # 将Cname输入框的状态设为有效，以便插入信息
            CnameBox.delete(0, END)
            CnameBox.insert(END, info[3])
            CnameBox.config(state='disabled')  # 将Cname输入框的状态设为无效，避免修改学号
            GradeBox.delete(0, END)
            GradeBox.insert(END, info[4])
            pass
        except mysql.connector.Error as error:
            outputBox.insert(END, "查询失败! %s\n" % error)
        except TypeError:
            outputBox.insert(END, "未查询到相关选课信息!\n")

    def doModify():
        try:
            Sno = SnoBox.get()
            Cno = CnoBox.get()
            Grade = GradeBox.get()
            modifySCInfo(databaseHandle, (Sno, Cno, Grade))
            outputBox.insert(END, "成绩已经被修改！\n")
        except mysql.connector.Error as error:
            outputBox.insert(END, "更新错误, 错误信息： %s\n" % error)
    top = Toplevel(root)
    top.title(funcName)

    titleFrame = Frame(top)
    titleFrame.pack(side='top', fill=X, padx=10)
    queryFrame = Frame(top)
    queryFrame.pack(side='top', fill=X, pady=10)
    modifyFrame = Frame(top)
    modifyFrame.pack(side='top', fill=X, pady=10, padx=10)
    outputFrame = Frame(top)
    outputFrame.pack(side='top', fill=X, padx=10)

    titleLabel = Label(titleFrame, text=funcName, font=('黑体', '30'), bg='#eaeaea')
    titleLabel.pack(side='top', fill=X, padx=10)
    queryLabelFrame = Frame(queryFrame)
    queryInfoFrame = Frame(queryFrame, bg='#ececec')
    queryLabel = Label(queryLabelFrame, text='请输入查询信息:', font=('黑体', '15', 'bold'),bg='#efefef')
    querySnoFrame = Frame(queryInfoFrame, bg='#ececec')
    querySnoLabel = Label(querySnoFrame, bg='#ececec', text='学号')
    querySnoBox = Entry(querySnoFrame)

    queryCnoFrame = Frame(queryInfoFrame, bg='#ececec')
    queryCnoLabel = Label(queryCnoFrame, bg='#ececec', text='课程号')
    queryCnoBox = Entry(queryCnoFrame)

    queryButton = ttk.Button(queryInfoFrame, text='查询', command=doQuery)
    exitButton = ttk.Button(queryInfoFrame, text='退出', command=closeThisWindow)
    queryLabelFrame.pack(side='top', fill=X, padx=10)
    queryLabel.pack(side='left', fill=X)
    queryInfoFrame.pack(side='top', fill=X, padx=10)
    querySnoFrame.pack(side='left', fill=X, padx=10, ipady=10)
    querySnoLabel.pack(side='top', fill=X, padx=10)
    querySnoBox.pack(side='top', fill=X, padx=10)
    queryCnoFrame.pack(side='left',fill=X, padx=10, ipady=10)
    queryCnoLabel.pack(side='top', fill=X, padx=10)
    queryCnoBox.pack(side='top', fill=X, padx=10)
    exitButton.pack(side='right', padx=10)
    queryButton.pack(side='right', padx=10)

    modifyLabelFrame = Frame(modifyFrame)
    modifyLabel = Label(modifyLabelFrame, text='符合条件的信息:', bg='#efefef', font=('黑体', '15', 'bold'))
    modifysubFrame = Frame(modifyFrame, bg='#ececec')

    SnoFrame = Frame(modifysubFrame, bg='#ececec')
    SnoLabel = Label(SnoFrame, text='学号', bg='#ececec')
    SnoBox = Entry(SnoFrame, width=15, state='disabled')

    SnameFrame = Frame(modifysubFrame, bg='#ececec')
    SnameLabel = Label(SnameFrame, text='姓名', bg='#ececec')
    SnameBox = Entry(SnameFrame, width=15, state='disabled')

    CnoFrame = Frame(modifysubFrame, bg='#ececec')
    CnoLabel = Label(CnoFrame, text='课程号', bg='#ececec')
    CnoBox = Entry(CnoFrame, width=8, state='disabled')

    CnameFrame = Frame(modifysubFrame, bg='#ececec')
    CnameLabel = Label(CnameFrame, text='课程名', bg='#ececec')
    CnameBox = Entry(CnameFrame, width=8, state='disabled')

    GradeFrame = Frame(modifysubFrame, bg='#ececec')
    GradeLabel = Label(GradeFrame, text='课程成绩', bg='#ececec')
    GradeBox = Entry(GradeFrame, width=8)

    modifyButtonFrame = Frame(modifyFrame, bg='#ececec')
    modifyButton = ttk.Button(modifyButtonFrame, text='修改', command=doModify)
    modifyLabelFrame.pack(side='top', fill=X)
    modifyLabel.pack(side='left', fill=X)
    modifysubFrame.pack(side='top', fill=X)

    SnoFrame.pack(side='left', ipadx=5, pady=10)
    SnoLabel.pack(side='top', ipadx=5, pady=3)
    SnoBox.pack(side='bottom', ipadx=5, pady=3)
    SnameFrame.pack(side='left', ipadx=5, pady=10)
    SnameLabel.pack(side='top', ipadx=5, pady=3)
    SnameBox.pack(side='bottom', ipadx=5, pady=3)
    CnoFrame.pack(side='left', ipadx=5, pady=10)
    CnoLabel.pack(side='top', ipadx=5, pady=3)
    CnoBox.pack(side='bottom', ipadx=5, pady=3)
    CnameFrame.pack(side='left', ipadx=5, pady=10)
    CnameLabel.pack(side='top', ipadx=5, pady=3)
    CnameBox.pack(side='bottom', ipadx=5, pady=3)
    GradeFrame.pack(side='left', ipadx=5, pady=10)
    GradeLabel.pack(side='top', ipadx=5, pady=3)
    GradeBox.pack(side='bottom', ipadx=5, pady=3)
    modifyButtonFrame.pack(side='top', fill=X)
    modifyButton.pack(side='right', fill=X, padx=10, pady=5)

    outputBox = Text(outputFrame, width=100, bd=2, height=30, relief=RIDGE)
    outputBox.pack(side='top', padx=10, pady=10)
    # top.geometry('1000x750+30+30')
    top.mainloop()


def gradeStatisticsUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    top = Toplevel(root)
    top.title("统计信息")
    titleFrame = Frame(top)
    titleLabel = Label(titleFrame, text="统 计 信 息", font=('圆体-简', '30'))
    titleFrame.pack(side='top', fill=X, padx=10)
    titleLabel.pack(side='top', fill=X, padx=10)

    color = ("#ececec", "#ffffff",)

    deptInfo = queryDept(databaseHandle)
    for dept in deptInfo:
        deptFrame = Frame(top)
        deptLabelFrame = Frame(deptFrame)
        deptLabel = Label(deptLabelFrame, text=dept[0], font=('圆体-简', '20'))
        leftLabel = Label(deptLabelFrame, text="~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~", font=('圆体-简', '20'))
        rightLabel = Label(deptLabelFrame, text="~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~", font=('圆体-简', '20'))
        deptFrame.pack(side='top', padx=10, pady=20)
        deptLabelFrame.pack(side='top', fill=X, padx=10)
        leftLabel.pack(side='left', padx=20, pady=20)
        deptLabel.pack(side='left', fill=X, padx=20)
        rightLabel.pack(side='left', padx=20, pady=20)
        infoTableFrame = Frame(deptFrame)
        infoTableFrame.pack(side='top', fill=X, padx=10)
        headFrame = Frame(infoTableFrame)
        headFrame.pack(side='top', padx=10)
        CnoHeadLabel = Label(headFrame, text='课程号', width=10)
        CnoHeadLabel.pack(side='left', padx=10)
        CnameHeadLabel = Label(headFrame, text='课程名', width=10)
        CnameHeadLabel.pack(side='left', padx=10)
        avgGradeHeadLabel = Label(headFrame, text='平均分', width=10)
        avgGradeHeadLabel.pack(side='left', padx=10)
        maxGradeHeadLabel = Label(headFrame, text='最高分', width=10)
        maxGradeHeadLabel.pack(side='left', padx=10)
        minGradeHeadLabel = Label(headFrame, text='最低分', width=10)
        minGradeHeadLabel.pack(side='left', padx=10)
        goodRateHeadLabel = Label(headFrame, text='优秀率', width=10)
        goodRateHeadLabel.pack(side='left', padx=10)
        badRateHeadLabel = Label(headFrame, text='不及格人数', width=10)
        badRateHeadLabel.pack(side='left', padx=10)

        infoByDept = gradeStatistics(databaseHandle, dept)
        count = 0;
        for course in infoByDept:
            print(course)
            infoRowFrame = Frame(deptFrame, bg=color[count % 2])
            infoRowFrame.pack(side='top', fill=X, padx=10)
            CnoLabel = Label(infoRowFrame, text=course[0], width=10, bg=color[count % 2])
            CnoLabel.pack(side='left', padx=10)
            CnameLabel = Label(infoRowFrame, text=course[1], width=10, bg=color[count % 2])
            CnameLabel.pack(side='left', padx=10)
            avgGradeLabel = Label(infoRowFrame, text=course[2], width=10, bg=color[count % 2])
            avgGradeLabel.pack(side='left', padx=10)
            maxGradeLabel = Label(infoRowFrame, text=course[3], width=10, bg=color[count % 2])
            maxGradeLabel.pack(side='left', padx=10)
            minGradeLabel = Label(infoRowFrame, text=course[4], width=10, bg=color[count % 2])
            minGradeLabel.pack(side='left', padx=10)
            goodRateLabel = Label(infoRowFrame, text="%.1f %%" % course[5], width=10, bg=color[count % 2])
            goodRateLabel.pack(side='left', padx=10)
            badRateLabel = Label(infoRowFrame, text="%d" % course[6], width=10, bg=color[count % 2])
            badRateLabel.pack(side='left', padx=10)
            count += 1
    exitButtonFrame = Frame(top)
    exitButton = Button(exitButtonFrame, text='关闭', command=closeThisWindow)
    exitButtonFrame.pack(side='top', fill=X, padx=10)
    exitButton.pack(side='top', fill=X, padx=10)
    top.mainloop()


def queryStudentInfoUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    def doQuery():
        try:
            Sno = int(queryBox.get())
            outputFrame.pack_forget()
            for item in SCCnoBox:
                item.pack_forget()
            SCCnoBox.clear()
            for item in SCCnameBox:
                item.pack_forget()
            SCCnameBox.clear()
            for item in SCGradeBox:
                item.pack_forget()
            SCGradeBox.clear()
            info = queryStudentInfo(Sno, databaseHandle)
            output(info)
        except mysql.connector.Error as error:
            print("查询失败! %s\n" % error)

    def output(info):

        baseInfoSet = info[0]
        SnoBox.config(text=baseInfoSet[0])
        SnameBox.config(text=baseInfoSet[1])
        SsexBox.config(text=baseInfoSet[2])
        SageBox.config(text=baseInfoSet[3])
        SdeptBox.config(text=baseInfoSet[4])
        ScholarshipBox.config(text=baseInfoSet[5])

        SCInfoSet = info[1]
        for SCNo in range(len(SCInfoSet)):
            SCCnoBox.append(Label(SCCnoFrame, text=SCInfoSet[SCNo][2]))
            SCCnoBox[SCNo].pack(side='top', fill=X, padx=10)
            SCCnameBox.append(Label(SCCnameFrame, text=SCInfoSet[SCNo][3]))
            SCCnameBox[SCNo].pack(side='top', fill=X, padx=10)
            SCGradeBox.append(Label(SCGradeFrame, text=SCInfoSet[SCNo][4]))
            SCGradeBox[SCNo].pack(side='top', fill=X, padx=10)
        outputFrame.pack(side='top', fill=X, padx=10)


    top = Toplevel(root)
    top.title("查询学生信息")

    titleFrame = Frame(top)
    titleFrame.pack(side='top', fill=X, padx=10)
    queryFrame = Frame(top)
    queryFrame.pack(side='top', fill=X, pady=10)
    modifyFrame = Frame(top)
    modifyFrame.pack(side='top', fill=X, pady=10, padx=10)
    outputFrame = Frame(top)

    titleLabel = Label(titleFrame, text='查 询 学 生 信 息', font=('圆体-简', '30'), bg='#eaeaea')
    titleLabel.pack(side='top', fill=X, padx=10)
    queryLabelFrame = Frame(queryFrame)
    queryLabel = Label(queryLabelFrame, text='请输入学号:', font=('黑体', '15', 'bold'), bg='#efefef')
    querySubFrame = Frame(queryFrame, bg='#ececec')
    queryBox = Entry(querySubFrame)
    queryButton = ttk.Button(querySubFrame, text='查询', command=doQuery)
    exitButton = ttk.Button(querySubFrame, text='退出', command=closeThisWindow)
    queryLabelFrame.pack(side='top', fill=X, padx=10)
    queryLabel.pack(side='left', fill=X)
    querySubFrame.pack(side='top', fill=X, padx=10, ipady=10)
    queryBox.pack(side='left', fill=X, padx=10)
    exitButton.pack(side='right', padx=10)
    queryButton.pack(side='right', padx=10)

    baseInfoFrame = Frame(outputFrame)
    baseInfoFrame.pack(side='top', ipadx=5, pady=3)
    baseInfoLabel = Label(baseInfoFrame, text='学生基础信息')
    baseInfoLabel.pack(side='top', ipadx=5, pady=3)
    SnoFrame = Frame(baseInfoFrame, bg='#ececec')
    SnoLabel = Label(SnoFrame, text='学号', bg='#ececec')
    SnoBox = Label(SnoFrame, width=12)
    SnameFrame = Frame(baseInfoFrame, bg='#ececec')
    SnameLabel = Label(SnameFrame, text='姓名', bg='#ececec')
    SnameBox = Label(SnameFrame, width=10)
    SsexFrame = Frame(baseInfoFrame, bg='#ececec')
    SsexLabel = Label(SsexFrame, text='性别', bg='#ececec')
    SsexBox = Label(SsexFrame, width=5)
    SageFrame = Frame(baseInfoFrame, bg='#ececec')
    SageLabel = Label(SageFrame, text='年龄', bg='#ececec')
    SageBox = Label(SageFrame, width=5)
    SdeptFrame = Frame(baseInfoFrame, bg='#ececec')
    SdeptLabel = Label(SdeptFrame, text='系别', bg='#ececec')
    SdeptBox = Label(SdeptFrame, width=5)
    ScholarshipFrame = Frame(baseInfoFrame, bg='#ececec')
    ScholarshipLabel = Label(ScholarshipFrame, text='奖学金', bg='#ececec')
    ScholarshipBox = Label(ScholarshipFrame, width=5)
    SnoFrame.pack(side='left', ipadx=5, pady=10)
    SnoLabel.pack(side='top', ipadx=5, pady=3)
    SnoBox.pack(side='bottom', ipadx=5, pady=3)
    SnameFrame.pack(side='left', ipadx=5, pady=10)
    SnameLabel.pack(side='top', ipadx=5, pady=3)
    SnameBox.pack(side='bottom', ipadx=5, pady=3)
    SsexFrame.pack(side='left', ipadx=5, pady=10)
    SsexLabel.pack(side='top', ipadx=5, pady=3)
    SsexBox.pack(side='bottom', ipadx=5, pady=3)
    SageFrame.pack(side='left', ipadx=5, pady=10)
    SageLabel.pack(side='top', ipadx=5, pady=3)
    SageBox.pack(side='bottom', ipadx=5, pady=3)
    SdeptFrame.pack(side='left', ipadx=5, pady=10)
    SdeptLabel.pack(side='top', ipadx=5, pady=3)
    SdeptBox.pack(side='bottom', ipadx=5, pady=3)
    ScholarshipFrame.pack(side='left', ipadx=5, pady=10)
    ScholarshipLabel.pack(side='top', ipadx=5, pady=3)
    ScholarshipBox.pack(side='bottom', ipadx=5, pady=3)

    SCInfoFrame = Frame(outputFrame)
    SCInfoLabel = Label(SCInfoFrame, text='学生选课信息')

    SCCnoFrame = Frame(SCInfoFrame, bg='#ececec')
    SCCnoLabel = Label(SCCnoFrame, text='课程号', bg='#ececec', width=5)
    SCCnoBox = []

    SCCnameFrame = Frame(SCInfoFrame, bg='#ececec')
    SCCnameLabel = Label(SCCnameFrame, text='课 程 名', bg='#ececec', width=15)
    SCCnameBox = []

    SCGradeFrame = Frame(SCInfoFrame, bg='#ececec')
    SCGradeLabel = Label(SCGradeFrame, text='课程成绩', bg='#ececec', width=8)
    SCGradeBox = []

    SCInfoFrame.pack(side='top', ipadx=5, pady=3)
    SCInfoLabel.pack(side='top', ipadx=5, pady=3)

    SCCnoFrame.pack(side='left', pady=10,ipady=3)
    SCCnoLabel.pack(side='top', pady=3)
    SCCnameFrame.pack(side='left', pady=10,ipady=3)
    SCCnameLabel.pack(side='top', pady=3)
    SCGradeFrame.pack(side='left', pady=10,ipady=3)
    SCGradeLabel.pack(side='top', pady=3)


    top.mainloop()


def rankUI(root, funcName, databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        top.destroy()

    top = Toplevel(root)
    top.title("统计信息")
    titleFrame = Frame(top)
    titleLabel = Label(titleFrame, text="成 绩 排 名", font=('圆体-简', '30'))
    titleFrame.pack(side='top', fill=X, padx=10)
    titleLabel.pack(side='top', fill=X, padx=10)

    color = ("#ffffff", "#ececec")

    deptInfo = queryDept(databaseHandle)
    for dept in deptInfo:
        deptFrame = Frame(top)
        deptLabelFrame = Frame(deptFrame)
        deptLabel = Label(deptLabelFrame, text=dept[0], font=('圆体-简', '20'))
        leftLabel = Label(deptLabelFrame, text="~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ", font=('圆体-简', '20'))
        rightLabel = Label(deptLabelFrame, text="~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ", font=('圆体-简', '20'))
        deptFrame.pack(side='top', padx=10, pady=20)
        deptLabelFrame.pack(side='top', fill=X, padx=10)
        leftLabel.pack(side='left', padx=20, pady=20)
        deptLabel.pack(side='left', fill=X, padx=20)
        rightLabel.pack(side='left', padx=20, pady=20)
        infoTableFrame = Frame(deptFrame)
        infoTableFrame.pack(side='top', fill=X, padx=10)
        headFrame = Frame(infoTableFrame)
        headFrame.pack(side='top', padx=10)
        SnoHeadLabel = Label(headFrame, text='学号', width=10)
        SnoHeadLabel.pack(side='left', padx=10)
        SnameHeadLabel = Label(headFrame, text='姓名', width=10)
        SnameHeadLabel.pack(side='left', padx=10)
        avgGradeHeadLabel = Label(headFrame, text='平均分', width=10)
        avgGradeHeadLabel.pack(side='left', padx=10)
        rankHeadLabel = Label(headFrame, text='名次', width=10)
        rankHeadLabel.pack(side='left', padx=10)

        courseInfo = queryCourseByDept(databaseHandle, dept)
        for course in courseInfo:
            courseHeadLabel = Label(headFrame, text=course[0], width=10)
            courseHeadLabel.pack(side='left', padx=10)

        infoByDept = ranking(databaseHandle, dept)
        count = 1;

        for course in infoByDept:
            infoRowFrame = Frame(deptFrame, bg=color[count % 2])
            infoRowFrame.pack(side='top', fill=X, padx=10)
            SnoLabel = Label(infoRowFrame, text=course[0], width=10, bg=color[count % 2])
            SnoLabel.pack(side='left', padx=10)
            SnameLabel = Label(infoRowFrame, text=course[1], width=10, bg=color[count % 2])
            SnameLabel.pack(side='left', padx=10)
            avgGradeLabel = Label(infoRowFrame, text=course[2], width=10, bg=color[count % 2])
            avgGradeLabel.pack(side='left', padx=10)
            rankLabel = Label(infoRowFrame, text=count, width=10, bg=color[count % 2])
            rankLabel.pack(side='left', padx=10)
            for i in range(len(courseInfo)):
                scInfo = querySCBySnoCno(course[0], courseInfo[i][1], databaseHandle)
                print(scInfo)
                gradeLabel = Label(infoRowFrame, bg=color[count % 2], width=10)
                gradeLabel.pack(side='left', padx=10)
                try:
                    gradeLabel.config(text=scInfo[4])
                except:
                    gradeLabel.config(text='无成绩')
            count += 1
    exitButtonFrame = Frame(top)
    exitButton = Button(exitButtonFrame, text='关闭', command=closeThisWindow)
    exitButtonFrame.pack(side='top', fill=X, padx=10)
    exitButton.pack(side='top', fill=X, padx=10)
    top.mainloop()