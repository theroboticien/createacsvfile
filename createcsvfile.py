import tkinter as tk
from tkinter import messagebox
from tkinter import ttk # Import ttk for themed widgets
from tkinter import filedialog # Import filedialog for file browsing
import os # Import os for temporary file handling
import random # Import random for generating unique temporary filenames
from fillCsvDataFile import createaCSVFile 

class CSVApp:
    # Define constants for repeated strings
    MSG_INPUT_REQUIRED_TITLE = "Input Required"
    MSG_INPUT_INVALID_TITLE = "Input Error"
    MSG_INPUT_INVALID_INT = "Invalid input. Please enter valid integers for rows and columns."


    def __init__(self, master):
        """
        Initializes the CSV File Creator application.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        master.title('CSV File Creator')
        
        # Set initial window size and center it, preventing resizing
        self._center_window(master, 500, 350) 
        master.resizable(False, False) # Prevent window resizing

        # Configure styles for ttk widgets for a modern look
        self._configure_styles()

        # Initialize an attribute to store column data types
        self.column_data_types = [] 
        # Initialize an attribute to store the output file path
        self.output_filepath = tk.StringVar(value="data.csv") # Default filename

        # A seed for reproducibility - initialized to None
        self.current_seed = None 

        # Store previous column/row counts to detect changes and reset seed
        self.prev_nbr_coloumn = 0
        self.prev_nbr_line = 0

        # Create and place all GUI widgets
        self._create_widgets()

    def _configure_styles(self):
        """
        Configures the styles for ttk widgets to give a modern look.
        """
        style = ttk.Style()
        style.theme_use('clam') 

        style.configure('TLabel', font=('Arial', 11))
        style.configure('TEntry', font=('Arial', 11))
        style.configure('TButton', font=('Arial', 11, 'bold'), padding=8) 
        style.map('TButton',
                  background=[('active', '#e0e0e0')], 
                  foreground=[('active', 'black')]) 
        style.configure('TCombobox', font=('Arial', 10))


    def _create_widgets(self):
        """
        Creates and places all the GUI widgets in the window.
        """
        # Padding variables for consistent spacing
        pad_x = 20
        pad_y = 10

        # Frame for input fields to group them logically and apply consistent padding
        input_frame = ttk.Frame(self.master, padding=(pad_x, pad_y, pad_x, pad_y))
        input_frame.pack(pady=10, padx=20, fill='x', expand=True) 

        # Label and Entry for Number of columns
        ttk.Label(input_frame, text='Number of columns:').grid(
            row=0, column=0, padx=pad_x, pady=pad_y, sticky='w' 
        )
        self.ent_col = ttk.Entry(input_frame, width=20)
        self.ent_col.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky='ew') 
        # Bind change event to reset seed
        self.ent_col.bind("<KeyRelease>", self._reset_seed_on_input_change)

        # Label and Entry for Number of rows
        ttk.Label(input_frame, text='Number of rows:').grid(
            row=1, column=0, padx=pad_x, pady=pad_y, sticky='w' 
        )
        self.ent_line = ttk.Entry(input_frame, width=20)
        self.ent_line.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky='ew') 
        # Bind change event to reset seed
        self.ent_line.bind("<KeyRelease>", self._reset_seed_on_input_change)

        # Output File Path
        ttk.Label(input_frame, text='Output File Path:').grid(
            row=2, column=0, padx=pad_x, pady=pad_y, sticky='w'
        )
        file_path_frame = ttk.Frame(input_frame)
        file_path_frame.grid(row=2, column=1, padx=pad_x, pady=pad_y, sticky='ew')

        self.ent_file_path = ttk.Entry(file_path_frame, textvariable=self.output_filepath, width=30)
        self.ent_file_path.pack(side=tk.LEFT, fill='x', expand=True)
        ttk.Button(file_path_frame, text="Browse", command=self._browse_output_file, width=8).pack(side=tk.RIGHT, padx=(5,0))

        # Make the second column within the input_frame expand
        input_frame.grid_columnconfigure(1, weight=1)

        # Frame for buttons to group them and manage their layout
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=5, padx=20)

        # Configure Column Data Types button
        ttk.Button(button_frame, text="Configure Column Types", command=self._open_column_config_window).pack(
            side=tk.TOP, pady=5, fill='x', expand=True
        )
        
        # Preview Data button
        ttk.Button(button_frame, text="Preview Data", command=self._preview_data).pack( 
            side=tk.TOP, pady=5, fill='x', expand=True
        )

        # Create CSV File button
        ttk.Button(button_frame, text="Create CSV File", command=self._on_create_csv).pack(
            side=tk.LEFT, padx=(0, 5), pady=5 
        )

        # Exit button
        ttk.Button(button_frame, text="Exit", command=self.master.quit).pack(
            side=tk.LEFT, padx=(5, 0), pady=5 
        )

    def _browse_output_file(self):
        """
        Opens a file dialog to let the user select the output CSV file path.
        """
        initial_filename = self.output_filepath.get()
        if "/" in initial_filename:
            initial_dir = "/".join(initial_filename.split("/")[:-1])
            initial_file = initial_filename.split("/")[-1]
        else:
            initial_dir = "" 
            initial_file = initial_filename
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=initial_file,
            initialdir=initial_dir
        )
        if file_path:
            self.output_filepath.set(file_path)

    def _reset_seed_on_input_change(self, event=None):
        """
        Resets the current_seed to None if the number of columns or rows changes.
        This ensures that new random data is generated if input parameters change.
        """
        try:
            current_col = int(self.ent_col.get())
            current_row = int(self.ent_line.get())
        except ValueError:
            # If input is invalid, treat as a change to trigger new seed
            current_col = -1 
            current_row = -1

        if current_col != self.prev_nbr_coloumn or current_row != self.prev_nbr_line:
            self.current_seed = None # Reset the seed
            self.prev_nbr_coloumn = current_col
            self.prev_nbr_line = current_row

    def _ensure_random_seed(self):
        """
        Ensures a random seed exists. If not, it generates a new one.
        This seed will then be used for both preview and actual file generation
        until inputs change or it's explicitly reset.
        """
        if self.current_seed is None:
            self.current_seed = random.randint(0, 1000000)

    def _preview_data(self):
        """
        Generates a small sample of the CSV data (based on 'Number of rows' input)
        and displays it in a new Toplevel window.
        Uses a temporary file to avoid overwriting the main output.
        """
        try:
            nbr_coloumn = int(self.ent_col.get())
            preview_nbr_line = int(self.ent_line.get()) 

            if nbr_coloumn <= 0 or preview_nbr_line <= 0:
                messagebox.showwarning(
                    self.MSG_INPUT_REQUIRED_TITLE, "Please enter positive integers for rows and columns to preview."
                )
                return
        except ValueError:
            messagebox.showwarning(
                self.MSG_INPUT_REQUIRED_TITLE, self.MSG_INPUT_INVALID_INT
            )
            return

        if not self.column_data_types or len(self.column_data_types) != nbr_coloumn:
            preview_column_types = ["random_lowercase"] * nbr_coloumn
        else:
            preview_column_types = self.column_data_types

        temp_filename = f"temp_preview_{os.getpid()}_{random.randint(0, 10000)}.csv"

        try:
            self._ensure_random_seed() # Ensure a seed exists
            random.seed(self.current_seed) # Apply the seed
            createaCSVFile(preview_nbr_line, nbr_coloumn, preview_column_types, temp_filename)

            with open(temp_filename, 'r') as f:
                preview_content = f.read()

            preview_window = tk.Toplevel(self.master)
            preview_window.title("CSV Data Preview (Seed: " + str(self.current_seed) + ")") 
            self._center_window(preview_window, 600, 400) 
            preview_window.transient(self.master)
            preview_window.grab_set()

            text_area = tk.Text(preview_window, wrap='none', font=('Courier New', 10))
            text_area.insert(tk.END, preview_content)
            text_area.config(state='disabled') 

            h_scroll = ttk.Scrollbar(preview_window, orient='horizontal', command=text_area.xview)
            v_scroll = ttk.Scrollbar(preview_window, orient='vertical', command=text_area.yview)
            text_area.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

            h_scroll.pack(side='bottom', fill='x')
            v_scroll.pack(side='right', fill='y')
            text_area.pack(side='left', fill='both', expand=True)

            close_button_frame = ttk.Frame(preview_window, padding=(10, 5))
            close_button_frame.pack(fill='x', pady=5)
            ttk.Button(close_button_frame, text="Close Preview", command=preview_window.destroy).pack(pady=5)

        except Exception as e:
            messagebox.showerror("Preview Error", f"Failed to generate preview: {e}")
        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)


    def _open_column_config_window(self):
        """
        Opens a new Toplevel window to configure data types for each column.
        """
        try:
            nbr_coloumn = int(self.ent_col.get())
            if nbr_coloumn <= 0:
                messagebox.showwarning(
                    self.MSG_INPUT_REQUIRED_TITLE, "Please enter a positive number of columns first."
                )
                return
        except ValueError:
            messagebox.showwarning(
                self.MSG_INPUT_REQUIRED_TITLE, self.MSG_INPUT_INVALID_INT
            )
            return

        # Reset seed if column count changed before opening config
        self._reset_seed_on_input_change() 

        config_window = tk.Toplevel(self.master)
        config_window.title(f"Configure {nbr_coloumn} Columns")
        self._center_window(config_window, 400, min(100 + nbr_coloumn * 40, 600)) 
        config_window.transient(self.master) 
        config_window.grab_set() 

        self.config_comboboxes = []
        data_type_options = ["random_lowercase", "random_integer", "random_float", "random_boolean", "random_date", "random_name"] 

        if not self.column_data_types or len(self.column_data_types) != nbr_coloumn:
            self.column_data_types = ["random_lowercase"] * nbr_coloumn

        for i in range(nbr_coloumn):
            frame_row = ttk.Frame(config_window, padding=(10, 5))
            frame_row.pack(fill='x', padx=10, pady=2)

            ttk.Label(frame_row, text=f"Column {i+1} Type:").pack(side=tk.LEFT, padx=(0,10))
            
            col_combobox = ttk.Combobox(frame_row, values=data_type_options, state="readonly", width=20)
            
            if self.column_data_types[i] not in data_type_options:
                col_combobox.set("random_lowercase") 
            else:
                col_combobox.set(self.column_data_types[i])
            
            col_combobox.pack(side=tk.LEFT, expand=True, fill='x')
            self.config_comboboxes.append(col_combobox) 

        # Save and Cancel buttons for the config window
        button_frame_config = ttk.Frame(config_window, padding=(10, 10))
        button_frame_config.pack(pady=10) 

        ttk.Button(button_frame_config, text="Save Settings", command=lambda: self._save_column_config(config_window)).grid(
            row=0, column=0, padx=5, pady=5
        )
        ttk.Button(button_frame_config, text="Cancel", command=config_window.destroy).grid(
            row=0, column=1, padx=5, pady=5
        )
        button_frame_config.grid_columnconfigure(0, weight=1)
        button_frame_config.grid_columnconfigure(1, weight=1)
        button_frame_config.grid_rowconfigure(0, weight=1)


        self.master.wait_window(config_window) 


    def _save_column_config(self, config_window):
        """
        Saves the selected column data types from the configuration window.
        """
        self.column_data_types = [cb.get() for cb in self.config_comboboxes]
        messagebox.showinfo("Configuration Saved", "Column data types have been saved.")
        self.current_seed = None # Reset seed when column types are changed/saved
        config_window.destroy()


    def _on_create_csv(self):
        """
        Handles the event when the 'Create CSV File' button is clicked.
        Validates user input and calls the CSV creation function.
        Includes robust error handling for user feedback.
        """
        try:
            nbr_coloumn = int(self.ent_col.get())
            nbr_line = int(self.ent_line.get())
            output_file = self.output_filepath.get() 

            if nbr_coloumn <= 0 or nbr_line <= 0:
                messagebox.showerror(
                    self.MSG_INPUT_INVALID_TITLE, "Please enter positive integers for rows and columns."
                )
                return
            
            if not output_file:
                messagebox.showerror(
                    self.MSG_INPUT_REQUIRED_TITLE, "Please specify an output file path."
                )
                return

            if not self.column_data_types or len(self.column_data_types) != nbr_coloumn:
                response = messagebox.askyesno(
                    "Configuration Missing", 
                    "Column data types are not configured or do not match the number of columns. "
                    "Do you want to proceed with 'random_lowercase' for all columns?"
                )
                if response:
                    self.column_data_types = ["random_lowercase"] * nbr_coloumn
                else:
                    messagebox.showinfo("Action Cancelled", "Please configure column types or adjust column count.")
                    return 

            self._ensure_random_seed() # Ensure a seed exists
            random.seed(self.current_seed) # Apply the seed
            createaCSVFile(nbr_line, nbr_coloumn, self.column_data_types, output_file) 
            messagebox.showinfo("Success", f"CSV file '{output_file}' created successfully!")
        except ValueError:
            messagebox.showerror(
                self.MSG_INPUT_INVALID_TITLE, self.MSG_INPUT_INVALID_INT
            )
        except Exception as e: 
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def _center_window(self, win, width, height):
        """
        Calculates the position to center the Tkinter window on the screen.

        Args:
            win (tk.Tk): The Tkinter window object.
            width (int): The desired width of the window.
            height (int): The desired height of the window.
        """
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVApp(root)
    root.mainloop()
