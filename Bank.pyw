'''Banking application by 

   K.Rishika(097) 

   K.Prasanna(093) 

   V.Goutham(072)''' 

 

from tkinter import Button, Label, Entry, messagebox, Tk, END, ttk, LabelFrame 

import sqlite3 

import datetime 

import time 

 

def withdraw(): 

    withdraw_window=Tk()             #withdraw window in tkinter 

    withdraw_window.title('Withdraw Money') 

     

    Label(withdraw_window ,text='Enter your Customer ID').grid(row=0,column=0,pady=10,padx=5)       #Customer ID Label 

    cust_id=Entry(withdraw_window ,text='Enter your Customer ID',width=30)     #ask for the customer id 

    cust_id.grid(row=0,column=1) 

    amount_label=Label(withdraw_window,text='Enter the amount to withdraw',font=('bold',10)) 

    amount=Entry(withdraw_window) 

 

    def withdraw_continue(): 

        cust_num=cust_id.get() 

        row=list(customer.execute('SELECT * FROM customer_info WHERE Customer_ID= ?',[cust_num])) 

        if len(row)>0: 

            amount_label.grid(row=1,column=0) 

            amount.grid(row=1,column=1) 

        else: 

            messagebox.showerror('No Customer found','Unable to find customer with this customer ID\nReturning to Menu') 

            withdraw_window.destroy() 

            return 

 

        def withdraw_continues():  

            messagebox.showwarning('Warning',f'You must have Rs. {amount.get()} in your account') 

            amt=int(amount.get()) 

            if row[0][7]>=amt: 

                customer.execute('UPDATE customer_info SET Balance=Balance-? WHERE Customer_ID=?',(amt,cust_num)) 

                found=True 

            else: 

                try: 

                    messagebox.showerror('Low Balance',"You don't have enough balance in your account") 

                except: 

                    pass 

            if found: 

                employee.execute('SELECT * FROM Bank_Data') 

                last_entry=list(employee.fetchall()[-1]) 

                last_entry[0]=datetime.datetime.now();last_entry[2]+=amt 

                employee.execute('INSERT INTO Bank_Data VALUES(?,?,?)',last_entry) 

                bank_data.commit() 

                customer_data.commit() 

                try: 

                    messagebox.showinfo('Withdraw Request','Amount withdrawn Successfully') 

                except: 

                    pass 

            withdraw_window.destroy() 

         

        Button(withdraw_window,text='Next',command=withdraw_continues).grid(row=1,column=2)     #Next Button 

     

    submit=Button(withdraw_window,text='Find Customer',command=withdraw_continue,padx=5) 

    submit.grid(row=0,column=2)    

 

 

def deposit(): 

    deposit_window=Tk()                      #deposit window in tkinter 

    deposit_window.title('Deposit Money') 

     

    Label(deposit_window ,text='Enter your Customer ID').grid(row=0,column=0,pady=10,padx=5)       #Customer ID Label 

    cust_id=Entry(deposit_window ,text='Enter your Customer ID',width=30)     #ask for the customer id 

    cust_id.grid(row=0,column=1) 

    amount_label=Label(deposit_window,text='Enter the amount to Deposit',font=('bold',10)) 

    amount=Entry(deposit_window) 

 

    def deposit_continue(): 

        cust_num=cust_id.get() 

        row=list(customer.execute('SELECT * FROM customer_info WHERE Customer_ID= ?',[cust_num])) 

        if len(row)>0: 

            amount_label.grid(row=1,column=0) 

            amount.grid(row=1,column=1) 

        else: 

            try: 

                messagebox.showerror('No Customer found','Unable to find customer with this customer ID\nReturning to Menu') 

            except:pass 

            deposit_window.destroy() 

            return 

 

        def deposit_continues():  

            found=False 

            amt=int(amount.get()) 

            customer.execute('UPDATE customer_info SET Balance=Balance+? WHERE Customer_ID=?',(amt,cust_num)) 

            found=True 

            if found: 

                employee.execute('SELECT * FROM Bank_Data') 

                last_entry=list(employee.fetchall()[-1]) 

                last_entry[0]=datetime.datetime.now();last_entry[2]+=amt 

                employee.execute('INSERT INTO Bank_Data VALUES(?,?,?)',last_entry) 

                bank_data.commit() 

                customer_data.commit() 

                try: 

                    messagebox.showinfo('Deposit Request','Amount deposited Successfully') 

                except: pass 

            deposit_window.destroy() 

         

        Button(deposit_window,text='Next',command=deposit_continues).grid(row=1,column=2)     #Next Button 

     

    submit=Button(deposit_window,text='Find Customer',command=deposit_continue,padx=5) 

    submit.grid(row=0,column=2)    

 

 

