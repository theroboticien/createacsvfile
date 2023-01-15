from python_random_strings import random_strings
import tkinter.messagebox
from tkinter import *

def createaCSVFile():
    """
       Funtion for filling the CSV File
    """

    if len(ent1.get()) == 0:
            nbr_coloumn = 0
    else :
        nbr_coloumn = int(float(ent1.get()))

    if len(ent2.get()) == 0:
            nbr_line = 0
    else :
        nbr_line    = int(float(ent2.get()))

    if (nbr_line == 0 and nbr_coloumn ==0):
        tkinter.messagebox.showinfo("Error","Please Enter the number of data entry you need")

    else :
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