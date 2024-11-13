from tkinter import Button, Entry, Label, PhotoImage, Tk, Toplevel, messagebox
import MySQLdb
from tkinter import *
from PIL import Image


# Database connection
db = MySQLdb.connect("localhost", "root", "root", "bbms")
cursor = db.cursor()

# Main Tkinter window
root = Tk()
image1 = PhotoImage(file="1.gif")
panel = Label(root, image=image1, bg="antique white").place(x=0, y=0, relwidth=1, relheight=1)
root.title("BLOOD BANK")
root.geometry("1920x1080")
root.configure(background='white')


l3 = Label(root, text="BLOOD BANK SYSTEM", bg='white', font="Helvetica 15 bold").place(x=650, y=40, w=300, h=40)
l1 = Label(root, text="Click to enter the details of the donor", bg='white', font="Helvetica 12").place(x=80, y=100, w=300, h=40)
b1 = Button(root, text="Donor Details", command=lambda: donordetails()).place(x=80, y=150)
l2 = Label(root, text="Click to make a request for blood", bg='white', font="Helvetica 12").place(x=80, y=200, w=300, h=40)
b3 = Button(root, text="Blood Request", command=lambda: requestblood()).place(x=80, y=250)
b4 = Button(root, text="Exit", command=lambda: stop(root)).place(x=80, y=300)

v = StringVar() 


