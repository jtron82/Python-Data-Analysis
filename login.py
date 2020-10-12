# imports
from tkinter import *
from tkinter import messagebox as msg
import sqlite3
import matplotlib.pyplot as plt 
from data import *
import time

# name
print("Final Project - Read in Data Over the Web, Plot and Show Data Analysis Results by Jimmy Tran")

print()

# mm/dd/yy format with current time in military time
print ("Date:", time.strftime("%x"))
print ("Current time:", time.strftime("%X"))

# main class
class main:
    # constructor
    def __init__(self,master):
        self.master = master
        self.usersname = StringVar()
        self.password = StringVar()

    # login method
    def login(self):
    	# database connection
        with sqlite3.connect('mydb.db') as db:
            c = db.cursor()

        # query statement for credential verification
        find_users = ('SELECT * FROM users WHERE uname = ? and upass = ?')
        c.execute(find_users,[(self.usersname.get()),(self.password.get())])
        result = c.fetchall()
        self.widgets()

        # if statement for successful user login
        if result:
            self.crf = Frame(self.master, padx=0, pady=0, height=800)
            
            self.head['text'] = 'Currently Logged in as: ' + self.usersname.get()
            self.head['pady'] = 5  
            self.head.pack()

            Label(self.crf, text='Choose Which Graph to Display', font=('',25), pady=15, padx=5).grid()
            Label(self.crf, text="Bar Chart Shows Top 5 Crimes in Pre-Designated Area", font=('',10), pady=15, padx=5).grid(row=1)
            Label(self.crf, text="Horizontal Bar Chart Shows Bottom 5 Crimes in Pre-Designated Area", font=('',10), pady=15, padx=5).grid(row=2)
            Label(self.crf, text="Line Chart Shows All Crimes in Pre-Designated Area", font=('',10), pady=15, padx=5).grid(row=3)
            Button(self.crf, text='Bar Chart', bd=5, font=('',15), padx=5, pady=5, command=self.barChart).grid(row=4, sticky=W)
            Button(self.crf, text='Horizontal Bar Chart', bd=5, font=('',15), padx=5, pady=5, command=self.hbarChart).grid(row=4)
            Button(self.crf, text='Line Chart', bd=5, font=('',15), padx=5, pady=5, command=self.lineChart).grid(row=4, sticky=E)
            self.crf.grid_rowconfigure(5, minsize=30)
            self.logf.pack_forget()
            self.crf.pack()
            root.title("Data Plot Visualization")
        else:
            msg.showerror("Error", "Username does not exist.")

    # display line graph of top 5 crimes in area
    def lineChart(self):
        dataframe = df[['primary_type']]
        top_crime_count = pd.DataFrame(dataframe.groupby('primary_type').size().sort_values(ascending=True).rename('Crime Count'))
        data = top_crime_count.iloc[-6:-1]

        print(data[::-1])

        data.plot(kind='line')

        plt.title("Line Chart")
        plt.xlabel("Top 5 Various Crimes")
        plt.ylabel("Crime Count Within My Location")
        plt.subplots_adjust(left=0.11, right=0.90, top=0.93, bottom=0.11)

        plt.show()

    # display horizontal bar graph of all crimes in area
    def hbarChart(self):
        dataframe = df[['primary_type']]
        all_crime_count = pd.DataFrame(dataframe.groupby('primary_type').size().sort_values(ascending=True).rename('Crime Count'))
        data = all_crime_count.iloc[-15:-1]

        print(data[::-1])

        data.plot(kind='barh')

        plt.title("Horizontal Bar Chart")
        plt.ylabel("All Crimes")
        plt.xlabel("Crime Count Within My Location")
        plt.subplots_adjust(left=0.48, right=0.98, top=0.93, bottom=0.11)

        plt.show()

    # display bar graph of bottom 5 crimes in area
    def barChart(self):
        dataframe = df[['primary_type']]
        bottom_crime_count = pd.DataFrame(dataframe.groupby('primary_type').size().sort_values(ascending=True).rename('Crime Count'))
        data = bottom_crime_count.iloc[-13:-8]

        print(data[::-1])

        data.plot(kind='bar')

        plt.title("Bar Chart")
        plt.xlabel("Bottom 5 Various Crimes")
        plt.ylabel("Crime Count Within My Location")
        plt.subplots_adjust(left=0.10, right=0.96, top=0.92, bottom=0.61) 

        plt.show()

    # login widgets
    def widgets(self):
        self.head = Label(self.master, text='User Login', font=('',25), pady=0)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=90)
        Label(self.logf, text='Username: ', font=('',15), pady=5, padx=5).grid(sticky = W)
        Entry(self.logf, textvariable=self.usersname, bd=5, font=('',10)).grid(row=0,column=1)
        Label(self.logf, text='Password: ', font=('',15), pady=5, padx=5).grid(sticky = W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('',10), show = '*').grid(row=1,column=1)
        Button(self.logf, text='Login', bd=3 , font=('',15), padx=5, pady=5, command=self.login).place(relx=0.5, rely=1.5, anchor=CENTER)
        self.logf.pack()

# create table
def createTable():
    connection = sqlite3.connect('mydb.db')
    print("\nDatabase Opened Successfully\n")

    connection.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      uname TEXT NOT NULL,
                      upass CHAR(64) NOT NULL);''')
    print("Table Created Successfully\n")

    connection.close()

# create window, database table and application object
createTable()
root = Tk()
root.title("Login Window")

# instantiate class
cobj = main(root) 
cobj.login()
root.mainloop()