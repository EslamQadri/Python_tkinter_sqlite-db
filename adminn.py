
from tkinter import*
from tkinter import ttk
from data import *
class ButtonAdmin:
    def __init__(self,root):
        self.root=root
        self.root.title("By ahmed Abdel El Khaleq")
        self.root.geometry("1000x600+0+0") 
         
        self.lbltitle=Label(self.root,text="WELCOME Admin",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        self.lbltitle.pack(side=TOP,fill=X) 
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        frame.place(x=0,y=130,width=1000,height=500)         
        #  =================================DataFrameLeft===========================================
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",
                                 bd=12,relief=RIDGE,font=("arial",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=400)
        self.BookIdd= StringVar()
        self.BookTitlee=StringVar()
        self.Autherr=StringVar()
        self.Summeryyy=StringVar()
        self.ActualPricee=StringVar()
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book ID:",
                        padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        
        self.BookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.BookIdd,width=29)
        self.BookId.grid(row=0,column=3)
        
        lblBooktitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",
                           padx=2,pady=6,bg="powder blue")
        lblBooktitle.grid(row=1,column=2,sticky=W)
        self.BookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.BookTitlee,width=29)
        self.BookTitle.grid(row=1,column=3)
        
        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",
                        padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        self.Auther=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Autherr,width=29)
        self.Auther.grid(row=2,column=3)
      
        lblSummery=Label(DataFrameLeft,font=("arial",12,"bold"),text="Summery :",
                              padx=2,pady=6,bg="powder blue")
        lblSummery.grid(row=7,column=2,sticky=W)
        self.Summery=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Summeryyy,width=29)
        self.Summery.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",
                             padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        self.ActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable= self.ActualPricee,width=29)
        self.ActualPrice.grid(row=8,column=3)
        
        
        
        #====================================== Button Frame ============================================
        
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        Framebutton.place(x=0,y=530,width=1000,height=70)
        
        
        
            
        def enter_to_database():
            id=(self.BookIdd.get())
            booktitle=(self.BookTitlee.get())
            auther=(self.Autherr.get())
            summery= (self.Summeryyy.get())
            price=(self.ActualPricee.get())
    

            insert_to_database(id ,booktitle,auther,summery,price)
    
    
        

        self.btnAddData=Button(Framebutton,text=" Save ",font=("arial",15,"bold"),command=lambda:enter_to_database(),
                          width=30,height=1,bg="green",fg="white")
        self.btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,text="Back",font=("arial",15,"bold"),command=lambda:back_to_admin_dachbord(root),
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=0,column=1)
        
           

def runaddpage():
    root=Tk()
    objkt=ButtonAdmin(root)
    root.mainloop()
def delete_action(root):
    root.destroy()
    delete_page()
def reed_viwe():
    root=Tk()
    obj=Reader(root)
    root.mainloop()
def reed_action(root):
    root.destroy()
    reed_viwe()
#+++++++++++++++++++++++++++++++++

