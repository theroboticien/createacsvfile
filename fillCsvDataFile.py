import random
import string
import datetime

def random_lowercase(length=6):
    """Generates a random string of lowercase English letters."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def random_integer(min_val=0, max_val=1000):
    """Generates a random integer within a specified range."""
    return random.randint(min_val, max_val)

def random_float(min_val=0.0, max_val=100.0, precision=2):
    """Generates a random float within a specified range with given precision."""
    return round(random.uniform(min_val, max_val), precision)

def random_boolean():
    """Generates a random boolean value (True or False)."""
    return random.choice([True, False])

def random_date(start_date=datetime.date(2000, 1, 1), end_date=datetime.date(2025, 12, 31)):
    """
    Generates a random date within a specified range.
    NOTE: For more advanced usage, these start/end dates would be configurable via UI.
    """
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_day = start_date + datetime.timedelta(days=random_number_of_days)
    return random_day.strftime("%Y-%m-%d") # Format as YYYY-MM-DD string

def random_name():
    """Generates a random common first name."""
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kelly", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zoe"]
    return random.choice(names)


def createaCSVFile(nbr_line, nbr_coloumn, column_types, filename="data.csv"):
    """
    Creates a CSV file filled with data based on specified column types.

    Args:
        nbr_line (int): The number of lines (rows) to generate.
        nbr_coloumn (int): The number of columns per line.
        column_types (list): A list of strings specifying the data type for each column
                              (e.g., ["random_lowercase", "random_integer", ...]).
        filename (str): The name/path of the CSV file to create. Defaults to "data.csv".

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
    
    with open(filename, "w") as f:
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
                elif col_type == "random_boolean":
                    row_data.append(str(random_boolean()))
                elif col_type == "random_date":
                    row_data.append(str(random_date()))
                elif col_type == "random_name":
                    row_data.append(str(random_name()))
                else:
                    # Default to random lowercase if type is unknown
                    row_data.append(str(random_lowercase())) 
            f.write(",".join(row_data) + "\n")
