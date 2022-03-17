from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Employee Payroll System || Developed By VISHAL PAWAR")
root.geometry("1350x720+0+0")
root.config(bg="white")


#=========================Variables Storage============================

name = StringVar()
company = StringVar()
Hourswork = StringVar()
Tax = StringVar()
Gross = StringVar()
Address = StringVar()
Mobile = StringVar()
Hourlyrate = StringVar()
Overtime = StringVar()
Netpay = StringVar()


#================================Reset Function working=====================
def iReset():
    name.set("")
    company.set("")
    Hourswork.set("")
    Tax.set("")
    Gross.set("")
    Address.set("")
    Mobile.set("")
    Hourlyrate.set("")
    Overtime.set("")
    Netpay.set("")
    txtPaymentSlip.delete("1.0",END)

def Info():
    txtPaymentSlip.delete("1.0",END)
    txtPaymentSlip.insert(END,"\t\t\t Amdocs Presents Pay Slip \n\n")
    txtPaymentSlip.insert(END," \t\t Full Name: \t\t" + name.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Company Name \t\t" + company.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Hours Worked \t\t" + Hourswork.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Tax: \t\t" + Tax.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Gross Pay: \t\t" + Gross.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Address: \t\t" + Address.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Hourly Rate: \t\t" + Hourlyrate.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t Over Time: \t\t" + Overtime.get() + "\n\n")
    txtPaymentSlip.insert(END, " \t\t NetPay: \t\t" + Netpay.get() + "\n\n")

def WagesForWeekly():
    txtPaymentSlip.delete("1.0",END)
    Hrs_wrk_per_Week = float(Hourswork.get())
    wgs_per_hrs = float(Hourlyrate.get())

    DuePayment = Hrs_wrk_per_Week * wgs_per_hrs
    PaymentDue = "P" + str('%.2f' % DuePayment)
    Gross.set(PaymentDue)

    Taxable = DuePayment * 0.13
    taxx = "P" + str('%.2f' % Taxable)
    Tax.set(taxx)

    NetPayment = DuePayment - Taxable
    PaymentNet = "P" + str('%.2f' % NetPayment)
    Netpay.set(PaymentNet)

    if Hrs_wrk_per_Week > 40:
        hrs_per_wk = (Hrs_wrk_per_Week - 40) + wgs_per_hrs * 1.5
        hrs_week = "P" + str('%.2f' % hrs_per_wk)
        Overtime.set(hrs_week)
    

def iExit():
    Close = messagebox.askyesno("Employee Payroll System","Do you want to exit ?")
    if Close > 0:
        root.destroy()
        return
#===================================Frames=====================
Tops = Frame(root,width=1320,height=80,bd=10,relief='raise')
Tops.place(x=10,y=20)

Fleft = Frame(root,width=800,height=500,bd=6,relief='raise')
Fleft.place(x=10,y=106)

Fright = Frame(root,width=480,height=500,bd=5,relief='ridge')
Fright.place(x=845,y=106)

Fbtn = Frame(root,width=1320,height=80,relief='raise',bd=4)
Fbtn.place(x=10,y=630)

#===================================title frame name=====================
lblTitle = Label(Tops,text="Amdocs Employees Payroll Management System",font=("arial",32,'bold'),bg='orange',fg='black',anchor='w',bd=4,relief='ridge')
lblTitle.place(x=160,y=0)

#========================Fleft frame labels===================================
lblName = Label(Fleft,text='Name',font=('arial',18,'bold'),relief='raise',bd=3)
lblName.place(x=12,y=10)

lblccompany = Label(Fleft,text='Company',font=('arial',18,'bold'),relief='raise',bd=3)
lblccompany.place(x=12,y=100)

lblHHours = Label(Fleft,text='Hours Worked',font=('arial',18,'bold'),relief='raise',bd=3)
lblHHours.place(x=12,y=200)

lblttax = Label(Fleft,text='Tax',font=('arial',18,'bold'),relief='raise',bd=3)
lblttax.place(x=12,y=300)

lblggrosspay = Label(Fleft,text='Gross Pay',font=('arial',18,'bold'),relief='raise',bd=3)
lblggrosspay.place(x=12,y=400)

lblAAddress = Label(Fleft,text='Address',font=('arial',18,'bold'),relief='raise',bd=3)
lblAAddress.place(x=420,y=10)

lblmmobile = Label(Fleft,text='Mobile',font=('arial',18,'bold'),relief='raise',bd=3)
lblmmobile.place(x=420,y=100)

lblHHourleyRate = Label(Fleft,text='Hourly Rate',font=('arial',18,'bold'),relief='raise',bd=3)
lblHHourleyRate.place(x=420,y=200)

lblOOverTime = Label(Fleft,text='Over Time',font=('arial',18,'bold'),relief='raise',bd=3)
lblOOverTime.place(x=420,y=300)

lblNNetPay = Label(Fleft,text='Net Pay',font=('arial',18,'bold'),relief='raise',bd=3)
lblNNetPay.place(x=420,y=400)

#==========================Fleft Entries========================================
txtname = Entry(Fleft,width=18,textvariable=name,relief='sunken',bd=4,font='arial 15 bold')
txtname.place(x=185,y=11)

txtcompany = Entry(Fleft,width=18,textvariable=company,relief='sunken',bd=4,font='arial 15 bold')
txtcompany.place(x=185,y=101)

txtHourswork = Entry(Fleft,width=18,textvariable=Hourswork,relief='sunken',bd=4,font='arial 15 bold')
txtHourswork.place(x=185,y=201)

txtTax = Entry(Fleft,width=18,textvariable=Tax,relief='sunken',bd=4,font='arial 15 bold')
txtTax.place(x=185,y=301)

txtGross = Entry(Fleft,width=18,textvariable=Gross,relief='sunken',bd=4,font='arial 15 bold')
txtGross.place(x=185,y=401)

txtAddress = Entry(Fleft,width=18,textvariable=Address,relief='sunken',bd=4,font='arial 15 bold')
txtAddress.place(x=565,y=11)

txtMobile = Entry(Fleft,width=18,textvariable=Mobile,relief='sunken',bd=4,font='arial 15 bold')
txtMobile.place(x=565,y=101)

txtHourlyrate = Entry(Fleft,width=18,textvariable=Hourlyrate,relief='sunken',bd=4,font='arial 15 bold')
txtHourlyrate.place(x=565,y=201)

txtOvertime = Entry(Fleft,width=18,textvariable=Overtime,relief='sunken',bd=4,font='arial 15 bold')
txtOvertime.place(x=565,y=301)

txtNetpay = Entry(Fleft,width=18,textvariable=Netpay,relief='sunken',bd=4,font='arial 15 bold')
txtNetpay.place(x=565,y=401)

#============================Buttons======================================
btnWeeklySalary = Button(Fbtn,text="Weekly Salary",command=WagesForWeekly,relief='raise',bd=5,font=('arial',15,'bold'))
btnWeeklySalary.place(x=20,y=10)

btnReset = Button(Fbtn,text="Reset",relief='raise',command=iReset,bd=5,font=('arial',15,'bold'))
btnReset.place(x=400,y=10)

btnSlip = Button(Fbtn,text="View Slip",command=Info,relief='raise',bd=5,font=('arial',15,'bold'))
btnSlip.place(x=800,y=10)

btnExit = Button(Fbtn,text="Exit System",command=iExit,relief='raise',bd=5,font=('arial',15,'bold'))
btnExit.place(x=1130,y=10)

#=====================textarea widgets============================================
PaySlip = Label(Fright,font='arial 14 bold',bg='orange',fg='black',bd=10,relief='raise',text='Amdocs Company Payment Slip').place(x=80,y=10)

txtPaymentSlip = Text(Fright,font='arial 9 bold',width=65,height=25)
txtPaymentSlip.place(x=5,y=60)



root.mainloop()