def transfer(): 

    transfer_window=Tk() 

    transfer_window.title('Money Transfer') 

     

    Label(transfer_window, text='Enter your Customer ID',pady=5,padx=5).grid(row=0,column=0)        #Customer ID sender Label 

    cust_id_sender=Entry(transfer_window) 

    cust_id_sender.grid(row=0,column=1,ipadx=50,padx=10) 

     

    Label(transfer_window, text='Enter the amount to Transfer').grid(row=1,column=0)        #Amount Label 

    Amount=Entry(transfer_window,) 

    Amount.grid(row=1,column=1,ipadx=50,padx=10) 

     

    Label(transfer_window, text='Enter the Customer ID of the Receiver').grid(row=2,column=0)           #Customer ID receiver Label 

    cust_id_receiver=Entry(transfer_window,) 

    cust_id_receiver.grid(row=2,column=1,ipadx=50,padx=10) 

 

    def transfer_continue(): 

        customer_id_sender=cust_id_sender.get() 

        customer_id_receiver=cust_id_receiver.get() 

        amount=int(Amount.get()) 

        found_sender=False 

        found_receiver=False 

        row_sender=list(customer.execute('SELECT * FROM customer_info WHERE Customer_ID=?',[customer_id_sender])) 

        if len(row_sender)>0: 

            found_sender=True 

            if found_sender: 

                row_receiver=list(customer.execute('SELECT * FROM customer_info WHERE Customer_ID=?',[customer_id_receiver])) 

                if len(row_receiver)>0: 

                    found_receiver=True 

            if not found_receiver: 

                try: 

                    messagebox.showerror('Receiver not fount','Customer not found with this customer ID') 

                except Exception as e: pass 

                transfer_window.destroy() 

                return 

        else: 

            try: 

                messagebox.showerror('No Customer found','Unable to find customer with this customer ID\nReturning to Menu') 

            except Exception as e: pass 

            transfer_window.destroy() 

            return 

                                                     

        if found_receiver: 

            if amount<=row_sender[0][7]: 

                customer.execute('UPDATE customer_info SET Balance=Balance-? WHERE Customer_ID=?',[amount,customer_id_sender]) 

                customer.execute('UPDATE customer_info SET Balance=Balance+? WHERE Customer_ID=?',[amount,customer_id_receiver]) 

                employee.execute('SELECT * FROM Bank_Data') 

                last_entry=list(employee.fetchall()[-1]) 

                last_entry[0]=datetime.datetime.now() 

                last_entry[2]=last_entry[2]+amount 

                employee.execute('INSERT INTO Bank_Data VALUES(?,?,?)',last_entry) 

                bank_data.commit() 

                customer_data.commit() 

                try: 

                    messagebox.showinfo('Withdraw Request','Money Transferred Successfully!!!') 

                except: pass 

            else: 

                try: 

                    messagebox.showerror('Insufficient Balance','Money Transfer cancelled due to Insufficient Balance') 

                except: pass 

        transfer_window.destroy() 

    Button(transfer_window, text='Next',bg='Green', padx=10,pady=5,command=transfer_continue).grid(row=3,column=0,columnspan=2,ipadx=70,pady=5) 

 

 

def balance(): 

    balance_window=Tk() 

    balance_window.title('Check Balance') 

    balance_window.geometry('600x112') 

     

    Label(balance_window, 

          text='Enter your customer ID below to check balance in your account:', 

          font=('bold',12), 

          pady=10).grid(row=0,column=0,columnspan=2)       #Heading 

 

    cust_id=Entry(balance_window, fg='grey',font=('bold',12)) 

    cust_id.grid(row=1,column=0,ipadx=120) 

 

    def balance_continue(): 

        customer_id=cust_id.get() 

        customer.execute('SELECT Balance FROM customer_info WHERE Customer_ID=?',(customer_id,)) 

        Balance=customer.fetchone() 

        if Balance!=None: 

            try: 

                messagebox.showinfo('Account Balance',f'Available Balance in your Account: Rs.{Balance[0]}') 

            except: pass 

            balance_window.destroy() 

            return 

        try: 

            messagebox.showerror('No Customer found','Unable to find customer with this customer ID\nReturning to Menu') 

        except: pass 

        balance_window.destroy() 

         

    submit=Button(balance_window, text='Check Balance',font=('bold',12),command=balance_continue) 

    submit.grid(row=2,column=0,pady=5) 

 

 