def insertDonor(name, age, gender, address, contactno, bloodgroup, platelet, rbc, quantity):
    if not name or not age or not gender:  
        messagebox.showerror("Error", "Please complete all required fields.")
        return
    
    insert = """
    INSERT INTO donors(name, age, gender, address, contactno, bloodgroup, platelet, rbc, quantity) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(insert, (name, age, gender, address, contactno, bloodgroup, platelet, rbc, quantity))
        db.commit()
        messagebox.showinfo("Success", "Donor details added successfully!")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Failed to add donor details: {e}")




def retrieve(bg):
    request = "SELECT * FROM donors WHERE bloodgroup='" + bg + "'"
    
    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        if not rows:
            print("No matching donors found.")
        db.commit()
        return rows
    except Exception as e:
        print("Error executing query:", e)
        db.rollback()


# Donor Details Window
# Donor Details Window with grid layout
def donordetails():
    donor_window = Toplevel()
    donor_window.title("BLOOD BANK")
    donor_window.geometry("480x580")
    donor_window.configure(background='#FF8F8F')

    # Labels for donor details
    Label(donor_window, text="Name:", bg='white', font="Helvetica 12").grid(row=0, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="Age:", bg='white', font="Helvetica 12").grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="Gender:", bg='white', font="Helvetica 12").grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="Address:", bg='white', font="Helvetica 12").grid(row=5, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="Contact:", bg='white', font="Helvetica 12").grid(row=6, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="BG:", bg='white', font="Helvetica 12").grid(row=7, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="Platelet:", bg='white', font="Helvetica 12").grid(row=8, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="RBC:", bg='white', font="Helvetica 12").grid(row=9, column=0, padx=10, pady=10, sticky='w')
    Label(donor_window, text="Quantity of Blood (ml):", bg='white', font="Helvetica 12").grid(row=10, column=0, padx=10, pady=10, sticky='w')

    # Entry fields for donor details
    e1 = Entry(donor_window)
    e1.grid(row=0, column=1, padx=10, pady=10)
    e2 = Entry(donor_window)
    e2.grid(row=1, column=1, padx=10, pady=10)
    r1 = Radiobutton(donor_window, text="Male", variable=v, value="Male", bg='#FF8F8F')
    r2 = Radiobutton(donor_window, text="Female", variable=v, value="Female", bg='#FF8F8F')
    r3 = Radiobutton(donor_window, text="Other", variable=v, value="Other", bg='#FF8F8F')
    r1.grid(row=2, column=1, sticky='w', padx=10, pady=5)
    r2.grid(row=3, column=1, sticky='w', padx=10, pady=5)
    r3.grid(row=4, column=1, sticky='w', padx=10, pady=5)
    e4 = Entry(donor_window)
    e4.grid(row=5, column=1, padx=10, pady=10)
    e5 = Entry(donor_window)
    e5.grid(row=6, column=1, padx=10, pady=10)
    e6 = Entry(donor_window)
    e6.grid(row=7, column=1, padx=10, pady=10)
    e7 = Entry(donor_window)
    e7.grid(row=8, column=1, padx=10, pady=10)
    e8 = Entry(donor_window)
    e8.grid(row=9, column=1, padx=10, pady=10)
    e9 = Entry(donor_window)
    e9.insert(0, "250")
    e9.grid(row=10, column=1, padx=10, pady=10)

    # Submit details function
    def submit_details():
        name = e1.get()
        age = e2.get()
        gender = v.get()
        address = e4.get()
        contactno = e5.get()
        bloodgroup = e6.get()
        platelet = e7.get()
        rbc = e8.get()
        quantity = e9.get()

        insertDonor(name, age, gender, address, contactno, bloodgroup, platelet, rbc, quantity)
        donor_window.destroy()

    # Submit button
    submit_button = Button(donor_window, text="Submit", command=submit_details)
    submit_button.grid(row=11, column=0, padx=10, pady=10)

    # Back button
    back_button = Button(donor_window, text="Back", command=lambda: stop(donor_window))
    back_button.grid(row=11, column=1, padx=10, pady=10)

# Function to display matching donors based on blood group
def grid1(bg):
    matching_donors_window = Toplevel()
    matching_donors_window.title("LIST OF MATCHING DONORS")
    matching_donors_window.geometry("750x500")
    matching_donors_window.configure(background='white')

    
    # Create a text box to display the availability message
    availability_text = Text(matching_donors_window, height=2, width=50, wrap='word', bg='lightgray')
    availability_text.insert(INSERT, "Searching for matching donors...")
    availability_text.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    rows = retrieve(bg)
    print("ROWS:",rows)
    if not rows:
        availability_text.delete(1.0, END)  # Clear the text box
        availability_text.insert(INSERT, "No matching donors found.")
    else:
        availability_text.delete(1.0, END)  # Clear the text box
        availability_text.insert(INSERT, "Matching donors found:")
    
    x = 1  
    
    for row in rows:
        Label(matching_donors_window, text=row[0], bg="white", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[1], bg="white", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[2], bg="white", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[3], bg="white", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[4], bg="white", font="Verdana 15 bold").grid(row=x, column=4, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[5], bg="white", font="Verdana 15 bold").grid(row=x, column=5, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)

        # Add "Confirm Order" button for each donor
        b = Button(matching_donors_window, text="Confirm Order", command=lambda donor=row[0]: confirm_order(donor))
        b.grid(row=x, column=6, padx=10, pady=10)
        x += 1


# Confirm Order window (with popup)
def confirm_order(donor_name):
    order_window = Toplevel()
    order_window.geometry("300x200")
    order_window.title("Confirm Order")

    message = f"Do you want to request blood from {donor_name}?"
    messagebox.showinfo("Order Confirmation", message)

    Button(order_window, text="Yes", command=lambda: donor_name(donor_name)).pack(pady=20)
    Button(order_window, text="No", command=order_window.destroy).pack(pady=20)


def requestblood():
    request_window = Tk()
    request_window.title("BLOOD REQUEST")
    request_window.geometry("520x320")
    request_window.configure(background='#FF8F8F')

   
    l1 = Label(request_window, text="Blood Group:", font="Helvetica 12").place(x=40, y=40, w=250, h=20)
    e1 = Entry(request_window)
    e1.place(x=350, y=40)

    # Submit button
    submit_button = Button(request_window, text="Submit", command=lambda: grid1(e1.get())).place(x=40, y=80)

    # Back button
    back_button = Button(request_window, text="Back", command=lambda: stop(request_window)).place(x=120, y=80)

    request_window.mainloop()



def stop(window):
    window.destroy()

root.mainloop()
