from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import sqlite3


def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital anagement System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.master.configure(background="blue")

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="Hospital Management Systems", font=('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.LoginFrame1 = LabelFrame(self.frame, width=1010, height=300, font=('arial', 20, 'bold'), relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=100, font=('arial', 20, 'bold'), relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        self.LoginFrame3 = LabelFrame(self.frame, width=1000, height=200, font=('arial', 20, 'bold'), relief='ridge')
        self.LoginFrame3.grid(row=3, column=0, pady=10)

        # ===============================================================================================================
        self.lblUsername = Label(self.LoginFrame1, text="Username", font=('arial', 30, 'bold'), bd=20)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, text="Username", font=('arial', 30, 'bold'), bd=20,
                                 textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text="Password", font=('arial', 30, 'bold'), bd=20)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, text="Password", font=('arial', 30, 'bold'), bd=20,
                                 textvariable=self.Password, show="*")
        self.txtPassword.grid(row=1, column=1)

        # ================================Buttons1==============================================================================

        self.btnLogin = Button(self.LoginFrame2, text="Login", width=17, font=('arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.LoginFrame2, text="Reset", width=17, font=('arial', 20, 'bold'), command=self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnSign = Button(self.LoginFrame2, text="Sign Up", width=17, font=('arial', 20, 'bold'),
                              command=self.SignUp)
        self.btnSign.grid(row=0, column=2)

        self.btnExit = Button(self.LoginFrame2, text="Exit", width=17, font=('arial', 20, 'bold'), command=self.iExit)
        self.btnExit.grid(row=0, column=3)
        # ==============================Buttons2=======================================================================================

        self.btnPatients = Button(self.LoginFrame3, text="Patient Registration", font=('arial', 20, 'bold'),
                                      state=DISABLED, command=self.Registration_window)
        self.btnPatients.grid(row=0, column=0)

        # =======================================Window1 Functions===============================================================================

    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user=="" or pas==""):
            tkinter.messagebox.showinfo("Insert Status","All fields are required")
        else:
            conn = sqlite3.connect("PatientsBase.db")
            cursor=conn.cursor()
            sqlite_select_query = """SELECT * from Patients"""
            cursor.execute(sqlite_select_query)
            pat = cursor.fetchall()
            for column in pat:
                if user==str(column[7]) and pas==str(column[8]):
                    self.btnPatients.config(state=NORMAL)
                    break
                else:
                    tkinter.messagebox.showinfo("Insert Status","There is no Patient with these Username or Password")
                    conn.commit()
                    self.Reset()
                    break



    def Reset(self):
        self.btnPatients.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return
        else:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
            return

    def SignUp(self):
        self.SignUp = Toplevel(self.master)
        self.app = SignUp(self.SignUp)

    def Registration_window(self):
        self.Patients = Toplevel(self.master)
        self.app = Patients(self.Patients)

        # ===================================Sign Up======================================================================================


