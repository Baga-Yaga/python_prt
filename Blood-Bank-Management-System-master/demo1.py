from tkinter import Button, Entry, Label, PhotoImage, Radiobutton, StringVar, Tk, Toplevel
import MySQLdb
from tkinter import *
from PIL import Image

#from demo import requestblood

# Database connection
db = MySQLdb.connect("localhost", "root", "root", "bbms")
cursor = db.cursor()

# Main Tkinter window
root = Tk()
image1 = PhotoImage(file="donation.gif")
panel = Label(root, image=image1, bg="black").place(x=0, y=0, relwidth=1, relheight=1)
root.title("BLOOD BANK")
root.geometry("1920x1080")
root.configure(background='white')

# Labels and Buttons for main window
l3 = Label(root, text="BLOOD BANK SYSTEM", bg='white', font="Helvetica 15 bold").place(x=450, y=40, w=300, h=40)
l1 = Label(root, text="Click to enter the details of the donor", bg='white', font="Helvetica 12").place(x=80, y=100, w=300, h=40)
b1 = Button(root, text="Donor Details", command=lambda: donordetails()).place(x=80, y=150)
l2 = Label(root, text="Click to make a request for blood", bg='white', font="Helvetica 12").place(x=80, y=200, w=300, h=40)
b3 = Button(root, text="Blood Request", command=lambda: requestblood()).place(x=80, y=250)
b4 = Button(root, text="Exit", command=lambda: stop(root)).place(x=80, y=300)

v = StringVar()  # For gender selection

# Function to insert donor details (including blood details) into the database
def insertDonor(name, age, gender, address, contactno, bloodgroup, platelet, rbc):
    insert = "INSERT INTO donors(name, age, gender, address, contactno, bloodgroup, platelet, rbc) VALUES('" + name + "', '" + age + "', '" + gender + "', '" + address + "', '" + contactno + "', '" + bloodgroup + "', '" + platelet + "', '" + rbc + "')"
    try:
        cursor.execute(insert)
        db.commit()
    except:
        db.rollback()

# Function to retrieve matching donors based on blood group
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
def donordetails():
    donor_window = Toplevel()
    donor_window.title("BLOOD BANK")
    donor_window.geometry("1024x768")
    donor_window.configure(background='#FF8F8F')

    # Labels for donor details
    l1 = Label(donor_window, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(donor_window, text="Age:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3 = Label(donor_window, text="Gender:", bg='white', font="Helvetica 12").place(x=40, y=120)
    l4 = Label(donor_window, text="Address:", bg='white', font="Helvetica 12").place(x=40, y=220)
    l5 = Label(donor_window, text="Contact:", bg='white', font="Helvetica 12").place(x=40, y=260)
    l6 = Label(donor_window, text="Blood Group:", bg='white', font="Helvetica 12").place(x=40, y=300)
    l7 = Label(donor_window, text="Platelet Count:", bg='white', font="Helvetica 12").place(x=40, y=340)
    l8 = Label(donor_window, text="RBC Count:", bg='white', font="Helvetica 12").place(x=40, y=380)

    # Entry fields for donor details
    e1 = Entry(donor_window)
    e1.place(x=120, y=40)
    e2 = Entry(donor_window)
    e2.place(x=120, y=80)
    r1 = Radiobutton(donor_window, text="Male", variable=v, value="Male").place(x=120, y=120)
    r2 = Radiobutton(donor_window, text="Female", variable=v, value="Female").place(x=120, y=150)
    r3 = Radiobutton(donor_window, text="Other", variable=v, value="Other").place(x=120, y=180)
    e4 = Entry(donor_window)
    e4.place(x=120, y=220)
    e5 = Entry(donor_window)
    e5.place(x=120, y=260)
    e6 = Entry(donor_window)
    e6.place(x=120, y=300)
    e7 = Entry(donor_window)
    e7.place(x=120, y=340)
    e8 = Entry(donor_window)
    e8.place(x=120, y=380)

    # Submit details function
    def submit_details():
        name = e1.get()
        age = e2.get()
        gender = v.get()  # Get selected gender
        address = e4.get()
        contactno = e5.get()
        bloodgroup = e6.get()
        platelet = e7.get()
        rbc = e8.get()

        # Call the insertDonor function to add donor details to the database
        insertDonor(name, age, gender, address, contactno, bloodgroup, platelet, rbc)
        donor_window.destroy()  # Close the donor details window after submitting

    # Submit button
    submit_button = Button(donor_window, text="Submit", command=submit_details).place(x=40, y=420)

    # Back button
    back_button = Button(donor_window, text="Back", command=lambda: stop(donor_window)).place(x=120, y=420)

# Function to display matching donors based on blood group
def grid1(bg):
    matching_donors_window = Tk()
    matching_donors_window.title("LIST OF MATCHING DONORS")
    matching_donors_window.geometry("750x500")
    matching_donors_window.configure(background='white')

    # Create a text box to display the availability message
    availability_text = Text(matching_donors_window, height=2, width=50, wrap='word', bg='lightgray')
    availability_text.insert(INSERT, "Searching for matching donors...")
    availability_text.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    rows = retrieve(bg)
    
    if not rows:
        availability_text.delete(1.0, END)  # Clear the text box
        availability_text.insert(INSERT, "No matching donors found.")
    else:
        availability_text.delete(1.0, END)  # Clear the text box
        availability_text.insert(INSERT, "Matching donors found:")

    # Now, display the donor details in the grid
    x = 1  # Start displaying donors after the availability message
    for row in rows:
        Label(matching_donors_window, text=row[0], bg="white", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[1], bg="white", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[2], bg="white", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        Label(matching_donors_window, text=row[3], bg="white", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
        x += 1

    matching_donors_window.mainloop()

def requestblood():
    request_window = Tk()
    request_window.title("BLOOD REQUEST")
    request_window.geometry("1024x768")
    request_window.configure(background='#FF8F8F')

    # Labels and Entry for blood group
    l1 = Label(request_window, text="Blood Group:", font="Helvetica 12").place(x=40, y=40, w=250, h=20)
    e1 = Entry(request_window)
    e1.place(x=350, y=40)

    # Submit button
    submit_button = Button(request_window, text="Submit", command=lambda: grid1(e1.get())).place(x=40, y=80)

    # Back button
    back_button = Button(request_window, text="Back", command=lambda: stop(request_window)).place(x=120, y=80)

    request_window.mainloop()

# To exit the program
def stop(window):
    window.destroy()

root.mainloop()