def Edit_details(): 

    update_window=Tk() 

    update_window.title('Update Customer Details') 

    update_window.geometry('600x112') 

     

    heading=Label(update_window, text='Enter your Customer ID:',font=('bold',12),pady=10) 

    heading.grid(row=0,column=0,columnspan=2) 

 

    cust_id=Entry(update_window, fg='grey',font=('bold',12)) 

    cust_id.grid(row=1,column=1,ipadx=150) 

     

    def Edit_details_continue(): 

        customer_id=cust_id.get() 

        cust_id.grid_remove() 

        submit.grid_remove() 

        heading.grid_remove() 

         

        update_window.geometry('420x200') 

        frame=LabelFrame(update_window,text='Fill your Details',bd=5,padx=10,pady=10) 

        frame.grid(row=0,column=0) 

         

        Label(frame, text='Name',font=('bold',10)).grid(row=1,column=0,padx=5)          #Name Label 

        name=Entry(frame,width=50,fg='grey') 

        Label(frame, text='Contact',font=('bold',10)).grid(row=2,column=0,padx=5)       #Contact Label 

        contact=Entry(frame,width=50,fg='grey') 

        Label(frame, text='State',font=('bold',10)).grid(row=3,column=0,padx=5)         #State Label 

        state=Entry(frame,fg='grey',width=50) 

        Label(frame, text='City',font=('bold',10)).grid(row=4,column=0,padx=5)          #City Label 

        city=Entry(frame,fg='grey',width=50) 

        Label(frame, text='Pincode',font=('bold',10)).grid(row=5,column=0,padx=5)       #Pincode Label 

        pincode=Entry(frame,fg='grey',width=50) 

        Label(frame, text='Email',font=('bold',10)).grid(row=6,column=0,padx=5)         #Email Label 

        email=Entry(frame,fg='grey',width=50) 

         

     

        trim=customer.execute('SELECT * FROM customer_info WHERE Customer_ID=?',(customer_id,)).fetchone() 

        if trim!=None: 

            details=[name,contact,state,city,pincode,email] 

            for  i in range(len(details)): 

                details[i].insert(END,trim[i+1]) 

            name.grid(row=1,column=1) 

            contact.grid(row=2,column=1) 

            state.grid(row=3,column=1) 

            city.grid(row=4,column=1) 

            pincode.grid(row=5,column=1) 

            email.grid(row=6,column=1) 

        else: 

            try: 

                messagebox.showerror('No Customer found','Unable to find customer with this customer ID\nReturning to Menu') 

            except: pass 

            update_window.destroy() 

            return 

 

        def Edit_details_continued():         

            customer.execute('UPDATE customer_info SET Name=?, Contact=?, State=?, City=?, Pincode=?, Email=? WHERE Customer_ID=?', 

                             (name.get(),contact.get(),state.get(),city.get(),pincode.get(),email.get(),customer_id)) 

            try: 

                messagebox.showinfo('Update Details','Your account details has been updates Successfully!!') 

            except: pass 

            update_window.destroy() 

            customer_data.commit() 

                 

         

        Button(frame,text='Submit',width=50,command=Edit_details_continued,bg='Green').grid(row=7,column=0,columnspan=2) 

     

    submit=Button(update_window, text='Find Customer',font=('bold',12),command=Edit_details_continue) 

    submit.grid(row=1,column=2,pady=5) 

 

 

