from python_random_strings import random_strings
import tkinter.messagebox
from tkinter import *


windows=Tk() #creating the main windowsdow and storing the windowsdow object in 'windows'
windows.geometry('300x100') #setting the size of the windowsdow
windows.title('createaCSVFile') #setting title of the windowsdow

Label(windows, text='number coloumn').grid(row=0)
Label(windows, text='number line').grid(row=1)

ent1 = Entry(windows)
ent2 = Entry(windows)
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)


def func():#function of the button
    nbr_coloumn = int(float(ent1.get()))
    nbr_line    = int(float(ent2.get()))

    # Create a random word
    word = random_strings.random_lowercase(6)

    # Create the csv file
    # A CSV file is a Comma Separated Values file. All CSV files are plain text files,
    # can contain numbers and letters only,
    # and structure the data contained within them in a tabular, or table, form.
    # Open a file with the option to rewrite the file if exist and create file if does not exist
    #file if exist and create file if does not exist
    f = open("data.csv", "w")

    # Fill the file with the information needed
    for i in range(0,nbr_line):
        for j in range(0,nbr_coloumn):
            # Create a random word
            word = random_strings.random_lowercase(6)
            # Write to the word to the file
            f.write(f"{word}") if j == nbr_coloumn-1 else f.write(f"{word},")
        f.write("\n")
    # Close the opened file
    f.close()
    tkinter.messagebox.showinfo("Congratulation","CSV File created")

#creating a button that launch the creation of the CSV File
btn=Button(windows,text="Create CSV file", width=10,height=2,command=func)
btn.place(x=200,y=55)

# exit button
exit_button = Button(windows,text="Exit",width=10,height=2,command=lambda:windows.quit())
exit_button.place(x=100,y=55)
mainloop() 