class SignUp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up System")
        self.master.geometry('1100x600+0+0')
        self.master.configure(background='light blue')

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        Identity = StringVar()
        Age = StringVar()
        Username = StringVar()
        Password = StringVar()
        Gender = StringVar()

        def database():
            firstname = self.txtName.get()
            surname = self.txtSurname.get()
            address = self.txtAddress.get()
            postcode = self.txtPostCode.get()
            telephone = self.txtTelephone.get()
            identity = self.txtIdentityNo.get()
            age = self.txtAge.get()
            username = self.txtUser.get()
            password = self.txtPassword.get()
            gender = self.cboGender.get()




            if (str(username) != str(password)):
                self.ValidLabel2.grid(row=4, column=0)
                Reset()
            else:
                conn = sqlite3.connect("PatientsBase.db")
                with conn:
                    cursor = conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS Patients (FIRSTNAME TEXT,SURNAME TEXT,ADDRESS TEXT,POSTCODE TEXT,TELEPHONE TEXT,IDENTITY TEXT,AGE TEXT,USERNAME TEXT,PASSWORD TEXT,GENDER TEXT)')
                cursor.execute(
                    'INSERT INTO Patients (FIRSTNAME,SURNAME,ADDRESS,POSTCODE,TELEPHONE,IDENTITY,AGE,USERNAME,PASSWORD,GENDER) VALUES(?,?,?,?,?,?,?,?,?,?)',
                    (firstname, surname, address, postcode, telephone, identity, age, username, password, gender))
                conn.commit()
                tkinter.messagebox.showinfo("Sign Up System","Welcome to our system")


        def Reset():
            Firstname.set("")
            Username.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Identity.set("")
            Age.set("")
            Username.set("")
            Password.set("")
            Gender.set("")

        def iExit():
            self.iExit = tkinter.messagebox.askyesno("Patient Sign Up System", "Confirm if you want to exit")
            if self.iExit > 0:
                self.master.destroy()
                return
            else:
                self.SignUp = Toplevel(self.master)
                self.app = SignUp(self.SignUp)
                return



        # ================================Frames====================================================================================
        Mainframe = Frame(self.master)
        Mainframe.pack()

        self.LabelTitle = Label(Mainframe, text="Patient Sign Up System", font=('arial', 30, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.PatientInfo = LabelFrame(Mainframe, width=1010, height=300, font=('arial', 20, 'bold'), relief='ridge',
                                      bd=20)
        self.PatientInfo.grid(row=1, column=0)

        self.ButtonFrame = LabelFrame(Mainframe, width=1010, height=100, font=('arial', 20, 'bold'), relief='ridge')
        self.ButtonFrame.grid(row=2, column=0)

        self.ValidLabel1 = Label(Mainframe, text="***Your username and Password must be the same",
                                 font=('arial', 10, 'bold'))
        self.ValidLabel1.grid(row=4, column=0)

        self.ValidLabel2 = Label(Mainframe, text="***Your username and Password are not the same",
                                 font=('arial', 15, 'bold'))

        # ===============================Labels and Buttons========================================================================

        self.btnSave = Button(self.ButtonFrame, text="Save", width=17, font=('arial', 20, 'bold'), command=database)
        self.btnSave.grid(row=0, column=0)

        self.btnReset = Button(self.ButtonFrame, text="Reset", width=17, font=('arial', 20, 'bold'), command=Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.ButtonFrame, text="Exit", width=17, font=('arial', 20, 'bold'), command=iExit)
        self.btnExit.grid(row=0, column=3)
        # ==================================
        self.lblName = Label(self.PatientInfo, text="Firstname", font=('arial', 14, 'bold'), bd=7)
        self.lblName.grid(row=0, column=0)
        self.txtName = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, textvariable=Firstname, insertwidth=2)
        self.txtName.grid(row=0, column=1)

        self.lblSurname = Label(self.PatientInfo, text="Surname", font=('arial', 14, 'bold'), bd=7)
        self.lblSurname.grid(row=1, column=0)
        self.txtSurname = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Surname)
        self.txtSurname.grid(row=1, column=1)

        self.lblAddress = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, textvariable=Address, insertwidth=2)
        self.txtAddress.grid(row=2, column=1)

        self.lblPostCode = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Post Code", bd=7)
        self.lblPostCode.grid(row=3, column=0, sticky=W)
        self.txtPostCode = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, textvariable=Postcode,
                                 insertwidth=2)
        self.txtPostCode.grid(row=3, column=1)

        self.lblTelephone = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=4, column=0, sticky=W)
        self.txtTelephone = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, textvariable=Telephone,
                                  insertwidth=2)
        self.txtTelephone.grid(row=4, column=1)

        self.lblIdentityNo = Label(self.PatientInfo, font=("arial", 14, "bold"), text="Identity No:", bd=7)
        self.lblIdentityNo.grid(row=0, column=2, sticky=W)
        self.txtIdentityNo = Entry(self.PatientInfo, font=("arial", 14, "bold"), textvariable=Identity, bd=7,
                                   insertwidth=2)
        self.txtIdentityNo.grid(row=0, column=3)

        self.lblAge = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Age", bd=7)
        self.lblAge.grid(row=1, column=2, sticky=W)
        self.txtAge = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Age)
        self.txtAge.grid(row=1, column=3)

        self.lblUser = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Username", bd=7)
        self.lblUser.grid(row=2, column=2, sticky=W)
        self.txtUser = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Username)
        self.txtUser.grid(row=2, column=3)

        self.lblPassword = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Password", bd=7)
        self.lblPassword.grid(row=3, column=2, sticky=W)
        self.txtPassword = Entry(self.PatientInfo, font=('arial', 14, 'bold'), bd=7, insertwidth=2,
                                 textvariable=Password)
        self.txtPassword.grid(row=3, column=3)

        self.lblGender = Label(self.PatientInfo, font=('arial', 14, 'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=4, column=2, sticky=W)
        self.cboGender = ttk.Combobox(self.PatientInfo, state='readonly', font=('arial', 14, 'bold'), width=19,
                                      textvariable=Gender)
        self.cboGender['value'] = ("", "Male", "Female")
        self.cboGender.current("0")
        self.cboGender.grid(row=4, column=3)

    # =========================================================================================================================

class Patients:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient System")
        self.master.geometry('1350x750+0+0')
        self.master.configure()

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))


        Ref = StringVar()
        User = StringVar()
        Payment = StringVar()
        Membership = StringVar()
        Tablets = StringVar()
        Boxes = StringVar()
        Dose = StringVar()
        NoTablets = StringVar()
        Info = StringVar()


        Membership = StringVar()
        Membership.set("0")

        def RefNo():
            x=random.randint(10000, 60000)
            randomRef=str(x)
            Ref.set(randomRef)

        def Membership_Fees():
            Item=self.txtMembership.get()
            self.chkMembership.configure(state=NORMAL)
            Membership.set("€" + str(Item))

        def iPrescription():
            RefNo()
            self.txtPrescription.insert(END, self.txtRef.get() + "\n\n" + self.txtDate.get() + "\t\t" + self.txtBoxes.get() +" Boxes "
                                       + self.cboTablets.get() + "\t\t\t" + self.txtDose.get() + " Pills/Day" + "\t\t" + self.txtNoDose.get() + "/Dose"
                                        + "\t"+self.txtInfo.get())


        def Reset():
            Ref.set("")
            User.set("")
            Payment.set("")
            Tablets.set("")
            Boxes.set("")
            Dose.set("")
            NoTablets.set("")
            Info.set("")


        def iExit():
            self.iExit = tkinter.messagebox.askyesno("Patient System", "Confirm if you want to exit")
            if self.iExit > 0:
                self.master.destroy()
                return
            else:
                self.Patients = Toplevel(self.master)
                self.app = Patients(self.Patients)
                return


        def database():

            ref=self.txtRef.get()
            user=self.txtUser.get()
            date=self.txtDate.get()
            payment=self.cboMethodofPayment.get()
            membership=self.txtMembership.get()
            tablets=self.cboTablets.get()
            boxes=self.txtBoxes.get()
            dose=self.txtDose.get()
            notablets=self.txtNoDose.get()
            info=self.txtInfo.get()



            conn = sqlite3.connect("PatientsBase.db")
            with conn:
                cursor = conn.cursor()
            cursor.execute(

                'CREATE TABLE IF NOT EXISTS Pharmacy (REFERENCE TEXT,USERNAME TEXT,DATE TEXT,PAYMENT TEXT,MEMBERSHIP TEXT,TABLETS TEXT,BOXES TEXT,DOSE TEXT,NoTABLETS TEXT,INFO TEXT)')
            cursor.execute(
                'INSERT INTO Pharmacy (REFERENCE,USERNAME,DATE,PAYMENT,MEMBERSHIP,NoTABLETS,BOXES,DOSE,NoTABLETS,INFO) VALUES(?,?,?,?,?,?,?,?,?,?)',
                (ref, user, date, payment, membership, tablets, boxes, dose, notablets, info))
            conn.commit()

        #====================================================================================================================
        Mainframe = Frame(self.master)
        Mainframe.pack()

        self.LabelTitleFrame = Label(Mainframe, text="Patient System", font=('arial', 20, 'bold'))
        self.LabelTitleFrame.grid(row=0, column=0)

        self.PatientInfoFrame = LabelFrame(Mainframe, width=1200, height=400, font=('arial', 15, 'bold'), relief='ridge', bd=10)
        self.PatientInfoFrame.grid(row=1, column=0)

        self.ButtonFrame = LabelFrame(Mainframe, width=1010, height=50, font=('arial', 15, 'bold'), relief='ridge', bd=10)
        self.ButtonFrame.grid(row=2, column=0)

        self.ReceiptFrame = Text(Mainframe, width=1010, height=200, font=('arial', 15, 'bold'), relief='ridge', bd=10)
        self.ReceiptFrame.grid(row=3, column=0)

        #===========================================Widgets=================================================================
        self.lblRef = Label(self.PatientInfoFrame, text="Reference No", font=('arial', 14, 'bold'), bd=7)
        self.lblRef.grid(row=0, column=0, sticky=W)
        self.txtRef = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Ref, state=DISABLED, cursor="circle" )
        self.txtRef.grid(row=0, column=1)

        self.lblUser = Label(self.PatientInfoFrame, text="Username", font=('arial', 14, 'bold'), bd=7)
        self.lblUser.grid(row=1, column=0, sticky=W)
        self.txtUser = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=User)
        self.txtUser.grid(row=1, column=1)

        self.lblDate = Label(self.PatientInfoFrame, text="Date", font=('arial', 14, 'bold'), bd=7)
        self.lblDate.grid(row=2, column=0, sticky=W)
        self.txtDate = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2 , textvariable=DateofOrder)
        self.txtDate.grid(row=2, column=1)

        self.lblMethodofPayment = Label(self.PatientInfoFrame, text="Payment", font=('arial', 14, 'bold'), bd=7)
        self.lblMethodofPayment.grid(row=3, column=0, sticky=W)
        self.cboMethodofPayment = ttk.Combobox(self.PatientInfoFrame, state='readonly',width=19, font=('arial', 14, 'bold'), textvariable=Payment)
        self.cboMethodofPayment['value'] = ("","Visa Card","Master Card","Debit Card","Cash")
        self.cboMethodofPayment.current(0)
        self.cboMethodofPayment.grid(row=3, column=1)

        self.chkMembership = Checkbutton(self.PatientInfoFrame, font=('arial', 14, 'bold'), onvalue=1,text="Patient Fees",
                                         offvalue=0, command=Membership_Fees)
        self.chkMembership.grid(row=4, column=0, sticky=W)
        self.txtMembership = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, justify=RIGHT, textvariable=Membership)
        self.txtMembership.grid(row=4, column=1)

        self.lblTablets = Label(self.PatientInfoFrame, text="Tablets", font=('arial', 14, 'bold'), bd=7)
        self.lblTablets.grid(row=0, column=2, sticky=W)
        self.cboTablets = ttk.Combobox(self.PatientInfoFrame, state='readonly', width=19,
                                               font=('arial', 14, 'bold'), textvariable=Tablets)
        self.cboTablets['value'] = ("", "Ibuprofen", "Co-codamol", "Paracetamol", "Almodipine")
        self.cboTablets.current(0)
        self.cboTablets.grid(row=0, column=3)

        self.lblBox = Label(self.PatientInfoFrame, text="Boxes", font=('arial', 14, 'bold'), bd=7)
        self.lblBox.grid(row=1, column=2, sticky=W)
        self.txtBoxes = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Boxes)
        self.txtBoxes.grid(row=1, column=3)

        self.lblDose = Label(self.PatientInfoFrame, text="Dose", font=('arial', 14, 'bold'), bd=7)
        self.lblDose.grid(row=2, column=2, sticky=W)
        self.txtDose = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Dose)
        self.txtDose.grid(row=2, column=3)

        self.lblNoDose = Label(self.PatientInfoFrame, text="Tablets/Dose", font=('arial', 14, 'bold'), bd=7)
        self.lblNoDose.grid(row=3, column=2, sticky=W)
        self.txtNoDose = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=NoTablets)
        self.txtNoDose.grid(row=3, column=3)

        self.lblInfo = Label(self.PatientInfoFrame, text="Further Info", font=('arial', 14, 'bold'), bd=7)
        self.lblInfo.grid(row=4, column=2, sticky=W)
        self.txtInfo = Entry(self.PatientInfoFrame, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Info)
        self.txtInfo.grid(row=4, column=3)

        #=======================ButtonFrame=====================================================================================
        self.OKButton = Button(self.ButtonFrame, text="OK", width=9, font=('arial', 20, 'bold'), command=iPrescription)
        self.OKButton.grid(row=0, column=0)

        self.SAVEButton = Button(self.ButtonFrame, text="SAVE", width=9, font=('arial', 20, 'bold'), command=database)
        self.SAVEButton.grid(row=0, column=1)

        self.RESETButton = Button(self.ButtonFrame, text="Reset", width=9, font=('arial', 20, 'bold'), command= Reset)
        self.RESETButton.grid(row=0, column=2)

        self.EXITButton = Button(self.ButtonFrame, text="Exit", width=9, font=('arial', 20, 'bold'), command= iExit)
        self.EXITButton.grid(row=0, column=3)

        #==========================ReceiptFrame==========================================================================

        self.lblLabel = LabelFrame(self.ReceiptFrame, font=('arial', 13, 'bold'), pady=10,
                              text="Receipt",
                              bd=7)
        self.lblLabel.grid(row=0, column=0)

        self.txtPrescription = Text(self.lblLabel, font=("arial", 12, "bold"), height=12)
        self.txtPrescription.grid()







if __name__ == "__main__":
    main()
