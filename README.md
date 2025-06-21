# 📄 CSV File Creator

![image](https://github.com/user-attachments/assets/1a9a4fe2-5b88-445b-ba37-ac858d18b0d1)


**CSV File Creator** is a Python desktop application built with `Tkinter` that enables you to easily generate CSV (Comma-Separated Values) files with fully customizable data. You can define the number of rows and columns, assign data types per column, preview the generated data, and export it—all through a modern and intuitive UI.

---

## ✨ Features

* **Customizable Dimensions**
  Set the number of rows and columns for your CSV file.

* **Per-Column Data Types**
  Choose a data type for each column from the following options:

  * `random_lowercase`: Random lowercase strings
  * `random_integer`: Random integers
  * `random_float`: Random floating-point numbers
  * `random_boolean`: Boolean values (`True`/`False`)
  * `random_date`: Random dates (within a default range)
  * `random_name`: Random common first names

* **Output File Path Selection**
  Easily specify the filename and location where the CSV will be saved.

* **Data Preview**
  Preview a sample of the generated data before exporting the CSV.

* **Reproducible Randomness**
  Within a session, data generation is consistent (same preview = same final output).

* **Modern UI**
  Built with `tkinter.ttk` for a native look and feel.

---

## 🚀 Getting Started

### 📁 Requirements

* Python 3.x

### 📥 Setup

1. Clone this repository or download the source code.
2. Make sure the following two files are in the same directory:

   * `createcsvfile.py`
   * `fillCsvDataFile.py`

### ▶️ Running the Application

Open your terminal or command prompt, navigate to the project directory, and run:

```bash
python createcsvfile.py
```

---

## 🧩 Usage

### 1. Set Number of Columns and Rows

* Enter values in the `Number of columns:` and `Number of rows:` fields.

> *Note: Changing these resets the internal random seed for reproducibility.*

### 2. Configure Column Types *(Optional but Recommended)*

* Click **"Configure Column Types"**.
* In the new window, select a data type for each column from the dropdown.
* Click **"Save Settings"** to apply changes.

### 3. Choose Output File Path

* The default filename is `data.csv`.
* You can:

  * Edit it directly

### 4. Preview Your Data

* Click **"Preview Data"** to see what the output will look like.

### 5. Generate CSV

* Click **"Create CSV File"** to export the generated data to your chosen location.

### 6. Exit

* Click **"Exit"** to close the application.

---

## 🛠 Future Improvements (Planned)

* 🔧 **Per-Column Parameterization**: Configure min/max values, string lengths, or date ranges.
* 📊 **Progress Bar**: Indicate status when generating large files.
* ⚠️ **Real-time Input Validation**: Immediate feedback for invalid inputs.
* 🧠 **More Data Types**: Add options like unique IDs, phone numbers, or user-defined lists.

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).


