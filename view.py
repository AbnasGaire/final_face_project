import tkinter as tk
from tkinter import Message, Text
import cv2, os
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.font as font
import pymysql
from tkinter import ttk
# from Tkinter import *

window = tk.Tk()
window.title("Kathmandu Bernhardt College")
window.configure(background='gray')
window.geometry('1280x670')

def viewstd():
    con=pymysql.connect(host="localhost" ,user="root",passwd="",db="face")
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('',tk.END,values=row)
        con.commit()
    con.close()
lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white" , fg="black" , width=50 , height=2, font=('times', 30, 'italic bold')) 
lbl.place(x=100, y=20)

Table_Frame=tk.Frame(window,bd=3,bg="crimson")
Table_Frame.place(x=200,y=200,width=800,height=200)
scroll_x=tk.Scrollbar(Table_Frame,orient=tk.HORIZONTAL)
scroll_y=tk.Scrollbar(Table_Frame,orient=tk.VERTICAL)
Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Sem"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
scroll_y.pack(side=tk.RIGHT,fill=tk.Y)
scroll_x.config(command=Student_table.xview)
scroll_y.config(command=Student_table.yview)

Student_table.heading("Roll",text="Roll no")
Student_table.heading("Name",text="Name")
Student_table.heading("Sem",text="Sem")
Student_table['show']='headings'
viewstd()
Student_table.pack()




def delete():
    window = tk.Tk()
    window.title("Kathmandu Bernhardt College")
    window.configure(background='gray')
    window.geometry('1280x670')

    lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white" , fg="black" , width=50 , height=2, font=('times', 30, 'italic bold')) 
    lbl.place(x=100, y=20)

    lbl1 = tk.Label(window, text="Enter ID", width=20 , height=2 , fg="black" , bg="white", font=('times', 15, ' bold ') ) 
    lbl1.place(x=200, y=200)

    global stdid
    stdid= tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
    stdid.place(x=550, y=215)

   
    quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="black", bg="white", width=20, height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    quitWindow.place(x=800, y=400)

    delete = tk.Button(window, text="Delete",command=cleardata, fg="black", bg="white", width=20, height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    delete.place(x=500, y=400)


    lbl3 = tk.Label(window, text="KBC", width=80, fg="white", bg="black", font=('times', 15, ' bold')) 
    lbl3.place(x=200, y=620)
    
    
    window.mainloop()



def cleardata():
    id=stdid.get()
    print(id)
    con=pymysql.connect(host="localhost" ,user="root",passwd="",db="face")
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE id='%s'"%(id))
    con.commit()
    con.close()
    print("deleted data")


def edit():
    window = tk.Tk()
    window.title("Kathmandu Bernhardt College")
    window.configure(background='gray')
    window.geometry('1280x670')

    lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white" , fg="black" , width=50 , height=2, font=('times', 30, 'italic bold')) 
    lbl.place(x=100, y=20)

    lbl1 = tk.Label(window, text="Enter ID", width=20 , height=2 , fg="black" , bg="white", font=('times', 15, ' bold ') ) 
    lbl1.place(x=200, y=200)

    stdid= tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
    stdid.place(x=550, y=215)

    
    quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="black", bg="white", width=20, height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    quitWindow.place(x=800, y=400)

    edit = tk.Button(window, text="Edit",command=lambda:update(stdid), fg="black", bg="white", width=20, height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
    edit.place(x=500, y=400)


    lbl3 = tk.Label(window, text="KBC", width=80, fg="white", bg="black", font=('times', 15, ' bold')) 
    lbl3.place(x=200, y=620)
    
    return stdid
    window.mainloop()



def update(stdid):
        getId=stdid.get()
        
        con=pymysql.connect(host="localhost" ,user="root",passwd="",db="face")
        cur=con.cursor()
        cur.execute("select * from student where id="+getId)
        records=cur.fetchall()
        con.close()

        
        
        window = tk.Tk()
        window.title("Kathmandu Bernhardt College")
        window.configure(background='gray')
        window.geometry('1280x670')

        lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white" , fg="black" , width=50 , height=2, font=('times', 30, 'italic bold')) 
        lbl.place(x=100, y=20)

        lbl1 = tk.Label(window, text="Enter ID", width=20 , height=2 , fg="black" , bg="white", font=('times', 15, ' bold ') ) 
        lbl1.place(x=200, y=200)
        global txt1
        txt1 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        txt1.place(x=550, y=215)

        lbl2 = tk.Label(window, text="Enter Name", width=20 , fg="black", bg="white", height=2, font=('times', 15, ' bold ')) 
        lbl2.place(x=200, y=300)
        global txt2
        txt2 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold ')  )
        txt2.place(x=550, y=315)

        lbl4 = tk.Label(window, text="Enter Sem", width=20 , height=2 , fg="black" , bg="white", font=('times', 15, ' bold ') ) 
        lbl4.place(x=200, y=400)
        global txt4
        txt4 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold ')  )
        txt4.place(x=550, y=400)

        for record in records:
            txt1.insert(0,record[0])
            txt2.insert(0,record[1])
            txt4.insert(0,record[2])



        update = tk.Button(window, text="Update",command=lambda:save(getId),fg="black", bg="white", width=20, height=3, activebackground = "Green", font=('times', 15, ' bold '))
        update.place(x=400, y=500)

        window.mainloop()



def save(getId):
    con=pymysql.connect(host="localhost" ,user="root",passwd="",db="face")
    cur=con.cursor()
    a=getId
    print(a)
    cur.execute("UPDATE student SET name='%s', sem ='%s' WHERE id = '%s'"%(txt2.get(),txt4.get(),a))
    con.commit()
    con.close()





    
 

edit = tk.Button(window, text="Edit Student", command=edit, fg="black", bg="white", width=20, height=3, activebackground = "Green" ,font=('times', 15, ' bold '))
edit.place(x=50, y=400)

edit = tk.Button(window, text="Delete Student",command=delete, fg="black", bg="white", width=20, height=3, activebackground = "Green" ,font=('times', 15, ' bold '))
edit.place(x=350, y=400)


quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="black", bg="white", width=20, height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=650, y=400)

lbl3 = tk.Label(window, text="KBC", width=80, fg="white", bg="black", font=('times', 15, ' bold')) 
lbl3.place(x=200, y=620)

window.mainloop()