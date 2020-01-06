from tkinter import *
import mysql.connector
from tkinter import ttk
import FunctionUI
# from AddStudentInfo import *


def indexUI(databaseHandle: mysql.connector.connect):
    def closeThisWindow():
        root.destroy()

    # 初始化
    root = Tk()

    # 设置窗体标题
    root.title('数据库实验 实验四 学生管理系统')

    # 设置窗口大小和位置
    root.geometry('550x360')
    # 以下方法用来计算并设置窗体显示时，在屏幕中心居中
    scnWidth, scnHeight = root.maxsize()  # get screen width and height
    tmpcnf = '+%d+%d' % ((scnWidth - 500) / 2, (scnHeight - 300) / 2)
    root.geometry(tmpcnf)

    top_frame = Frame(root, bg='#fff')
    index_lable = Label(top_frame, text='Index', font=('Sinhala MN', '50', 'bold'))
    signature_lable = Label(top_frame, text='-- -- by Leslie', font=('SignPainter', '25', 'italic'))

    top_frame.pack(fill=X, side=TOP, padx=0, pady=0)
    index_lable.pack(side='left', ipadx=30, pady=8)
    signature_lable.pack(side='left', ipadx=0, ipady=20)

    content_frame = Frame(root, bg='#ececec')
    button_frame1 = Frame(content_frame, bg='#ececec')
    button_frame2 = Frame(content_frame, bg='#ececec')
    button_frame3 = Frame(content_frame, bg='#ececec')
    b1 = ttk.Button(button_frame1, text='新增学生信息', command=lambda: FunctionUI.addStudentInfoUI(root, '新增学生信息', databaseHandle), width=25)
    b2 = ttk.Button(button_frame2, text='修改学生信息', command=lambda: FunctionUI.modifyStudentInfoUI(root, '修改学生信息', databaseHandle), width=25)
    b3 = ttk.Button(button_frame1, text='新增课程信息', command=lambda: FunctionUI.addCourseInfoUI(root, '新增课程信息', databaseHandle), width=25)
    b4 = ttk.Button(button_frame2, text='修改课程信息', command=lambda: FunctionUI.modifyCourseInfoUI(root, '修改课程信息', databaseHandle), width=25)
    b5 = ttk.Button(button_frame1, text='录入学生成绩', command=lambda: FunctionUI.addSCInfoUI(root, '录入学生成绩', databaseHandle), width=25)
    b6 = ttk.Button(button_frame2, text='修改学生成绩', command=lambda: FunctionUI.modifySCInfoUI(root, '修改学生成绩', databaseHandle), width=25)
    b7 = ttk.Button(button_frame1, text='成绩统计', command=lambda: FunctionUI.gradeStatisticsUI(root, '成绩统计', databaseHandle), width=25)
    b8 = ttk.Button(button_frame2, text='成绩排名', command=lambda: FunctionUI.rankUI(root, '成绩排名', databaseHandle), width=25)
    b9 = ttk.Button(button_frame1, text='查询学生信息', command=lambda: FunctionUI.queryStudentInfoUI(root, '查询学生信息', databaseHandle), width=25)
    b0 = ttk.Button(button_frame2, text='退出', command=closeThisWindow, width=25)

    content_frame.pack(fill=X, side=TOP, ipady=5)
    button_frame1.pack(side='left', ipadx=5, ipady=50)
    button_frame2.pack(side='left', ipadx=5, ipady=50)
    b1.pack(side="top", pady=10, ipady=5)
    b2.pack(side="top", pady=10, ipady=5)
    b3.pack(side="top", pady=10, ipady=5)
    b4.pack(side="top", pady=10, ipady=5)
    b5.pack(side='top', pady=10, ipady=5)
    b6.pack(side="top", pady=10, ipady=5)
    b7.pack(side="top", pady=10, ipady=5)
    b8.pack(side='top', pady=10, ipady=5)
    b9.pack(side='top', pady=10, ipady=5)
    b0.pack(side='top', pady=10, ipady=5)

    root.mainloop()
