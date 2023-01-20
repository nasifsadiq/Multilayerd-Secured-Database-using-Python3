# Importing all modules
from tkinter import *
import os
import random
import smtplib
import sqlite3

# ===========================================================================================================================
# ===========================================================================================================================

# Below part is Database

def database():
    root = Tk()
    root.title("Employee Address Book")
    root.geometry("400x700")
    # Create a database or connect one
    conn = sqlite3.connect('employee_address_book.db')

    # Create cursor instance
    c = conn.cursor()
    '''
    # Create Table
    c.execute("""CREATE TABLE addresses (
                first_name text,
                last_name text,
                phonenumber integer,
                address text,
                city text,
                zipcode integer
                )""")

    '''

    # Create Edit Function to update A record
    def update():
        # Create a database or connect one
        conn = sqlite3.connect('employee_address_book.db')

        # Create cursor instance
        c = conn.cursor()
        record_id = delete_box.get()
        c.execute("""UPDATE addresses SET
        		first_name = :first,
        		last_name = :last,
        		phonenumber= :phonenumber,
        		address = :address,
        		city = :city,
        		zipcode = :zipcode
        		WHERE oid = :oid""",
                  {
                      'first': f_name_editor.get(),
                      'last': l_name_editor.get(),
                      'phonenumber': phonenumber_editor.get(),
                      'address': address_editor.get(),
                      'city': city_editor.get(),
                      'zipcode': zipcode_editor.get(),
                      'oid': record_id
                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        editor.destroy()

    def edit():
        global editor
        editor = Tk()
        editor.title("Update A Record")
        editor.geometry("400x300")

        # Create a database or connect one
        conn = sqlite3.connect('employee_address_book.db')

        # Create cursor instance
        c = conn.cursor()
        record_id = delete_box.get()
        # Query the database
        c.execute("SELECT * FROM addresses WHERE oid =" + record_id)
        records = c.fetchall()

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()
        # Create Global Variables for text box names
        global f_name_editor
        global l_name_editor
        global phonenumber_editor
        global address_editor
        global city_editor
        global zipcode_editor
        # Create text boxes

        f_name_editor = Entry(editor, width=40)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

        l_name_editor = Entry(editor, width=40)
        l_name_editor.grid(row=1, column=1)

        phonenumber_editor = Entry(editor, width=40)
        phonenumber_editor.grid(row=2, column=1)

        address_editor = Entry(editor, width=40)
        address_editor.grid(row=3, column=1)

        city_editor = Entry(editor, width=40)
        city_editor.grid(row=4, column=1)

        zipcode_editor = Entry(editor, width=40)
        zipcode_editor.grid(row=5, column=1)

        # Create Text Box Labels
        f_name_label = Label(editor, text="First Name")
        f_name_label.grid(row=0, column=0, pady=(10, 0))

        l_name_label = Label(editor, text="Last Name")
        l_name_label.grid(row=1, column=0)

        phonenumber_label = Label(editor, text="Phone Number")
        phonenumber_label.grid(row=2, column=0)

        address_label = Label(editor, text="Address")
        address_label.grid(row=3, column=0)

        city_label = Label(editor, text="City")
        city_label.grid(row=4, column=0)

        zipcode_label = Label(editor, text="Zip Code")
        zipcode_label.grid(row=5, column=0)

        # Loop through results
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            phonenumber_editor.insert(0,"0"+ str(record[2]))
            address_editor.insert(0, record[3])
            city_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        # Create save button to save edited record
        edit_btn = Button(editor, text="Save Record", command=update)
        edit_btn.grid(row=6, column=0, columnspan=2, pady=(10, 0), padx=10, ipadx=130)

    # Create Function to Delete A Record

    def delete():
        # Create a database or connect one
        conn = sqlite3.connect('employee_address_book.db')

        # Create cursor instance
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    # Create submit function for database
    def submit():
        # Create a database or connect one
        conn = sqlite3.connect('employee_address_book.db')

        # Create cursor instance
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :phonenumber, :address, :city, :zipcode)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'phonenumber': phonenumber.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'zipcode': zipcode.get()
                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        # Clear Text Fields
        f_name.delete(0, END)
        l_name.delete(0, END)
        phonenumber.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        zipcode.delete(0, END)

    def query():

        # Create a database or connect one
        conn = sqlite3.connect('employee_address_book.db')

        # Create cursor instance
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *,oid FROM addresses")
        records = c.fetchall()
        # print(records)

        # Loop through results
        print_records = ""
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\t0" + str(record[2]) + "\t" + str(
                record[3]) + ", " + str(record[4]) + "-" + str(record[5]) + "\t" + str(record[6]) + "\n"

        header_label = Label(root, text="Name\t\tPhone Number\tFull Address\t\tID")
        header_label.grid(row=11, column=0, columnspan=2)

        query_label = Label(root, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    # Create text boxes

    f_name = Entry(root, width=40)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name = Entry(root, width=40)
    l_name.grid(row=1, column=1)

    phonenumber = Entry(root, width=40)
    phonenumber.grid(row=2, column=1)

    address = Entry(root, width=40)
    address.grid(row=3, column=1)

    city = Entry(root, width=40)
    city.grid(row=4, column=1)

    zipcode = Entry(root, width=40)
    zipcode.grid(row=5, column=1)

    delete_box = Entry(root, width=40)
    delete_box.grid(row=8, column=1, pady=5)

    # Create Text Box Labels
    f_name_label = Label(root, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(root, text="Last Name")
    l_name_label.grid(row=1, column=0)

    phonenumber_label = Label(root, text="Phone Number")
    phonenumber_label.grid(row=2, column=0)

    address_label = Label(root, text="Address")
    address_label.grid(row=3, column=0)

    city_label = Label(root, text="City")
    city_label.grid(row=4, column=0)

    zipcode_label = Label(root, text="Zip Code")
    zipcode_label.grid(row=5, column=0)

    delete_box_label = Label(root, text="Select ID")
    delete_box_label.grid(row=8, column=0, pady=5)

    # Create Submit Button
    submit_btn = Button(root, text="Add Record To Database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=(10, 0), padx=10, ipadx=100)

    # Create a Query Button
    query_btn = Button(root, text="Show Records", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

    # Create a Delete Button
    delete_btn = Button(root, text="Delete Record", command=delete)
    delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

    # Create a Update Button
    edit_btn = Button(root, text="Edit Record", command=edit)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=(0, 10), padx=10, ipadx=135)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    root.mainloop()

# ===========================================================================================================================
# ===========================================================================================================================


# ===========================================================================================================================
# ===========================================================================================================================

# Below part is for Registration/Sign in/Authentication/

# ===========================================================================================================================
# ===========================================================================================================================


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=signUp_otp).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing Sign Up OTP Screen
def signUp_otp():
    global signUp_otp_screen
    signUp_otp_screen = Toplevel(register_screen)
    signUp_otp_screen.title("OTP")
    signUp_otp_screen.geometry("300x250")
    Label(signUp_otp_screen, text="Ask OTP from below to sign up").pack()
    Label(signUp_otp_screen, text="").pack()
    global signUp_otp_verify

    signUp_otp_verify = StringVar()
    signUp_otp_verify.set("")

    global otp_signup_entry
    Label(signUp_otp_screen, text="OTP * ").pack()
    otp_signup_entry = Entry(signUp_otp_screen, textvariable=signUp_otp_verify)
    otp_signup_entry.pack()

    Label(signUp_otp_screen, text="").pack()
    Button(signUp_otp_screen, text="Enter", width=10, height=1, command=otp_signUp_match_verify).pack()
    otp_for_signup()


# Implementing OTP Screen
def otp():
    global otp_screen
    otp_screen = Toplevel(login_screen)
    otp_screen.title("OTP")
    otp_screen.geometry("300x250")
    Label(otp_screen, text="Please enter OTP below to login").pack()
    Label(otp_screen, text="").pack()
    global otp_verify

    otp_verify = StringVar()
    otp_verify.set("")

    global otp_login_entry
    Label(otp_screen, text="OTP * ").pack()
    otp_login_entry = Entry(otp_screen, textvariable=otp_verify)
    otp_login_entry.pack()

    Label(otp_screen, text="").pack()
    Button(otp_screen, text="Enter", width=10, height=1, command=otp_match_verify).pack()
    otp_for_signin()


# Generating OTP for sign up
def otp_for_signup():
    global signup_otp
    global username_info
    username_info = username.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('botsemail(gmail)', 'password') #Replace these
    signup_otp = random.randint(100000, 999999)
    TEXT = f"Someone with email: '{username_info}' is trying to signup on your database system.\nIf you want to give him access forward this messesge to him or send the following OTP you the new user.\n OTP: {signup_otp}"
    SUBJECT = "Security Warning on Database Access!"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.sendmail('botsemail(gmail)', "adminsemail",
                    message)  # Admin mail is the second parameter


# Generating OTP for sign in
def otp_for_signin():
    global actual_otp
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('email(gmail)', 'password') #Replace these
    actual_otp = random.randint(100000, 999999)
    TEXT = f"Enter the otp for signing in into Database of your empoloyee: {actual_otp}"
    SUBJECT = "Database Sign in OTP"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.sendmail('botsemail(gmail)', username1, message)


# Implementing event on login button

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# OTP Verification

def otp_signUp_match_verify():
    signUp_otp1 = signUp_otp_verify.get()
    otp_signup_entry.delete(0, END)

    if int(signUp_otp1) == signup_otp:
        otp_sucess_signup()

    else:
        otp_for_signup()
        signup_otp_not_recognised()


# OTP Verification

def otp_match_verify():
    otp1 = otp_verify.get()
    otp_login_entry.delete(0, END)

    if int(otp1) == actual_otp:
        otp_sucess()

    else:
        otp_for_signin()
        otp_not_recognised()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Password Matched").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for otp success signup

def otp_sucess_signup():
    global otp_success_signup_screen
    otp_success_signup_screen = Toplevel(signUp_otp_screen)
    otp_success_signup_screen.title("Success")
    otp_success_signup_screen.geometry("250x200")
    Label(otp_success_signup_screen, text="OTP Matched. Registration Successful").pack()
    Button(otp_success_signup_screen, text="OK", command=delete_otp_success_signup).pack()
    register_user()


# Designing popup for otp success

def otp_sucess():
    global otp_success_screen
    otp_success_screen = Toplevel(otp_screen)
    otp_success_screen.title("Success")
    otp_success_screen.geometry("250x200")
    Label(otp_success_screen, text="OTP Matched. Login Successful").pack()
    Button(otp_success_screen, text="OK", command=delete_otp_success).pack()


# Designing popup for login invalid OTP
def signup_otp_not_recognised():
    global signup_otp_not_recog_screen
    signup_otp_not_recog_screen = Toplevel(otp_screen)
    signup_otp_not_recog_screen.title("Success")
    signup_otp_not_recog_screen.geometry("150x100")
    Label(signup_otp_not_recog_screen, text="Invalid OTP ").pack()
    Button(signup_otp_not_recog_screen, text="OK", command=delete_signup_otp_not_recognised).pack()


# Designing popup for login invalid OTP
def otp_not_recognised():
    global otp_not_recog_screen
    otp_not_recog_screen = Toplevel(otp_screen)
    otp_not_recog_screen.title("Success")
    otp_not_recog_screen.geometry("150x100")
    Label(otp_not_recog_screen, text="Invalid OTP ").pack()
    Button(otp_not_recog_screen, text="OK", command=delete_otp_not_recognised).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def distroy_all():
    login_screen.destroy()
    otp_screen.destroy()


def delete_login_success():
    otp()
    login_success_screen.destroy()


def delete_otp_success_signup():
    otp_success_signup_screen.destroy()
    register_screen.destroy()


def delete_otp_success():
    distroy_all()
    otp_success_screen.destroy()
    main_screen.destroy()
    database()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_otp_not_recognised():
    otp_not_recog_screen.destroy()


def delete_signup_otp_not_recognised():
    signup_otp_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x400")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
