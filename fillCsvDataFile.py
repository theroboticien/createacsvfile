import tkinter
from tkinter import messagebox
import random
import string

# Helper function to generate random lowercase strings
def random_lowercase(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Define the function to create the CSV file
def createaCSVFile():
    """
       Function for filling the CSV File
    """
    if len(ent1.get()) == 0:
        nbr_coloumn = 0
    else:
        nbr_coloumn = int(float(ent1.get()))

    if len(ent2.get()) == 0:
        nbr_line = 0
    else:
        nbr_line = int(float(ent2.get()))

    if nbr_line == 0 and nbr_coloumn == 0:
        messagebox.showinfo("Error", "Please Enter the number of data entry you need")
    else:
        # Open a file with the option to rewrite the file if it exists and create the file if it does not exist
        with open("data.csv", "w") as f:
            # Fill the file with the information needed
            for i in range(0, nbr_line):
                for j in range(0, nbr_coloumn):
                    # Create a random word
                    word = random_lowercase(6)
                    # Write the word to the file
                    f.write(f"{word}") if j == nbr_coloumn - 1 else f.write(f"{word},")
                f.write("\n")
        messagebox.showinfo("Congratulation", "CSV File created")

# Create the tkinter GUI
root = tkinter.Tk()
root.title("CSV File Creator")

# Add input fields and labels
tkinter.Label(root, text="Number of Columns:").grid(row=0, column=0)
ent1 = tkinter.Entry(root)
ent1.grid(row=0, column=1)

tkinter.Label(root, text="Number of Rows:").grid(row=1, column=0)
ent2 = tkinter.Entry(root)
ent2.grid(row=1, column=1)

# Add a button to trigger the CSV creation
tkinter.Button(root, text="Create CSV", command=createaCSVFile).grid(row=2, column=0, columnspan=2)

# Run the tkinter main loop
root.mainloop()