from tkinter import*
from tkinter import ttk 
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Fest:
    def __init__(self,root):
        self.root=root
        self.root.title("Fest Management System")
        self.root.geometry("1540x800+0+0")
        
        self.AID=int()
        self.Aname=StringVar()
        self.Collegename=StringVar() 
        self.City=StringVar()    
        self.State=StringVar()  
        self.Expense=int()   

        lbltitle=Label(self.root,bd=1,relief=RIDGE,text="FEST MANAGEMENT SYSTEM",fg="black",bg="light blue",font=("Garamond",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        Dataframe=Frame(self.root,bd=1,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("Garamond",25),text="Attendee Info")
        DataFrameLeft.place(x=0,y=5,width=765,height=350)

        # DataFrameRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("Garamond",25),text="Event info")
        # DataFrameRight.place(x=765,y=5,width=765,height=350)

        ButtonFrame=Frame(self.root,bd=10,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=480,width=1530,height=50)

        DetailsFrame=Frame(self.root,bd=10,relief=RIDGE,padx=20)
        DetailsFrame.place(x=0,y=530,width=1530,height=250)

        # attendee info

        lblIDAttendee=Label(DataFrameLeft,text="AID",font=("Garamond",20),textvariable=self.AID,padx=2,pady=6)
        lblIDAttendee.grid(row=0,column=0)

        lblNameAttendee=Label(DataFrameLeft,text="AName",font=("Garamond",20),textvariable=self.Aname,padx=2,pady=6)
        lblNameAttendee.grid(row=0,column=1)

        AttendeeName=ttk.Combobox(DataFrameLeft,font=("garamond",15),width=30)
        AttendeeName["values"]=("Keshav","Abhivadhya","Vasu","Shikhar")
        AttendeeName.grid(row=0,column=1)

        lblCollNameAttendee=Label(DataFrameLeft,text="College Name",font=("Garamond",20),textvariable=self.Collegename,padx=2,pady=6)
        lblCollNameAttendee.grid(row=1,column=0)

        AttendeeCollName=ttk.Combobox(DataFrameLeft,font=("garamond",15),width=30)
        AttendeeCollName["values"]=("BITS Pilani","IIT Delhi","IIT Kanpur","MNNIT")
        AttendeeCollName.grid(row=1,column=1)

        lblCityAttendee=Label(DataFrameLeft,text="City",font=("Garamond",20),textvariable=self.City,padx=2,pady=6)
        lblCityAttendee.grid(row=2,column=0)

        AttendeeCityName=ttk.Combobox(DataFrameLeft,font=("garamond",15),width=30)
        AttendeeCityName["values"]=("Kurukshetra","Kolkata","Chandigarh","Moradabad")
        AttendeeCityName.grid(row=2,column=1)

        lblStateAttendee=Label(DataFrameLeft,text="State",font=("Garamond",20),textvariable=self.State,padx=2,pady=6)
        lblStateAttendee.grid(row=3,column=0)

        AttendeeStateName=ttk.Combobox(DataFrameLeft,font=("garamond",15),width=30)
        AttendeeStateName["values"]=("Haryana","West Bengal","Punjab","UP")
        AttendeeStateName.grid(row=3,column=1)

        lblExpense=Label(DataFrameLeft,text="Expense",font=("Garamond",20),textvariable=self.Expense,padx=2,pady=6)
        lblExpense.grid(row=4,column=0)

        # Expense=ttk.Combobox(DataFrameLeft,font=("garamond",15),width=30)
        # Expense["values"]=("Music","Mime","concert","dance")
        # eName.grid(row=4,column=1)

        
        # ticket info
        # lblCollNameAttendee=Label(DataFrameRight,text="College Name",font=("Garamond",20),padx=2,pady=6)
        # lblCollNameAttendee.grid(row=1,column=0)

        # AttendeeCollName=ttk.Combobox(DataFrameRight,font=("garamond",15),width=30)
        # AttendeeCollName["values"]=("BITS Pilani","IIT Delhi","IIT Kanpur","MNNIT")
        # AttendeeCollName.grid(row=1,column=1)

        # lblCityAttendee=Label(DataFrameRight,text="City",font=("Garamond",20),padx=2,pady=6)
        # lblCityAttendee.grid(row=2,column=0)

        # AttendeeCityName=ttk.Combobox(DataFrameRight,font=("garamond",15),width=30)
        # AttendeeCityName["values"]=("Kurukshetra","Kolkata","Chandigarh","Moradabad")
        # AttendeeCityName.grid(row=2,column=1)

        # lblStateAttendee=Label(DataFrameRight,text="State",font=("Garamond",20),padx=2,pady=6)
        # lblStateAttendee.grid(row=3,column=0)

        # AttendeeStateName=ttk.Combobox(DataFrameRight,font=("garamond",15),width=30)
        # AttendeeStateName["values"]=("Haryana","West Bengal","Punjab","UP")
        # AttendeeStateName.grid(row=3,column=1)

        btnSubmit=Button(ButtonFrame,text="Submit",bg="white",fg="black",font=("garamond",15),width=30)
        btnSubmit.grid(row=0,column=0)

        conn=mysql.connector.connect(host="localhost",username="root",password="2602",database="fest_management")
        mycursor=conn.cursor()
        mycursor.execute("insert into attendee values(%d,%s,%s,%d,%s,%s)",(

            self.AID.get(),
            self.AName.get(),
            self.CollegeName.get(),
            self.Expense.get(),
            self.City.get(),
            self.State.get(),
        ))
        conn.commit()
        self.fetchdata()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")
        def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="2602",database="fest_management")
            mycursor=conn.cursor()
            mycursor.execute("select * from attendee")
            rows=mycursor.fetchall()
            if len(rows)!=0:
                self.attendee.delete(*self.attendee.get_AID())
                for i in rows:
                    self.attendee.insert("",END,values=i)

                conn.commit()
                conn.close()

        #update
def update

root=Tk()
ob=Fest(root)
root.mainloop()