def open_new_account(): 

    new_account=Tk() 

    new_account.title('Open New Account') 

     

    heading=Label(new_account,text='Fill Below details to open a new Account',font=('bold',14)) 

    heading.grid(row=0,column=1,columnspan=2,pady=5) 

     

    Label(new_account, text='Name',font=('bold',10)).grid(row=1,column=0,padx=5)        #Name Label 

    name=Entry(new_account, text='',width=50) 

    name.grid(row=1,column=1) 

    Label(new_account, text='Contact',font=('bold',10)).grid(row=2,column=0,padx=5)   #Contact Label 

    contact=Entry(new_account,width=50) 

    contact.grid(row=2,column=1) 

    Label(new_account, text='State',font=('bold',10)).grid(row=3,column=0,padx=5)       #State Label 

    state=Entry(new_account, text='',width=50) 

    state.grid(row=3,column=1) 

    Label(new_account, text='City',font=('bold',10)).grid(row=4,column=0,padx=5)        #City Label 

    city=Entry(new_account, text='',width=50) 

    city.grid(row=4,column=1) 

    Label(new_account, text='Pincode',font=('bold',10)).grid(row=5,column=0,padx=5)     #Pincode Label 

    pincode=Entry(new_account, text='',width=50) 

    pincode.grid(row=5,column=1) 

    Label(new_account, text='Email',font=('bold',10)).grid(row=6,column=0,padx=5)       #Email Label 

    email=Entry(new_account, text='',width=50) 

    email.grid(row=6,column=1) 

     

    employee.execute('SELECT * from Bank_Data') 

    bank_record=employee.fetchall() 

    last_entry=list(bank_record[-1]) 

    cust_id=int(last_entry[1])+ 43210 

 

    def process(): 

        new=(cust_id,name.get(),contact.get(),state.get(),city.get(),pincode.get(),email.get(),1000) 

        customer.execute('INSERT INTO customer_info VALUES(?,?,?,?,?,?,?,?)',new) 

        customer_data.commit() 

        messagebox.showinfo('New Account Opened',f"Your account has been created!!\nCustomer ID: {new[0]}")    

        last_entry[0]=datetime.datetime.now();last_entry[1]+=1 

        employee.execute('INSERT INTO Bank_Data VALUES(?,?,?)',last_entry) 

        bank_data.commit() 

        new_account.destroy() 

    Button(new_account,text='Submit',width=50,command=process).grid(row=7,column=0,columnspan=2)        #submit Button 

 

 

def home(): 

    root=Tk() 

    root.title('Banking Application') 

    root.geometry('500x450') 

    root.iconbitmap('anonymous.ico') 

    root.configure(bg='azure3') 

     

    m=Label(text='Welcome to PGR Bank',fg='White',bg='black',font=('bold',14),width=50) 

    m.grid(row=0,column=1,columnspan=4,pady=5) 

     

    new=Button(text='Apply For New Account',font=('bold',10),command=open_new_account) 

    new.grid(row=1,column=2,pady=10, padx=100) 

     

    withdraw_money=Button(text='Withdraw',font=('bold',10),command=withdraw) 

    withdraw_money.grid(row=3,column=2,pady=10,padx=100) 

     

    check_balance=Button(text='Check Balance',font=('bold',10),command=balance) 

    check_balance.grid(row=4,column=2,padx=100,pady=10) 

     

    deposit_money=Button(text='Deposit Money',font=('bold',10),command=deposit) 

    deposit_money.grid(row=5,column=2,padx=100,pady=10) 

     

    update=Button(text='Update Your Details',font=('bold',10),command=Edit_details) 

    update.grid(row=6,column=2,pady=10,padx=100) 

     

    acc_transfer=Button(text='Transfer Money',font=('bold',10),command=transfer) 

    acc_transfer.grid(row=7,column=2,pady=10,padx=100) 

     

    Exit=Button(text='Exit',font=('bold',10),command=root.destroy,width=6) 

    Exit.grid(row=8,column=2,pady=10,padx=100) 

    #need to add exit and confirmation dialog 

    root.mainloop() 

 

if __name__ == '__main__': 

    customer_info=['Customer ID','Name','Contact','State','City','Pincode','Email','Balance'] 

    customer_data=sqlite3.connect("customer.db") 

    customer=customer_data.cursor() 

    customer.execute('''CREATE TABLE IF NOT EXISTS customer_info( 

                        Customer_ID integer, 

                        Name text,  

                        Contact integer,  

                        State text, 

                        City text, 

                        Pincode integer,  

                        Email text,  

                        Balance integer 

                        )''') 

 

    customer.execute('SELECT * FROM customer_info') 

    bank_data=sqlite3.connect("BankData.db") 

    employee=bank_data.cursor() 

    employee.execute('''CREATE TABLE IF NOT EXISTS Bank_Data( 

                      Date text, 

                      Customer_count integer, 

                      Transactions integer   

                        )''') 

    employee.execute('SELECT * FROM Bank_Data') 

    records=employee.fetchall() 

    if len(records)<1: 

        employee.execute('INSERT INTO Bank_Data VALUES(0,0,0)') 

        bank_data.commit() 

 

 

    home() 
