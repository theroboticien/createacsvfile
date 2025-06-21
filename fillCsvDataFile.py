import random
import string

def random_lowercase(length=6):
    """Generates a random string of lowercase English letters."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_integer(min_val=0, max_val=1000):
    """Generates a random integer within a specified range."""
    return random.randint(min_val, max_val)

def random_float(min_val=0.0, max_val=100.0, precision=2):
    """Generates a random float within a specified range with given precision."""
    return round(random.uniform(min_val, max_val), precision)

def createaCSVFile(nbr_line, nbr_coloumn, column_types):
    """
    Creates a CSV file filled with data based on specified column types.

    Args:
        nbr_line (int): The number of lines (rows) to generate.
        nbr_coloumn (int): The number of columns per line.
        column_types (list): A list of strings specifying the data type for each column
                              (e.g., ["random_lowercase", "random_integer", ...]).

    Raises:
        ValueError: If nbr_line or nbr_coloumn are not positive integers,
                    or if column_types length does not match nbr_coloumn.
        TypeError: If nbr_line, nbr_coloumn, or column_types are of incorrect types.
    """
    if not isinstance(nbr_line, int) or not isinstance(nbr_coloumn, int):
        raise TypeError("Number of lines and columns must be integers.")
    if nbr_line <= 0 or nbr_coloumn <= 0:
        raise ValueError("Number of lines and columns must be positive integers.")
    if not isinstance(column_types, list) or len(column_types) != nbr_coloumn:
        raise ValueError(f"Column types list must be a list of length {nbr_coloumn}.")
    
    with open("data.csv", "w") as f:
        for _ in range(nbr_line):
            row_data = []
            for i in range(nbr_coloumn):
                col_type = column_types[i]
                if col_type == "random_lowercase":
                    row_data.append(str(random_lowercase()))
                elif col_type == "random_integer":
                    row_data.append(str(random_integer()))
                elif col_type == "random_float":
                    row_data.append(str(random_float()))
                else:
                    # Default to random lowercase if type is unknown
                    row_data.append(str(random_lowercase())) 
            f.write(",".join(row_data) + "\n")
