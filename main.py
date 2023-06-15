from tkinter import *
from tkinter import messagebox as msg
import mysql.connector as sqlctr
from PIL import Image, ImageTk
from datetime import datetime as dt


class App(Tk):
    def __init__(self):
        # some Variables
        self.success = "Success | CodeWithVdr"
        self.error = "Error | CodeWithVdr"
        self.font = ("Courier New", 15, "bold")
        # Main Code
        self.root = Tk()
        # -----
        self.Wwidth = self.root.winfo_screenwidth()
        self.Wheight = self.root.winfo_screenheight()
        # -----
        self.root.title("XYZ Billing | CodeWithVdr")
        self.root.geometry(f"800x800")
        try:
            self.root.state('zoomed')
        except:
            print("User Using Ubuntu")
            self.root.attributes('-zoomed', True)
        self.root.minsize(750, 750)
        try:
            self.root.iconbitmap("assets/images/icon.ico")
        except:
            print("User Using Ubuntu")
        # For Backgound Image
        self.bgimg = Image.open("assets/images/bg.jpg")
        self.r_img = self.bgimg.resize((self.Wwidth, self.Wheight))
        self.backgroundImage = ImageTk.PhotoImage(self.r_img)
        self.bg = Label(self.root, image=self.backgroundImage, bd=0)
        self.bg.place(x=0, y=0)

        # Heading
        self.heading = Label(self.root, text="WELCOME TO XYZ BILLING", font=(
            "Courier New", 40, "bold"), relief=SOLID)
        self.heading.pack(pady=20)
        self.bk = Button(self.root, text="←Back", command=self._back,
                         font=self.font, cursor="left_side")  # Back Button
        # ***************************************************************************************************
        # =====================For Login==========================
        bcg = "gray"
        self.login = Frame(self.root, bd=5, height=600,
                           width=500, background=bcg)
        # --------------------For Logo-----------------------
        self.logo = Image.open("assets/images/icon.png")
        self.r_img = self.logo.resize((200, 200))
        self.logo = ImageTk.PhotoImage(self.r_img)
        self._logo = Button(self.login, image=self.logo, bd=0, background=bcg,
                            activebackground=bcg, command=self._redirect, cursor="hand2")
        self._logo.pack()
        #  --------------------------------------------------
        # Fields
        self.uid = StringVar()
        self.pw = StringVar()
        # ------------------For UID--------------------
        self.labelUid = Label(self.login, text="Enter UID : ",
                              font=self.font, background=bcg)
        self.labelUid.pack(pady=10, anchor=W)
        self.entryUID = Entry(self.login, textvariable=self.uid,
                              font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryUID.pack(pady=5)
        # ----------------------------------------------
        # ------------------For PW--------------------
        self.labelPw = Label(self.login, text="Enter Password : ",
                             font=self.font, background=bcg)
        self.labelPw.pack(pady=10, anchor=W)
        self.entryPw = Entry(self.login, textvariable=self.pw,
                             font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow", show="*")
        self.entryPw.pack(pady=5)
        # --------------------------------------------
        # ----------------For Button------------------
        self.loginSubmit = Button(self.login, text="Submit", font=self.font, width=30,
                                  relief=SOLID, activebackground="green", cursor="hand2", command=self._authenticate)
        self.loginSubmit.pack(pady=20)
        # --------------------------------------------

        self.login.pack(pady=50, anchor=CENTER)
        # ==========================ENDS==========================
        # ***************************************************************************************************

        # ***************************************************************************************************
        # ==========================HOME SCREEN===============================
        self.homeScreen = Frame(self.root, background=bcg)
        # ---------------------------------------------------------------------------------------
        self.op1 = Button(self.homeScreen, text="Store Products", font=self.font, width=30,
                          relief=SOLID, activebackground="greenyellow", cursor="hand2", command=self._storeProduct)
        self.op1.pack(pady=10, padx=10)
        # ---------------------------------------------------------------------------------------
        self.op2 = Button(self.homeScreen, text="See Available Products", font=self.font, width=30,
                          relief=SOLID, activebackground="greenyellow", cursor="hand2", command=self._seeAvailableProducts)
        self.op2.pack(pady=10, padx=10)
        # ---------------------------------------------------------------------------------------
        self.op3 = Button(self.homeScreen, text="Entry Of Sold Products", font=self.font, width=30,
                          relief=SOLID, activebackground="greenyellow", cursor="hand2", command=self._entrySoldProducts)
        self.op3.pack(pady=10, padx=10)
        # ---------------------------------------------------------------------------------------
        self.op4 = Button(self.homeScreen, text="See Sell History", font=self.font, width=30,
                          relief=SOLID, activebackground="greenyellow", cursor="hand2", command=self._seeSellHistory)
        self.op4.pack(pady=10, padx=10)
        # ---------------------------------------------------------------------------------------
        # ====================================================================
        # ***************************************************************************************************
        #                                           STORE PEODUCTS
        # ***************************************************************************************************
        self.stpd = Frame(self.root, background=bcg)
        # Scrollbar
        self.scrollbar = Scrollbar(self.stpd, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        # Fields
        # variables
        self.productId = StringVar()
        self.productName = StringVar()
        self.productMfg = StringVar()
        self.productExp = StringVar()
        self.productQty = StringVar()
        self.price = StringVar()
        # -------------------------PRODUCT ID----------------------------
        self.labelProductId = Label(self.stpd, text="Enter Product ID : ",
                                    font=self.font, background=bcg)
        self.labelProductId.pack(pady=5, anchor=W)
        self.entryProductId = Entry(self.stpd, textvariable=self.productId,
                                    font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProductId.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT NAME----------------------------
        self.labelProductName = Label(self.stpd, text="Enter Product Name : ",
                                      font=self.font, background=bcg)
        self.labelProductName.pack(pady=5, anchor=W)
        self.entryProductName = Entry(self.stpd, textvariable=self.productName,
                                      font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProductName.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT Mfg----------------------------
        self.labelProductMfg = Label(self.stpd, text="Enter Product Manufacture : ",
                                     font=self.font, background=bcg)
        self.labelProductMfg.pack(pady=5, anchor=W)
        self.entryProductMfg = Entry(self.stpd, textvariable=self.productMfg,
                                     font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProductMfg.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT Exp----------------------------
        self.labelProductExp = Label(self.stpd, text="Enter Product Expire : ",
                                     font=self.font, background=bcg)
        self.labelProductExp.pack(pady=5, anchor=W)
        self.entryProductExp = Entry(self.stpd, textvariable=self.productExp,
                                     font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProductExp.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT Qty----------------------------
        self.labelProductExp = Label(self.stpd, text="Enter Product Quantity : ",
                                     font=self.font, background=bcg)
        self.labelProductExp.pack(pady=5, anchor=W)
        self.entryProductExp = Entry(self.stpd, textvariable=self.productQty,
                                     font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProductExp.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRICE----------------------------
        self.labelPrice = Label(self.stpd, text="Enter Price : ",
                                font=self.font, background=bcg)
        self.labelPrice.pack(pady=5, anchor=W)
        self.entryPrice = Entry(self.stpd, textvariable=self.price,
                                font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryPrice.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------Button-----------------------------
        self.sub = Button(self.stpd, text="Submit", font=self.font, width=30,
                          relief=SOLID, activebackground="greenyellow", cursor="hand2", command=self._StoreData)
        self.sub.pack(pady=10, padx=10)
        # ------------------------------------------------------------
        # --------------------------FOR TIME--------------------------
        self.time = Label(self.root, text="", font=(
            "Courier", 19), background="yellow", fg="red", cursor="target")
        self.time.pack(side=TOP, anchor=NE)

        def time():
            try:
                self.time['text'] = (str(dt.now()).split(".")[0])
                self.root.after(1000, time)
            except:
                pass
        time()
        # ------------------------------------------------------------
        # ***************************************************************************************************
        #                                   SEE AVAILABLE PRODUCTS
        # ***************************************************************************************************
        self.sap = Frame(self.root, background=bcg)
        self.scrollbarTxtAreaY = Scrollbar(self.sap, orient='vertical')
        self.scrollbarTxtAreaY.pack(side=RIGHT, fill='y')
        self.scrollbarTxtAreaX = Scrollbar(self.sap, orient='horizontal')
        self.scrollbarTxtAreaX.pack(side=BOTTOM, fill="x")
        self.TxtArea = Text(self.sap, yscrollcommand=self.scrollbarTxtAreaY.set, xscrollcommand=self.scrollbarTxtAreaX.set, background="black",
                            fg="white", selectbackground="white", selectforeground="black", insertbackground="grey", font=self.font, width=100, height=50)
        self.scrollbarTxtAreaY.config(command=self.TxtArea.yview)
        self.scrollbarTxtAreaX.config(command=self.TxtArea.xview)
        self.TxtArea.pack()
        # ***************************************************************************************************
        #                                   Entry Sold Products
        # ***************************************************************************************************
        self.esp = Frame(self.root, background=bcg)
        # Variables
        self.ProductID = StringVar()
        self.ProductName = StringVar()
        self.QTY = IntVar()
        self.BuyerName = StringVar()
        # -------------------------PRODUCT ID----------------------------
        self.labelProduct = Label(self.esp, text="Enter Product ID : ",
                                  font=self.font, background=bcg)
        self.labelProduct.pack(pady=5, anchor=W)
        self.entryProduct = Entry(self.esp, textvariable=self.ProductID,
                                  font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProduct.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT Name----------------------------
        self.labelProduct = Label(self.esp, text="Enter Product Name : ",
                                  font=self.font, background=bcg)
        self.labelProduct.pack(pady=5, anchor=W)
        self.entryProduct = Entry(self.esp, textvariable=self.ProductName,
                                  font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProduct.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT Quantity----------------------------
        self.labelProduct = Label(self.esp, text="Enter Product QTY : ",
                                  font=self.font, background=bcg)
        self.labelProduct.pack(pady=5, anchor=W)
        self.entryProduct = Entry(self.esp, textvariable=self.QTY,
                                  font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProduct.pack(pady=5)
        # ------------------------------------------------------------
        # -------------------------PRODUCT Buyer Name----------------------------
        self.labelProduct = Label(self.esp, text="Enter Buyer Name : ",
                                  font=self.font, background=bcg)
        self.labelProduct.pack(pady=5, anchor=W)
        self.entryProduct = Entry(self.esp, textvariable=self.BuyerName,
                                  font=self.font, width=50, relief=SOLID, highlightthickness=2, highlightcolor="greenyellow")
        self.entryProduct.pack(pady=5)
        # ------------------------------------------------------------
        self.labelProduct.pack(pady=5, anchor=W)
        self.labelProductPrice = Label(
            self.esp, font=self.font, fg="red", background="yellow")
        self.labelProductPrice.pack(pady=5, anchor=E)
        self.sub = Button(self.esp, text="Submit", font=self.font, width=30,
                          relief=SOLID, activebackground="greenyellow", cursor="hand2", command=self._StoreSellData)
        self.sub.pack(pady=10, padx=10)
        # ------------------------------------------------------------
        # ***************************************************************************************************
        #                                   See Sell History
        # ***************************************************************************************************
        self.ssh = Frame(self.root, background=bcg)
        self.scrollbarTxtAreaY1 = Scrollbar(self.ssh, orient='vertical')
        self.scrollbarTxtAreaY1.pack(side=RIGHT, fill='y')
        self.scrollbarTxtAreaX1 = Scrollbar(self.ssh, orient='horizontal')
        self.scrollbarTxtAreaX1.pack(side=BOTTOM, fill="x")
        self.TxtArea1 = Text(self.ssh, yscrollcommand=self.scrollbarTxtAreaY1.set, xscrollcommand=self.scrollbarTxtAreaX1.set, background="black",
                             fg="white", selectbackground="white", selectforeground="black", insertbackground="grey", font=self.font, width=100, height=50)
        self.scrollbarTxtAreaY1.config(command=self.TxtArea1.yview)
        self.scrollbarTxtAreaX1.config(command=self.TxtArea1.xview)
        self.TxtArea1.pack()
        # ***************************************************************************************************

        self.root.mainloop()

    def _redirect(self):
        import webbrowser
        webbrowser.open("https://codevdr.github.io/v/index.html#contact")

    def _authenticate(self):
        with open("assets/crypt/data.crypt", "r") as f:
            content = f.read().split(",")
            if (content[0] == (self.uid.get()).lower() and content[1] == (self.pw.get()).lower()):
                msg.showinfo(self.success, "Log In Successful")
                # Setting Fields Value To null
                self.uid.set(""), self.pw.set("")
                self.login.pack_forget()  # For Removing login Details
                # Redirecting To Home Screen After Login
                self.homeScreen.pack(pady=50, anchor=CENTER)
            else:
                msg.showerror(self.error, "User Id or Password is Incorrect")
            f.close()

    def _back(self):
        self.heading['text'] = "Welcome To XYZ Billing"
        try:
            self.stpd.pack_forget(), self.bk.place_forget(
            ), self.sap.pack_forget(), self.esp.pack_forget(), self.ssh.pack_forget()
        except:
            pass
        self.homeScreen.pack()

    # Use Of MySQL From Here
    with open("assets/crypt/data1.crypt", "r") as f:
        content = f.read().split(",")
        global hs, us, pw
        hs, us, pw = content[0], content[1], content[2]
        f.close()
    global cs, cd, cur
    cs = sqlctr.connect(host=hs, user=us, password=pw)
    curCS = cs.cursor()
    curCS.execute("create database if not exists XYZ_Billing")
    cd = sqlctr.connect(host=hs, user=us, password=pw, database="XYZ_Billing")
    cur = cd.cursor()

    def _StoreData(self):  # Tested OK
        if (self.productId.get() == "" and self.productName.get() == "" and self.productMfg.get() == "" and self.productExp.get() == "" and self.productQty.get() == "" and self.price.get() == ""):
            msg.showerror(self.error, "Error! Fields Can't Be Empty")
        else:
            cur.execute("CREATE TABLE IF NOT EXISTS products(pid varchar(10),pname varchar(25),pmfg varchar(90),pexp varchar(90),pqty varchar(10),pprice varchar(10),storedOn varchar(90));")
            pid, pname, pmfg, pexp, pqty, pprice = self.productId.get(), self.productName.get(
            ), self.productMfg.get(), self.productExp.get(), self.productQty.get(), self.price.get()
            try:
                cur.execute(
                    f"insert into products values('{pid}','{pname}','{pmfg}','{pexp}','{pqty}','{pprice}','{str(dt.now()).split('.')[0]}');")
                msg.showinfo(
                    self.success, "Successfully Stored Data In Database")
                cd.commit()
            except:
                msg.showerror(
                    self.error, "Some Error Occured While Storing Data In Database")
        self.productId.set(""), self.productName.set(""), self.productMfg.set(
            ""), self.productExp.set(""), self.productQty.set(""), self.price.set("")

    def _storeProduct(self):
        self.homeScreen.pack_forget()
        self.heading['text'] = "Store Product"
        self.bk.place(x=10, y=10)
        self.stpd.pack(pady=50, anchor=CENTER, expand=True)

    def _seeAvailableProducts(self):  # Tested OK
        self.homeScreen.pack_forget()
        self.heading['text'] = "Available Products"
        self.bk.place(x=10, y=10)
        self.sap.pack(pady=50, anchor=CENTER)
        self.TxtArea.config(state="normal")
        self.TxtArea.delete("1.0", "end")
        self.TxtArea.insert(END, """#PID\t#PNAME\t\t#PMFG\t\t#PEXP\t\t#QTY\t#PPRICE\t\t#STORED ON           
=======================================================================================================================""")
        # My Sql Code
        cur.execute("select * from products;")
        res = cur.fetchall()
        for i in range(len(res)):
            pid, pname, pmfg, pexp, pqty, pprice, storedOn = res[i][0], res[
                i][1], res[i][2], res[i][3], res[i][4], res[i][5], res[i][6]
            self.TxtArea.config(state="normal")
            self.TxtArea.insert(
                END, f"\n{pid}\t{pname}\t\t{pmfg}\t\t{pexp}\t\t{pqty}\t{pprice}\t{storedOn}")

        self.TxtArea.config(state="disabled")

    def _entrySoldProducts(self):
        self.homeScreen.pack_forget()
        self.heading['text'] = "Entry Sold Product"
        self.bk.place(x=10, y=10)
        self.esp.pack(pady=50, anchor=CENTER)
     # Function of above one

    def _StoreSellData(self):  # Tested OK
        pid, pname, pqty, byrname = self.ProductID.get(
        ), self.ProductName.get(), self.QTY.get(), self.BuyerName.get()
        if pid == "" or pname == "" or pqty == 0 or byrname == "":
            msg.showerror(self.error, "Fields Can't Be Empty")
        else:
            cur.execute(
                "create table if not exists sale(pid varchar(20),pname varchar(50),pqty varchar(10),price varchar(10),byrname varchar(50),time varchar(90));")
            cur.execute(
                f"select * from products where pid='{pid}' && pname='{pname}';")
            res = cur.fetchall()
            if res == []:
                msg.showerror(self.error, "No Products Found")
            else:
                price = int(res[0][5])*pqty
                self.labelProductPrice['text'] = f"Total : ₹{price}"
                cur.execute(
                    f"insert into sale values('{pid}','{pname}','{pqty}','{price}','{byrname}','{str(dt.now()).split('.')[0]}');")
                cur.execute(
                    f"update products set pqty=pqty-{pqty} where pid='{pid}' && pname='{pname}';")
                cd.commit()
                self.ProductID.set(""), self.ProductName.set(
                    ""), self.QTY.set(0), self.BuyerName.set("")

    def _seeSellHistory(self):  # Tested OK
        try:
            cur.execute("select * from sale;")
            res = cur.fetchall()
            if res == []:
                msg.showinfo(self.success, "No Sale Yet")
            else:
                self.homeScreen.pack_forget()
                self.heading['text'] = "Sell History"
                self.bk.place(x=10, y=10)
                self.ssh.pack(pady=50, anchor=CENTER)
                self.TxtArea1.config(state="normal")
                self.TxtArea1.delete("1.0", "end")
                self.TxtArea1.insert(END, """#PID\t#PNAME\t\t#PQTY\t#PRICE\t#Buyer Name\t\t#SOLD ON         
=======================================================================================================================""")
                for i in range(len(res)):
                    pid, pname, pqty, price, byrname, dateT = res[i][0], res[
                        i][1], res[i][2], res[i][3], res[i][4], res[i][5]
                    self.TxtArea1.insert(
                        END, f"\n{pid}\t{pname}\t\t{pqty}\t{price}\t{byrname}\t\t{dateT}")
                self.TxtArea1.config(state="disabled")
        except:
            msg.showinfo(self.success, "No Sale Yet")


if __name__ == "__main__":
    App()
