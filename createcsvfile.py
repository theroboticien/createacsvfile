"""
This is the version 1.2 of the createaCSVFile program
The aim of this program is to create a csv file to fill different Databases
On this version, all the data will be strings in this version

Note :


A CSV file is a Comma Separated Values file. All CSV files are plain text files,
and can contain numbers and letters only,
and structure the data contained within them in a tabular, or table, form.

Author : Aymane


Organisation : Qualité Logiciel Youtube Channel
"""
import random
import tkinter.messagebox
from tkinter import *
from fillCsvDataFile import createaCSVFile 

windows=Tk() #creating the main windowsdow and storing the windowsdow object in 'windows'
windows.geometry('300x100') #setting the size of the windowsdow
windows.title('createaCSVFile') #setting title of the windowsdow

Label(windows, text='number coloumn').grid(row=0)
Label(windows, text='number line').grid(row=1)

ent1 = Entry(windows)
ent2 = Entry(windows)
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)

#creating a button that launch the creation of the CSV File
createaCSVFilebutton=Button(windows,text="Create CSV file", width=10,height=2,command=createaCSVFile)
#setting the placement of the createaCSVFile button on int the software window
createaCSVFilebutton.place(x=200,y=55)

# exit button
exit_button = Button(windows,text="Exit",width=10,height=2,command=lambda:windows.quit())
#setting the placement of the exit button on int the software window
exit_button.place(x=100,y=55)
mainloop()
