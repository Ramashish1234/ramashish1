


from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

conn=mysql.connector.connect(host="localhost",username="root",password="Ashish@1553",database="bill_app")
my_cursor=conn.cursor()


class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Billing Software")


        lbl_title=Label(self.root,text="BILLIING SOFTWARE ",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=50,width=1400,height=45)


        main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        main_Frame.place(x=0,y=100,width=1360,height=620)


        self.var_Name=StringVar()
        self.var_mob=StringVar()
        self.var_email=StringVar()
        self.var_category=StringVar()
        self.var_Subcategory=StringVar()
        self.var_Product=StringVar()
        self.var_Price=StringVar()
        self.var_quantity=StringVar()
        self.var_Subtotal=StringVar()
        self.var_tax=StringVar()
        self.var_TotalAmount=StringVar()








        # customer labelframe
        Cust_Frame=LabelFrame(main_Frame,text="Customer", font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_Name=Label(Cust_Frame,text=" Customer Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Name.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_Name=ttk.Entry(Cust_Frame,textvariable=self.var_Name,font=("times new roman",12,"bold"),width=24)
        self.entry_Name.grid(row=0,column=1)

        self.lbl_mob=Label(Cust_Frame,text=" Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_Name=ttk.Entry(Cust_Frame,textvariable=self.var_mob,font=("times new roman",12,"bold"),width=24)
        self.entry_Name.grid(row=1,column=1)

        self.lbl_email=Label(Cust_Frame,text=" Email",font=("times new roman",12,"bold"),bg="white")
        self.lbl_email.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.entry_email=ttk.Entry(Cust_Frame,textvariable=self.var_email,font=("times new roman",12,"bold"),width=24)
        self.entry_email.grid(row=2,column=1)
        
        
         # Product labelframe
        Product_Frame=LabelFrame(main_Frame,text="Product", font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)
        
         # category
        self.lbl_category=Label(Product_Frame,text=" Select Category",font=("times new roman",12,"bold"),bg="white")
        self.lbl_category.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_category=ttk.Combobox(Product_Frame,value=self.categories,textvariable=self.var_category,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_category["value"]=(" Categories","Grocery","Clothes","Medicines","Mobiles")
        self.Combo_category.current(0)
        self.Combo_category.bind("<<ComboboxSelected>>",self.categories)

         # Subcategory
        self.lbl_Subcategory=Label(Product_Frame,text=" Sub Category",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Subcategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.Combo_Subcategory=ttk.Combobox(Product_Frame,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_Subcategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.Combo_Subcategory["value"]=(" Subcategories","Rice","oil","Vegetables","Pant","Shirt","TShirt","Syrup","Levocet","Chrocine","Iphone","Samsung","Redmi")
        self.Combo_Subcategory.current(0)
        
        #SubCatGrocery
        self.SubcatGrocery=["Rice","oil","Vegetables"]
        self.Rice=["Basmati","Moti","Chintu"]  
        self.price_Basmati=200
        self.price_Moti=150
        self.price_Chintu=100

        self.oil=["Sunflower","Mustard","Refined"]  
        self.price_Sunflower=200
        self.price_Mustard=250
        self.price_Refined=200

        self.Vegetables=["Potato","Onion","Tomato"]  
        self.price_Potato=20
        self.price_Onion=50
        self.price_Tomato=30

        

         #SubCatClothes
        self.SubcatClothes=["Pant","Shirt","TShirt"]
        self.Pant=["Nike","Levis","Mufti"]  
        self.price_Nike=2000
        self.price_Levis=5000
        self.price_Mufti=3000

        self.Shirt=["PEngland","Louis","Avenue"]  
        self.price_PEngland=20
        self.price_Louis=50
        self.price_Avenue=30

        self.TShirt=["Polo","Roadster","Jack"]  
        self.price_Polo=20
        self.price_Roadster=50
        self.price_Jack=30


        #SubCatMedicines
        self.SubcatMedicines=["Syrup","Levocet","Chrocine"]
        self.Syrup=["Syrup"]
        self.price_Syrup=500

        self.Syrup=["Levocet"]
        self.price_Levocet=200

        self.Chrocine=["Chrocine"]
        self.price_Chrocine=500


         #SubCatMobiles
        self.SubcatMobiles=["Iphone","Samsung","Redmi"]
        self.Iphone=["Iphone10","Iphone11","Iphone12"]
        self.price_10=50000
        self.price_11=70000
        self.price_12=90000

        self.Samsung=["SM16","SM12","SM21"]
        self.price_SM16=10000
        self.price_SM12=11000
        self.price_SM21=15000

        self.Redmi=["Redmi5","Redmi11","Redmi13"]
        self.price_Red5=15000
        self.price_Red11=18000
        self.price_Red13=20000







        

         # Product Name
        self.lbl_Product=Label(Product_Frame,text=" Product Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Product.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Combo_Product=ttk.Combobox(Product_Frame,value=[""],textvariable=self.var_Product,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_Product.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.Combo_Product["value"]=("Basmati","Moti","Chintu","Sunflower","Mustard","Refined","Potato","Onion","Tomato")        
        self.Combo_Subcategory.bind("<<ComboboxSelected>>",self.product_add)

         # Price
        self.lbl_Price=Label(Product_Frame,text=" Price",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Price.grid(row=0,column=2,stick=W,padx=5,pady=2)
        
        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.var_Price,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,stick=W,padx=5,pady=2)
        self.Combo_Price["value"]=(" MRP","100","120","140")
        
         # quantity
        self.lbl_quantity=Label(Product_Frame,text=" Quantity",font=("times new roman",12,"bold"),bg="white")
        self.lbl_quantity.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.Combo_quantity=ttk.Combobox(Product_Frame,textvariable=self.var_quantity,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.Combo_quantity.grid(row=1,column=3,stick=W,padx=5,pady=2)
        self.Combo_quantity["value"]=(" quantities","1x","2x","3x","4x","5x")
       

        

        #bill area
        RightlabelFrame=LabelFrame(main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightlabelFrame.place(x=1000,y=10,width=340,height=450)

        scroll_y=Scrollbar(RightlabelFrame,orient=VERTICAL)
        self.textarea=Text(RightlabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        
       
        self.textarea.pack(fill=BOTH,expand=1)
        
         # Bill Counter labelframe
        Bottom_Frame=LabelFrame(main_Frame,text="Bill Counter", font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=260,width=950,height=140)

        self.lbl_Subtotal=Label(Bottom_Frame,text=" Sub Total",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Subtotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntrySubtotal=ttk.Entry(Bottom_Frame,textvariable=self.var_Subtotal,font=("times new roman",10,"bold"),width=24)
        self.EntrySubtotal.grid(row=0,column=1,stick=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,text=" GST",font=("times new roman",12,"bold"),bg="white")
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.Entry_tax=ttk.Entry(Bottom_Frame,textvariable=self.var_tax,font=("times new roman",10,"bold"),width=24)
        self.Entry_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lbl_TotalAmount=Label(Bottom_Frame,text=" Total",font=("times new roman",12,"bold"),bg="white")
        self.lbl_TotalAmount.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Entry_TotalAmount=ttk.Entry(Bottom_Frame,textvariable=self.var_TotalAmount,font=("times new roman",10,"bold"),width=24)
        self.Entry_TotalAmount.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=500,y=0)

        self.BtnAddtoCart=Button(Bottom_Frame,text="Add to Cart",command=self.welcone_bill,font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnAddtoCart.grid(row=0,column=2)

        self.BtnGenerate_Bill=Button(Bottom_Frame,text="Generate Bill",font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnGenerate_Bill.grid(row=0,column=3)

        self.BtnSave=Button(Bottom_Frame,text="Save Bill",command=self.add_data,font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnSave.grid(row=0,column=4)
        
        self.BtnPrint=Button(Bottom_Frame,text="Bill Print",font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnPrint.grid(row=0,column=5)

        self.BtnClear=Button(Bottom_Frame,text="Clear",font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnClear.grid(row=0,column=6)

        self.BtnExit=Button(Bottom_Frame,text="Exit",font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnExit.grid(row=0,column=7)

        self.BtnQP=Button(Bottom_Frame,text="Subtotal",command=self.caluculate_Subtotal,font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnQP.grid(row=1,column=2)

        self.BtnSG=Button(Bottom_Frame,text="TOTAL",command=self.calculate_total,font=("times new roman",10,"bold"),height=2,width=15,bg="green",fg="white")
        self.BtnSG.grid(row=1,column=3)

        self.welcone_bill()

         # Bill Counter labelframe
        Bottom_Frame=LabelFrame(main_Frame,text="Bill Data", font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=460,width=1350,height=120)
        
        scroll_y=Scrollbar(Bottom_Frame,orient=VERTICAL)
        scroll_x=Scrollbar(Bottom_Frame,orient=HORIZONTAL)
        self.customertabel=Text(Bottom_Frame,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x,bg="white",fg="blue",font=("times new roman",12,"bold"))

        self.customertabel=ttk.Treeview(Bottom_Frame,column=("Name","Number","Email","Category","Subcategory","PName","Quantity","Price","SubTotal","GST","Total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.config(command=self.customertabel.yview)
        scroll_x.config(command=self.customertabel.xview)
        
        
        self.customertabel.heading("Name",text="Name")
        self.customertabel.heading("Number",text="Number")
        self.customertabel.heading("Email",text="Email")
        self.customertabel.heading("Category",text="Category")
        self.customertabel.heading("Subcategory",text="Subcategory")
        self.customertabel.heading("PName",text="PName")
        self.customertabel.heading("Quantity",text="Quantity")
        self.customertabel.heading("Price",text="Price")
        self.customertabel.heading("SubTotal",text="SubTotal")
        self.customertabel.heading("GST",text="GST")
        self.customertabel.heading("Total",text="Total")
        self.customertabel.pack(fill=BOTH,expand=1)
       
        self.customertabel["show"]="headings"

        self.customertabel.column("Name",width=100)
        self.customertabel.column("Number",width=100)
        self.customertabel.column("Email",width=100)
        self.customertabel.column("Category",width=100)
        self.customertabel.column("Subcategory",width=100)
        self.customertabel.column("PName",width=100)
        self.customertabel.column("Quantity",width=100)
        self.customertabel.column("Price",width=100)
        self.customertabel.column("SubTotal",width=100)
        self.customertabel.column("GST",width=100)
        self.customertabel.column("Total",width=100)
        
        self.textarea.pack(fill=BOTH,expand=1)
        self.show()

    def add_data(self):
        if (self.var_Name.get()=="" or self.var_mob.get()==""):
            messagebox.showerror("Error")
        else:
            try:
                
                query="INSERT INTO bill values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                a= (self.var_Name.get(),self.var_mob.get(),self.var_email.get(),self.var_category.get(),
                                                                                              self.var_Subcategory.get(),
                                                                                              self.var_Product.get(),
                                                                                              self.var_quantity.get(),
                                                                                              self.var_Price.get(),
                                                                                              self.var_Subtotal.get(),
                                                                                              self.var_tax.get(),
                                                                                              self.var_TotalAmount.get()
                                                                                           )
                my_cursor.execute(query,a)
                print(query)
                conn.commit()
                conn.close()
                messagebox.showinfo("success") 
                self.show()
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}", parent=self.root)                                                                          
        
    def show(self):
        try:
            query= "select * from bill;"
            my_cursor.execute(query)
            result = my_cursor.fetchall()

            self.customertabel.delete(*self.customertabel.get_children())
            for row in result:
                self.customertabel.insert('', END, value = row)
        except Exception as e:
            print(e)
            
    def categories(self,event=""):
        if self.Combo_category.get()=="Grocery":
            self.Combo_Subcategory.config(textvariable=self.SubcatGrocery)
            self.Combo_Subcategory.current(0)
            
        if self.Combo_category.get()=="Clothes":
            self.Combo_Subcategory.config(textvariable=self.SubcatClothes)
            self.Combo_Subcategory.current(0) 

        if self.Combo_category.get()=="Medicines":
            self.Combo_Subcategory.config(textvariable=self.SubcatMedicines)
            self.Combo_Subcategory.current(0)

        if self.Combo_category.get()=="Mobiles":
            self.Combo_Subcategory.config(textvariable=self.SubcatMobiles)
            self.Combo_Subcategory.current(0)    
    
    def product_add(self,event=""):
        if self.Combo_Subcategory.get()=="Pant":
            self.Combo_Product.config(Value=self.Pant)
            self.Combo_Product.current(0)

    
    
    
    
    def caluculate_Subtotal(self):
        self.value = self.var_Price.get()
        self.quan = self.var_quantity.get()

        total = int(self.value) * int(self.quan[0])
        self.EntrySubtotal.delete(0, END)
        self.EntrySubtotal.insert(0, total)
 
    
    def calculate_total(self):
        self.v1=self.var_Subtotal.get()
        self.v2=self.var_tax.get()

        total= int(self.v1) + int(self.v2)
        self.Entry_TotalAmount.delete(0, END)
        self.Entry_TotalAmount.insert(0, total)


    def welcone_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\t         ***WELCOME***")
        self.textarea.insert(END,f"\n===================================")
        self.textarea.insert(END,f"\n Customer Name: {self.var_Name.get()}")
        self.textarea.insert(END,f"\n Mob NO: {self.var_mob.get()}")
        self.textarea.insert(END,f"\n Email: {self.var_email.get()}")
        self.textarea.insert(END,f"\n===================================")
        self.textarea.insert(END,f"\nProducts\t\tQty\t\tPrice")
        self.textarea.insert(END,f"\n===================================")
        if self.var_quantity.get()!=0:
           self.textarea.insert(END,f"\n{self.var_Product.get()}\t\t{self.var_quantity.get()}\t\t{self.var_TotalAmount.get()}")
        

    def RightlabelFrame(self):
        self.welcone_bill()

if __name__ =='__main__':
    root=Tk()
    obj=bill_app(root)
    root.mainloop()