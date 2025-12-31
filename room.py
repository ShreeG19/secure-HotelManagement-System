from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1640x670+500+420")
        
       # =============== variable =============
        self.var_contact=StringVar()
        self.var_Check_in=StringVar()
        self.var_Check_out=StringVar()
        self.var_Room_type=StringVar()
        self.var_AvailableRoom=StringVar()
        self.var_Meal=StringVar()
        self.var_NoOfDays=StringVar()
        self.var_PaidTax=StringVar()
        self.var_SubTotal=StringVar()
        self.var_TotalCost=StringVar()
        
        
        #  ==================== title ====================
        lbl_title = Label(self.root,text="RoomBooking Details",font=("times new roman", 30, "bold"),bg="black",fg="gold",bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1640, height=60)
        
        #  ======================logo ======================
        img2 = Image.open("/home/kalilinux/Desktop/hotel_foxysDolphin/images/logo.png")
        img2 = img2.resize((100, 54), Image.Resampling.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lilimg = Label(self.root, image = self.photoimg2, bd=0.5, relief = RIDGE)
        lilimg.place(x=4, y=2, width=100, height=54)
        
        #  ======================lableFrame ======================
        lableFrameLeft=LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("times new roman", 20, "bold"), padx=2)
        lableFrameLeft.place(x=5, y=75, width=510, height=580)
        
        #  ======================lables and Entries ======================
        #customer_contact
        lbl_cust_contact=Label(lableFrameLeft, text="Customer Contact :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact=ttk.Entry(lableFrameLeft, textvariable=self.var_contact, font=("Arial", 14, "bold"), width = 15)
        enty_contact.grid(row=0, column=1, sticky=W, padx=0)
        
        # Fentch data button
        btnfetchData=Button(lableFrameLeft, text="Fetch Data", command=self.fetch_contact,  font=("Arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnfetchData.place(x=410, y=2)
        
        #check_in date
        check_in_date=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Check_in Date :", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date=ttk.Entry(lableFrameLeft, textvariable=self.var_Check_in, font=("Arial", 14, "bold"), width = 26)
        txtcheck_in_date.grid(row=1, column=1, sticky=W)
        
        #check_out date
        lbl_Check_out=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Check_out Date :", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txtcheck_out_date=ttk.Entry(lableFrameLeft, textvariable=self.var_Check_out, font=("Arial", 14, "bold"), width = 26)
        txtcheck_out_date.grid(row=2, column=1)
        
        #Room type
        lable_RoomType=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Room Type :", padx=2, pady=6)
        lable_RoomType.grid(row=3, column=0, sticky=W)
        
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        rooms = my_cursor.fetchall()
        
        combo_RoomType = ttk.Combobox(lableFrameLeft, textvariable=self.var_Room_type, font=("Arial", 14, "bold"), width=24, state="readonly")
        combo_RoomType["values"] = rooms 
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1, sticky=W)

        
        #Available Room
        lblRoomAvailable=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Available Room :", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        #txtRoomAvailable=ttk.Entry(lableFrameLeft, textvariable=self.var_AvailableRoom, font=("Arial", 14, "bold"), width = 26)
        #txtRoomAvailable.grid(row=4, column=1)
        
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()
        
        combo_RoomNo = ttk.Combobox(lableFrameLeft, textvariable=self.var_AvailableRoom, font=("Arial", 14, "bold"), width=24, state="readonly")
        combo_RoomNo["values"] = rows 
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1, sticky=W)
        
        #Meal
        lblMeal=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Meal :", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry(lableFrameLeft, textvariable=self.var_Meal, font=("Arial", 14, "bold"), width = 26)
        txtMeal.grid(row=5, column=1)
        
        #No of Days
        lblNoOfDays=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Number of Days :", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(lableFrameLeft, textvariable=self.var_NoOfDays, font=("Arial", 14, "bold"), width = 26)
        txtNoOfDays.grid(row=6, column=1)
        
        #Paid Tax
        lblNoOfDays=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Paid Tax :", padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(lableFrameLeft, textvariable=self.var_PaidTax, font=("Arial", 14, "bold"), width = 26)
        txtNoOfDays.grid(row=7, column=1)
        
        #Sub Total
        lblNoOfDays=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Sub Total :", padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(lableFrameLeft, textvariable=self.var_SubTotal, font=("Arial", 14, "bold"), width = 26)
        txtNoOfDays.grid(row=8, column=1)
        
        #Total cost
        lblIdNumber=Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Total cost :", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber=ttk.Entry(lableFrameLeft, textvariable=self.var_TotalCost, font=("Arial", 14, "bold"), width = 26)
        txtIdNumber.grid(row=9, column=1)
        
        # ======= bill button ============
        btnBill=Button(lableFrameLeft, text="Bill", command=self.total,  font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnBill.grid(row=10,column=0, padx=16, pady=15, sticky=W)
        
        # ==================== btns ==================
        btn_frame=Frame(lableFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=15, y=445, width=458, height=91)
        
        btnAdd=Button(btn_frame, text="Add", command=self.add_data,  font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnAdd.grid(row=0,column=0, padx=1)
        
        btnUpdate=Button(btn_frame, text="Update", command=self.update, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnUpdate.grid(row=0,column=1, padx=1)
        
        btnDelete=Button(btn_frame, text="Delete", command=self.mDelete, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnDelete.grid(row=1,column=0, padx=2)
        
        btnReset=Button(btn_frame, text="Reset", command=self.reset, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnReset.grid(row=1,column=1, padx=2)
        
        # ============= RightSide Image ==============        
        img3 = Image.open("/home/kalilinux/Desktop/hotel_foxysDolphin/images/room_img2.jpg")
        img3 = img3.resize((300, 220), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lilimg = Label(self.root, image=self.photoimg3, bd=0.5, relief=RIDGE)
        lilimg.place(x=900, y=65, width=280, height=220)
        
        img5 = Image.open("/home/kalilinux/Desktop/hotel_foxysDolphin/images/room_img1.jpg")
        img5 = img5.resize((300, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lilimg = Label(self.root, image=self.photoimg5, bd=0.5, relief=RIDGE)
        lilimg.place(x=1180, y=65, width=255, height=220)
        
        img4 = Image.open("/home/kalilinux/Desktop/hotel_foxysDolphin/images/room_img3.jpg")
        img4 = img4.resize((300, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lilimg = Label(self.root, image=self.photoimg4, bd=0.5, relief=RIDGE)
        lilimg.place(x=1435, y=65, width=200, height=220)

        
        # ==================== table frame search system ==================
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 20, "bold"), padx=2)
        Table_Frame.place(x=520, y=280, width=1110, height=375)
        
        lblSearchBy=Label(Table_Frame, text="Search Ref :", font=("Arial", 15, "bold"), bg="black", fg="gold")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("Arial", 15, "bold"),width=20, state="readonly")
        combo_search["value"]=("Contact Number", "Check-In Date")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("Arial", 14, "bold"), width = 26)
        txtSearch.grid(row=0, column=2, padx=2, pady=2)
        
        btnSearch=Button(Table_Frame, text="Search", command=self.search, font=("Arial", 14, "bold"), bg="black", fg="gold", width=8)
        btnSearch.grid(row=0,column=3, padx=1)
        
        btnShowAll=Button(Table_Frame, text="Show All", command=self.fetch_data, font=("Arial", 14, "bold"), bg="black", fg="gold", width=8)
        btnShowAll.grid(row=0,column=4, padx=1)
        
        # ==================== show table frame ==================
        detail_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=50, width=1100, height=293)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(detail_table,columns=("customer_contact", "Check_in", "Check_out", "Room_type","AvailableRoom", "Meal", "NoOfDays", 
                                                             "PaidTax", "SubTotal", "TotalCost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set
                                                     )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("customer_contact", text="Contact")
        self.room_table.heading("Check_in", text="Check-in")
        self.room_table.heading("Check_out", text="Check-out")
        self.room_table.heading("Room_type", text="Room Type")
        self.room_table.heading("AvailableRoom", text="Available Room")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("NoOfDays", text="No Of Days")
        self.room_table.heading("PaidTax", text="Paid Tax")
        self.room_table.heading("SubTotal", text="Sub Total")
        self.room_table.heading("TotalCost", text="Total Cost")

        self.room_table["show"] = "headings"

        self.room_table.column("customer_contact", width=100)
        self.room_table.column("Check_in", width=100)
        self.room_table.column("Check_out", width=100)
        self.room_table.column("Room_type", width=100)
        self.room_table.column("AvailableRoom", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("NoOfDays", width=100)
        self.room_table.column("PaidTax", width=100)
        self.room_table.column("SubTotal", width=100)
        self.room_table.column("TotalCost", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()
        
        # ===  add data  ===
    def add_data(self):
        if self.var_contact.get()=="" or self.var_Check_in.get()=="":
            messagebox.showerror("Error","All fields are manditory",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_contact.get(),
                                                                                  self.var_Check_in.get(),
                                                                                  self.var_Check_out.get(),
                                                                                  self.var_Room_type.get(),
                                                                                  self.var_AvailableRoom.get(),
                                                                                  self.var_Meal.get(),
                                                                                  self.var_NoOfDays.get(),
                                                                                  self.var_PaidTax.get(),
                                                                                  self.var_SubTotal.get(),
                                                                                  self.var_TotalCost.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been inserted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)
                
            # === fetch data ===
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        # === get curser ===
    def get_cuersor(self, event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_contact.set(row[0]),
        self.var_Check_in.set(row[1]),
        self.var_Check_out.set(row[2]),
        self.var_Room_type.set(row[3]),
        self.var_AvailableRoom.set(row[4]),
        self.var_Meal.set(row[5]),
        self.var_NoOfDays.set(row[6]),
        self.var_PaidTax.set(row[7]),
        self.var_SubTotal.set(row[8]),
        self.var_TotalCost.set(row[9])
        
    # ================== update ==================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s, Check_out=%s, Room_type=%s, AvailableRoom=%s, Meal=%s, NoOfDays=%s, PaidTax=%s, SubTotal=%s, TotalCost=%s where contact=%s",(
                                                                                                                                                                    
                                                                                                                                                                    self.var_Check_in.get(),
                                                                                                                                                                    self.var_Check_out.get(),
                                                                                                                                                                    self.var_Room_type.get(),
                                                                                                                                                                    self.var_AvailableRoom.get(),
                                                                                                                                                                    self.var_Meal.get(),
                                                                                                                                                                    self.var_NoOfDays.get(),
                                                                                                                                                                    self.var_PaidTax.get(),
                                                                                                                                                                    self.var_SubTotal.get(),
                                                                                                                                                                    self.var_TotalCost.get(),
                                                                                                                                                                    self.var_contact.get()
                                                                                                                                                                )) 
            conn.commit()
            self.fetch_data()
            conn.close()  
            messagebox.showinfo("Update","Memory Updated Sucessfully",parent=self.root)
            
    # === Delete ===
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete this customer", parent=self.root)
        if mDelete > 0 :
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query = "delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()
        
    # === Reset ===    
    
    def reset(self):
        self.var_contact.set(""),
        self.var_Check_in.set(""),
        self.var_Check_out.set(""),
        #self.var_Room_type.set(""),
        self.var_AvailableRoom.set(""),
        self.var_Meal.set(""),
        self.var_NoOfDays.set(""),
        self.var_PaidTax.set(""),
        self.var_SubTotal.set(""),
        self.var_TotalCost.set("")
            
    
    # ================ All data fetch ==============
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
        if row==None:
            messagebox.showerror("Error","This number not Found", parent=self.root)
        else:
            conn.commit()
            conn.close()
            
            showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showDataframe.place(x=510, y=65, width=385, height=215)
            
            lblName=Label(showDataframe, text="Name: ", font=("arial", 16, "bold"))
            lblName.place(x=0, y=0)
            lbl=Label(showDataframe, text=row, font=("arial", 16, "bold"))
            lbl.place(x=90, y=0)
            
            # gender
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query=("select Gender from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblGender=Label(showDataframe, text="Gender: ", font=("arial", 16, "bold"))
            lblGender.place(x=0, y=30)
            lbl2=Label(showDataframe, text=row, font=("arial", 16, "bold"))
            lbl2.place(x=90, y=30)
            
            # email
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query=("select email from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblEmail=Label(showDataframe, text="E-Mail: ", font=("arial", 16, "bold"))
            lblEmail.place(x=0, y=60)
            lbl3=Label(showDataframe, text=row, font=("arial", 16, "bold"))
            lbl3.place(x=90, y=60)
            
            # nationality
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query=("select nationality from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblNationality=Label(showDataframe, text="Nationality: ", font=("arial", 16, "bold"))
            lblNationality.place(x=0, y=90)
            lbl4=Label(showDataframe, text=row, font=("arial", 16, "bold"))
            lbl4.place(x=130, y=90)
            
            # ID-Proof
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query=("select id_proof from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lblid_proof=Label(showDataframe, text="ID Proof: ", font=("arial", 16, "bold"))
            lblid_proof.place(x=0, y=120)
            lbl5=Label(showDataframe, text=row, font=("arial", 16, "bold"))
            lbl5.place(x=100, y=120)
            
            # Address
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query=("select address from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            lbladdress=Label(showDataframe, text="Address: ", font=("arial", 16, "bold"))
            lbladdress.place(x=0, y=150)
            lbl6=Label(showDataframe, text=row, font=("arial", 16, "bold"))
            lbl6.place(x=100, y=150)
            
    # search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor = conn.cursor()
        # Map the combobox selection to actual column names in your DB
        column_map = {
            "contact Number": "Contact",
            "Check-In Date": "Check_in"
        }
        search_by = self.search_var.get()  
        column = column_map.get(search_by, "contact")  
        search_text = self.txt_search.get()
        
        query = f"SELECT * FROM room WHERE {column} LIKE %s OR Check_in LIKE %s"
        my_cursor.execute(query, ('%' + search_text + '%', '%' + search_text + '%'))
        
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
        
        conn.commit()
        conn.close()
        
    # ========== billing section for rooms and meals ========

    def total(self):
        inDate = self.var_Check_in.get()
        outDate = self.var_Check_out.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_NoOfDays.set(abs(outDate-inDate).days)
        
        if (self.var_Meal.get()=="Breakfast" and self.var_Room_type.get()=="Luxury"):
            q1=float(1000)
            q2=float(12000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Lunch" and self.var_Room_type.get()=="Luxury"):
            q1=float(2000)
            q2=float(12000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Dinner" and self.var_Room_type.get()=="Luxury"):
            q1=float(2000)
            q2=float(12000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Breakfast" and self.var_Room_type.get()=="Double"):
            q1=float(600)
            q2=float(8000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Lunch" and self.var_Room_type.get()=="Double"):
            q1=float(1000)
            q2=float(8000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
            
        elif (self.var_Meal.get()=="Dinner" and self.var_Room_type.get()=="Double"):
            q1=float(1000)
            q2=float(8000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Breakfast" and self.var_Room_type.get()=="Single"):
            q1=float(600)
            q2=float(4000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Lunch" and self.var_Room_type.get()=="Single"):
            q1=float(1000)
            q2=float(4000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="Dinner" and self.var_Room_type.get()=="Single"):
            q1=float(1000)
            q2=float(4000)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="-" and self.var_Room_type.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="-" and self.var_Room_type.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        elif (self.var_Meal.get()=="-" and self.var_Room_type.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_NoOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_PaidTax.set(Tax)
            self.var_SubTotal.set(ST)
            self.var_TotalCost.set(TT)
            
        else:
            messagebox.showerror("Error","If you do not whant to include meal plese fill '-' symbol",parent=self.root)
            

if __name__ ==  "__main__":
    root=Tk()
    obj= Roombooking(root)
    root.mainloop()