class DeleteData:
    def __init__(self,root):
        self.root=root
        self.root.title("By Ahmed Abdel El Khaleq")
        self.root.geometry("600x300+0+0")
        
        
        lbltitle=Label(self.root,text="Delete The Book",bg="powder blue",fg="green",bd=21,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        frame.place(x=0,y=130,width=900,height=670)
        
        
        
        
        #====================================== Button Frame ============================================
        
        Framebutton=Frame(self.root,bd=20,relief=RIDGE,padx=100,bg="powder blue",)
        Framebutton.place(x=0,y=100,width=900,height=670)
        
        self.txt=StringVar()
        btnAddData=Button(Framebutton,text=" Delete ",font=("arial",15,"bold"),command=lambda:delete_by_Id(self.txt.get()),
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,text="Back",font=("arial",15,"bold") ,command=lambda: back_to_admin_dachbord(root), 
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=1,column=0)
        
        lblMember=Label(Framebutton,bg="powder blue",text="Book ID",
                        font=("arial ",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=2,column=0,sticky=W)
        self.txtPRN_NO=Entry(Framebutton,font=("arial",13,"bold"),textvariable=self.txt,widt=20)
        self.txtPRN_NO.grid(row=2,column=0)



def delete_page():
    root=Tk()
    obj=DeleteData(root)
    root.mainloop()
#++++++++++++++++++++++++++++
class WelecomAdmin:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("By ahmed Abdel El Khaleq")
        self.root1.geometry("900x250+0+0")
        
        
        lbltitle=Label(self.root1,text="WELCOME Admin",bg="powder blue",fg="green",bd=21,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root1,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        frame.place(x=0,y=130,width=900,height=670)
        
        
        #====================================== Button Frame ============================================
        
        Framebutton=Frame(self.root1,bd=20,relief=RIDGE,padx=100,bg="powder blue",)
        Framebutton.place(x=0,y=100,width=900,height=670)
        

        btnAddData=Button(Framebutton,text=" Add ",font=("arial",15,"bold"),
                          width=30,height=1,bg="green",fg="white",command=lambda:run_add_buttom(root1))
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,text="Delete",font=("arial",15,"bold"),command=lambda:delete_action(root1),
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,text="Reset",font=("arial",15,"bold"),command=reset,
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=1,column=0)
        
        btnAddData=Button(Framebutton,text="Back",font=("arial",15,"bold"),command=lambda:back_to_start(root1),
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=1,column=1)
        
def run_add_buttom(root1):
    root1.destroy()
    runaddpage()

def admain_dashbord():
    root1=Tk()
    objadmin=WelecomAdmin(root1) 
    root1.mainloop()

def back_to_admin_dachbord(root1):
    root1.destroy()
    admain_dashbord()

def back_to_start(root1):
    root1.destroy()
    start_gate()
def exit(root):
    root.destroy()
#++++++++++++++++++++++++++++++++++++++++
class Reader:
    def __init__(self,root):
        self.root=root
        self.root.title("By Ahmed Abdel El Khaleq")
        self.root.geometry("1000x450+0+0")
        
        
        lbltitle=Label(self.root,text="WELCOME TO READE",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        frame.place(x=0,y=130,width=1000,height=500)
        
         
      
        
        
        
        #====================================== Button Frame ============================================
        
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        Framebutton.place(x=0,y=335,width=1000,height=70)
        
        

        btnAddData=Button(Framebutton,text="  Back ",font=("arial",15,"bold"),command=lambda:back_to_start(root),
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,text="Exit",font=("arial",15,"bold"),command=lambda:exit(root),
                          width=30,height=1,bg="green",fg="white")
        btnAddData.grid(row=0,column=1)
        
        
        #=====================================Information Frame=========================================
        
        
        
        
        FrameDetalis=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetalis.place(x=0,y=135,width=1000,height=200)
 
        
        
        xscroll=ttk.Scrollbar(FrameDetalis,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(FrameDetalis,orient=VERTICAL)
        columns=("bookid","booktitle","auther","Summery","finalprice")
        self.libray_table=ttk.Treeview(FrameDetalis,column=columns, show='headings',
                                       xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)
        def View(): 
    
            import sqlite3

            con1 = sqlite3.connect("database")

            cur1 = con1.cursor()

            cur1.execute("SELECT * FROM BOOK")

            rows = cur1.fetchall()    

            for row in rows:
                self.libray_table.insert('', 'end', value=row)
                
               

            con1.close()
        View()
        self.libray_table.heading("bookid",text="Book ID")
        self.libray_table.heading("booktitle",text="Book Title")
        self.libray_table.heading("auther",text="Auther")

        self.libray_table.heading("Summery",text="Summery")
        self.libray_table.heading("finalprice",text="Final Price")
        
        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH,expand=1)
                          
       
        self.libray_table.column("bookid",width=100)
        self.libray_table.column("booktitle",width=100)
        self.libray_table.column("auther",width=100)

        self.libray_table.column("Summery",width=100)
        self.libray_table.column("finalprice",width=100)
        
#+++++++++++++++++++++++++++++++
class StartLibrary:
    def __init__(self,root):
        self.root=root
        self.root.title("By Ahmed Abdel El Khaleq")
        self.root.geometry("600x300+0+0")
        
        
        lbltitle=Label(self.root,text="WELCOME IN LIBRARY",bg="powder blue",fg="green",bd=21,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue",)
        frame.place(x=0,y=130,width=600,height=670)
        
        #====================================== Button Frame ============================================
        
        Framebutton=Frame(self.root,bd=20,relief=RIDGE,padx=100,bg="powder blue",)
        Framebutton.place(x=0,y=100,width=600,height=670)
        

        btnAddData=Button(Framebutton,text=" Admin ",font=("arial",15,"bold"),
                          width=30,height=2,bg="green",fg="white",command=lambda:runaway(root))
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,text="Reader",font=("arial",15,"bold"),command=lambda:reed_action(root),
                          width=30,height=2,bg="green",fg="white")
        btnAddData.grid(row=1,column=0)
        
                    
def runaway(root):
    root.destroy()
    admain_dashbord()
   

    

def start_gate ():
    root=Tk()
    obj=StartLibrary(root)
    root.mainloop()
start_gate()





    
