from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1640x670+500+420")
        
        # ===================== variable =================
        self.var_ref = StringVar()
        x = random.randint(1000000,99999999)
        self.var_ref.set(str(x))
        
        self.var_cust_name = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()
   
   
        #  ==================== title ====================
        lbl_title = Label(self.root,text="Add Customer Details",font=("times new roman", 30, "bold"),bg="black",fg="gold",bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1640, height=60)
        
        #  ======================logo ======================
        img2 = Image.open("/home/kalilinux/Desktop/hotel_foxysDolphin/images/logo.png")
        img2 = img2.resize((100, 54), Image.Resampling.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lilimg = Label(self.root, image = self.photoimg2, bd=0.5, relief = RIDGE)
        lilimg.place(x=4, y=2, width=100, height=54)
        
        #  ======================lableFrame ======================
        lableFrameLeft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 20, "bold"), padx=2)
        lableFrameLeft.place(x=5, y=75, width=490, height=580)
        
        #  ======================lables and Entries ======================
        #cust_ref
        lbl_cust_ref=Label(lableFrameLeft, text="Customer Ref :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref=ttk.Entry(lableFrameLeft, textvariable=self.var_ref, font=("Arial", 14, "bold"), width = 26, state="readonly")
        enty_ref.grid(row=0, column=1)
        
        #cust name
        cname=Label(lableFrameLeft, text="Customer Name :", font=("Arial", 15, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname_ref=ttk.Entry(lableFrameLeft, textvariable=self.var_cust_name, font=("Arial", 14, "bold"), width = 26)
        txtcname_ref.grid(row=1, column=1)
        
        #gender combobox
        mname=Label(lableFrameLeft, text="Gender :", font=("Arial", 15, "bold"), padx=2, pady=6)
        mname.grid(row=2, column=0, sticky=W)
        
        combo_gender=ttk.Combobox(lableFrameLeft, textvariable=self.var_gender, font=("Arial", 15, "bold"),width=22, state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)
        
        #Post Code
        lblPostCode=Label(lableFrameLeft, text="Post Code :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=3, column=0, sticky=W)
        txtPostCode_ref=ttk.Entry(lableFrameLeft, textvariable=self.var_post, font=("Arial", 14, "bold"), width = 26)
        txtPostCode_ref.grid(row=3, column=1)
        
        #mobilenumber
        lblMobile=Label(lableFrameLeft, text="Mobile Number :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblMobile.grid(row=4, column=0, sticky=W)
        txtMobile_ref=ttk.Entry(lableFrameLeft, textvariable=self.var_mobile , font=("Arial", 14, "bold"), width = 26)
        txtMobile_ref.grid(row=4, column=1)
        
        #Email
        lblEmail=Label(lableFrameLeft, text="Email ID :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblEmail.grid(row=5, column=0, sticky=W)
        txtEmail_ref=ttk.Entry(lableFrameLeft, textvariable=self.var_email, font=("Arial", 14, "bold"), width = 26)
        txtEmail_ref.grid(row=5, column=1)
        
        #nationality
        lblNationality=Label(lableFrameLeft, text="Nationality :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblNationality.grid(row=6, column=0, sticky=W)
        
        combo_nationality=ttk.Combobox(lableFrameLeft, textvariable=self.var_nationality, font=("Arial", 15, "bold"),width=22, state="readonly")
        combo_nationality["value"]=("India","non-Indian")
        combo_nationality.current(0)
        combo_nationality.grid(row=6, column=1)
        
        #idproof type combobox
        lblIDproof=Label(lableFrameLeft, text="ID Proof :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblIDproof.grid(row=7, column=0, sticky=W)
        
        combo_id=ttk.Combobox(lableFrameLeft, textvariable=self.var_id_proof, font=("Arial", 15, "bold"),width=22, state="readonly")
        combo_id["value"]=("Aadhaar Card", "Passport", "ID card", "Driving Licence", "PAN Card")
        combo_id.current(0)
        combo_id.grid(row=7, column=1)
           
        #idnumber
        lblIDnumber=Label(lableFrameLeft, text="ID Number :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblIDnumber.grid(row=8 , column=0, sticky=W)
        txtIDnumber_ref=ttk.Entry(lableFrameLeft,textvariable=self.var_id_number , font=("Arial", 14, "bold"), width = 26)
        txtIDnumber_ref.grid(row=8 , column=1)

        #address
        lblIDnumber=Label(lableFrameLeft, text="Address :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lblIDnumber.grid(row=9, column=0, sticky=W)
        txtIDnumber_ref=ttk.Entry(lableFrameLeft, textvariable=self.var_address, font=("Arial", 14, "bold"), width = 26)
        txtIDnumber_ref.grid(row=9, column=1)
        
        # ==================== btns ==================
        btn_frame=Frame(lableFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=425, width=458, height=91)
        
        btnAdd=Button(btn_frame, text="Add",command=self.add_data,  font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnAdd.grid(row=0,column=0, padx=1)
        
        btnUpdate=Button(btn_frame, text="Update",command=self.update, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnUpdate.grid(row=0,column=1, padx=1)
        
        btnDelete=Button(btn_frame, text="Delete", command=self.mDelete, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnDelete.grid(row=1,column=0, padx=2)
        
        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnReset.grid(row=1,column=1, padx=2)
        
        # ==================== table frame search system ==================
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 20, "bold"), padx=2)
        Table_Frame.place(x=520, y=75, width=1110, height=580)
        
        lblSearchBy=Label(Table_Frame, text="Search Ref :", font=("Arial", 15, "bold"), bg="black", fg="gold")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("Arial", 15, "bold"),width=20, state="readonly")
        combo_search["value"]=("Mobile Number", "Ref Number")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("Arial", 14, "bold"), width = 26)
        txtSearch.grid(row=0, column=2, padx=2, pady=2)
        
        btnSearch=Button(Table_Frame, text="Search", command=self.search, font=("Arial", 18, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0,column=3, padx=1)
        
        btnShowAll=Button(Table_Frame, text="Show All", command=self.fetch_data, font=("Arial", 18, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0,column=4, padx=1)
        
        # ==================== show table frame ==================
        detail_table=Frame(Table_Frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=50, width=1100, height=493)
        scroll_x=ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table, orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(detail_table, column=("ref","name","gender","post","mobile","email","nationality",
                                                                    "id proof","id number","address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="Post Code")
        self.Cust_Details_Table.heading("mobile", text="Mobile No")
        self.Cust_Details_Table.heading("email", text="Email-ID")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("id proof", text="ID Proof")
        self.Cust_Details_Table.heading("id number", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("id proof",width=100)
        self.Cust_Details_Table.column("id number",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_id_number.get()=="" or self.var_address.get()=="" or self.var_gender.get()=="" or self.var_post.get()=="" or self.var_nationality.get()=="":
            messagebox.showerror("Error","All fields are manditory",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_ref.get(),
                                                                                  self.var_cust_name.get(),
                                                                                  self.var_gender.get(),
                                                                                  self.var_post.get(),
                                                                                  self.var_mobile.get(),
                                                                                  self.var_email.get(),
                                                                                  self.var_nationality.get(),
                                                                                  self.var_id_proof.get(),
                                                                                  self.var_id_number.get(),
                                                                                  self.var_address.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been inserted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)
                
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close
        
    def get_cuersor(self, event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_post.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationality.set(row[6]),
        self.var_id_proof.set(row[7]),
        self.var_id_number.set(row[8]),
        self.var_address.set(row[9])
    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, id_proof=%s, id_number=%s, address=%s where ref=%s",(
                                                                                                                                                                    
                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_ref.get()
                                                                                                                                                                )) 
            conn.commit()
            self.fetch_data()
            conn.close()  
            messagebox.showinfo("Update","Memory Updated Sucessfully",parent=self.root)
            
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete this customer", parent=self.root)
        if mDelete > 0 :
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query = "delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x = random.randint(1000000,99999999)
        self.var_ref.set(str(x))
   
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor = conn.cursor()
        # Map the combobox selection to actual column names in your DB
        column_map = {
            "Mobile Number": "mobile",
            "Ref Number": "ref"
        }
        search_by = self.search_var.get()  # e.g., "Mobile Number"
        column = column_map.get(search_by, "mobile")  # default to mobile if not found
        search_text = self.txt_search.get()
        
        query = f"SELECT * FROM customer WHERE {column} LIKE %s"
        my_cursor.execute(query, ('%' + search_text + '%',))
        
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
        
        conn.commit()
        conn.close()
 
if __name__ ==  "__main__":
    root=Tk()
    obj= Cust_Win(root)
    root.mainloop()