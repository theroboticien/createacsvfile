# Create CSV File

## Introduction

This project is a Python program designed to generate random CSV files. The generated CSV files can be used to populate different databases with random string data.

## Features

- Generates CSV files with user-defined numbers of rows and columns.
- Populates the CSV file with random strings.
- Simple and intuitive GUI built with `tkinter`.

## How It Works

1. The user specifies the number of rows and columns for the CSV file.
2. The program generates random strings for each cell in the table.
3. The data is saved in a file named `data.csv`.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `random` (standard Python library)

## Usage

1. Run the program by executing `fillCsvDataFile.py` or `createcsvfile.py`.
    ```bash
    py createcsvfile.py
2. Enter the number of rows and columns in the GUI.
3. Click the "Create CSV" button to generate the file.
4. The generated file will be saved as `data.csv` in the project directory.

## Example

If you specify:
- **Rows**: 10
- **Columns**: 5

The program will generate a `data.csv` file with 10 rows and 5 columns, filled with random strings.

## Notes

- A CSV (Comma Separated Values) file is a plain text file that organizes data in a tabular format.
- The generated data consists of random lowercase strings.

## License

This project is licensed under the [MIT License](LICENSE.md).
