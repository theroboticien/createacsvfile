# This is a program to create a csv file
# The aim of this program is to create a csv file to fill different Databases
# All the data will be strings
# we can make this better by selecting the type of data entered

from python_random_strings import random_strings


# Main program
# In this part of the program we define how many data we want create
# How many coloumn to fill
print('This is a program to create a csv file')
value = input('please enter the number of coloumn that you want to create: ')
nbr_coloumn =  int(float(value))
print(f'The number of coloumn is : {nbr_coloumn}')

# How many line to fill
value = input('please enter the number of line that you want to create: ')
nbr_line =  int(float(value))
print(f'The number of line is : {nbr_line}')

# Create a random word
word = random_strings.random_lowercase(6)

# Create the csv file
# A CSV file is a Comma Separated Values file. All CSV files are plain text files,
# can contain numbers and letters only,
# and structure the data contained within them in a tabular, or table, form.

# Open a file with the option to rewrite the file if exist and create file if does not exist
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
