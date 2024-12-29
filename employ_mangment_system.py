from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Data_base

# إنشاء اتصال بقاعدة البيانات
db = Data_base("employees.db")

# إعداد نافذة التطبيق
root = Tk()
root.geometry("1310x515+0+0")
root.config(bg="#33372C")
root.title("Employee Management System")

# إطار الإدخال
enter_frame = Frame(root, bg="#557C56", width=350, height=520)
enter_frame.place(x=1, y=0)

# تعريف المتغيرات
name1 = StringVar()
age1 = StringVar()
jop1 = StringVar()
gender1 = StringVar()
email1 = StringVar()
mobile1 = StringVar()

# عنوان الإطار
title = Label(enter_frame, text="EMPLOYEE COMPANY", bg="#557C56", font=("Calibri", 18, 'bold'), fg="black")
title.place(x=10, y=10)

# حقل الاسم
name = Label(enter_frame, text="Name", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
name.place(x=10, y=50)
entry_name = Entry(enter_frame, textvariable=name1, width=18, bg="#FFE5CF", font=("Calibri", 10, 'bold'))
entry_name.place(x=90, y=55)

# حقل الجنس
gender = Label(enter_frame, text="Gender", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
gender.place(x=10, y=100)
combo_gender = ttk.Combobox(enter_frame, width=18, textvariable=gender1, font=("Calibri", 14, 'bold'), state="readonly")
combo_gender['values'] = ["male", "female"]
combo_gender.place(x=90, y=100)

# حقل الوظيفة
job = Label(enter_frame, text="Job", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
job.place(x=10, y=150)
entry_job = Entry(enter_frame, width=18, bg="#FFE5CF", textvariable=jop1, font=("Calibri", 10, 'bold'))
entry_job.place(x=90, y=155)

# حقل العمر
age = Label(enter_frame, text="Age", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
age.place(x=10, y=200)
entry_age = Entry(enter_frame, width=18, bg="#FFE5CF", textvariable=age1, font=("Calibri", 10, 'bold'))
entry_age.place(x=90, y=205)

# حقل الهاتف
mobile = Label(enter_frame, text="Mobile", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
mobile.place(x=10, y=250)
entry_mobile = Entry(enter_frame, width=18, bg="#FFE5CF", textvariable=mobile1, font=("Calibri", 10, 'bold'))
entry_mobile.place(x=90, y=255)

# حقل البريد الإلكتروني
email = Label(enter_frame, text="Email", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
email.place(x=10, y=300)
entry_email = Entry(enter_frame, textvariable=email1, width=18, bg="#FFE5CF", font=("Calibri", 10, 'bold'))
entry_email.place(x=90, y=305)

# حقل العنوان
address = Label(enter_frame, text="Address", bg="#557C56", font=("Calibri", 14, 'bold'), fg="black")
address.place(x=10, y=330)
text_address = Text(enter_frame, width=30, height=2, bg="#FFE5CF", font=("Calibri", 10, 'bold'))
text_address.place(x=10, y=360)

# دوال التطبيق
def hide():
    root.geometry("360x515+0+0")

def show():
    root.geometry("1240x615+0+0")

# دالة لملء البيانات عند اختيار صف
def getdata(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data['values']
    name1.set(row[1])
    gender1.set(row[2])
    jop1.set(row[3])
    age1.set(row[4])
    mobile1.set(row[5])
    email1.set(row[6])
    text_address.delete(1.0, END)
    text_address.insert(END, row[7])

# دالة لعرض جميع البيانات
def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)
def delete():
    db.remove(row[0])
    clear()
    displayall()
# دالة لمسح جميع الحقول
def clear():
    name1.set("")
    gender1.set("")
    jop1.set("")
    age1.set("")
    mobile1.set("")
    email1.set("")
    text_address.delete(1.0, END)

# دالة لإضافة موظف جديد
def add_employee():
    if entry_name.get() == "" or entry_age.get() == "" or entry_job.get() == "" or entry_email.get() == "" or entry_mobile.get() == "" or combo_gender.get() == "" or text_address.get(1.0, END) == "":
        messagebox.showerror("Error", "Please fill all entry fields")
        return
    db.insert(
        entry_name.get(),
        combo_gender.get(),
        entry_job.get(),
        entry_age.get(),
        entry_mobile.get(),
        entry_email.get(),
        text_address.get(1.0, END)
    )
    clear()
    displayall()
def update_all():
    if entry_name.get() == "" or entry_age.get() == "" or entry_job.get() == "" or entry_email.get() == "" or entry_mobile.get() == "" or combo_gender.get() == "" or text_address.get(1.0, END) == "":
        messagebox.showerror("Error", "Please fill all entry fields")
        return
    db.update(row[0],
        entry_name.get(),
        combo_gender.get(),
        entry_job.get(),
        entry_age.get(),
        entry_mobile.get(),
        entry_email.get(),
        text_address.get(1.0, END)
              )
    clear()
    displayall()

# أزرار التحكم
btn_frame = Frame(enter_frame, bg="#557C56", bd=1)
btn_frame.place(x=5, y=400, width=335, height=100)

# زر الإضافة
btn_add = Button(btn_frame, text="Add", width=14, font=("Calibri", 14, 'bold'), fg="white", bd=0, command=add_employee, bg="#4E9F3D")
btn_add.place(x=4, y=5)

# زر الحذف
btn_delete = Button(btn_frame, text="Delete",command=delete ,width=14, font=("Calibri", 14, 'bold'), fg="white", bd=0, bg="#950101")
btn_delete.place(x=170, y=5)

# زر المسح
btn_clear = Button(btn_frame, text="Clear", width=14, font=("Calibri", 14, 'bold'), fg="white", bd=0, command=clear, bg="#C84B31")
btn_clear.place(x=170, y=50)

# زر التحديث
btn_update = Button(btn_frame, text="Update",command=update_all ,width=14, font=("Calibri", 14, 'bold'), fg="white", bd=0, bg="#064663")
btn_update.place(x=4, y=50)

# إطار الجدول
tree_frame = Frame(root, bg="#33372C")
tree_frame.place(x=352, y=1, width=960, height=520)

# إعداد الجدول
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 14, 'bold'))
style.configure("mystyle.Treeview.Heading", font=("Calibri", 14, 'bold'))

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=40)
tv.heading("2", text="Name")
tv.column("2", width=140)
tv.heading("3", text="Gender")
tv.column("3", width=90)
tv.heading("4", text="Job")
tv.column("4", width=50)
tv.heading("5", text="Age")
tv.column("5", width=50)
tv.heading("6", text="Mobile")
tv.column("6", width=140)
tv.heading("7", text="Email")
tv.column("7", width=100)
tv.heading("8", text="Address")
tv.column("8", width=140)

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getdata)
tv.pack()

# استدعاء عرض جميع البيانات عند بدء التشغيل
displayall()

# تشغيل التطبيق
root.mainloop()