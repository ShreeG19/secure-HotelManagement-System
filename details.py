from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1640x670+500+420")

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
        lableFrameLeft=LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Details", font=("times new roman", 20, "bold"), padx=2)
        lableFrameLeft.place(x=5, y=75, width=700, height=450)
        
        #  ======================lables and Entries ======================
        #Floor
        lbl_floor=Label(lableFrameLeft, text="Floor :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        
        self.var_floor=StringVar()
        enty_floor=ttk.Entry(lableFrameLeft, textvariable=self.var_floor, font=("Arial", 14, "bold"), width = 15)
        enty_floor.grid(row=0, column=1, sticky=W, padx=0)
        
        #Room No
        lbl_RoomNo=Label(lableFrameLeft, text="RoomNo :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomno=StringVar()
        enty_RoomNo=ttk.Entry(lableFrameLeft, textvariable=self.var_roomno, font=("Arial", 14, "bold"), width = 15)
        enty_RoomNo.grid(row=1, column=1, sticky=W, padx=0)
        
        #Room Type
        lbl_RoomType=Label(lableFrameLeft, text="RoomType :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_roomtype=StringVar()
        enty_RoomType=ttk.Entry(lableFrameLeft, textvariable=self.var_roomtype, font=("Arial", 14, "bold"), width = 15)
        enty_RoomType.grid(row=2, column=1, sticky=W, padx=0)

        # ==================== btns ==================
        btn_frame=Frame(lableFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=105, y=285, width=458, height=91)
        
        btnAdd=Button(btn_frame, text="Add", command=self.add_data, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnAdd.grid(row=0,column=0, padx=1)
        
        btnUpdate=Button(btn_frame, text="Update", command=self.update, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnUpdate.grid(row=0,column=1, padx=1)
        
        btnDelete=Button(btn_frame, text="Delete", command=self.mDelete, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnDelete.grid(row=1,column=0, padx=2)
        
        btnReset=Button(btn_frame, text="Reset", command=self.reset, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnReset.grid(row=1,column=1, padx=2)
        
        # ==================== table frame search system ==================
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("times new roman", 20, "bold"), padx=2)
        Table_Frame.place(x=720, y=75, width=900, height=450)
        
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame,columns=("floor", "roomno", "roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set
                                                     )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="RoomNumber")
        self.room_table.heading("roomtype", text="RoomType")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()

    # ===  add data  ===
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are manditory",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                        self.var_floor.get(),
                                                        self.var_roomno.get(),
                                                        self.var_roomtype.get()
                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)
                
    # === fetch data ===
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cuersor(self, event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])
        
    # ================== update ==================
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter RoomNumber Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s, roomtype=%s where roomno=%s",(
                                                                                                                                                                    
                                                            self.var_floor.get(),
                                                            self.var_roomtype.get(),
                                                            self.var_roomno.get()
                                                    )) 
            conn.commit()
            self.fetch_data()
            conn.close()  
            messagebox.showinfo("Update","Memory Updated Sucessfully",parent=self.root)
            
    # === Delete ===
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete this Room Details", parent=self.root)
        if mDelete > 0 :
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor=conn.cursor()
            query = "delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()
        
    # === Reset ===    
    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set(""),





if __name__ ==  "__main__":
    root=Tk()
    obj= DetailsRoom(root)
    root.mainloop()