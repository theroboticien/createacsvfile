import tkinter as tk
from tkinter import messagebox
from tkinter import ttk # Import ttk for themed widgets
from fillCsvDataFile import createaCSVFile # This is the correct import

class CSVApp:
    def __init__(self, master):
        """
        Initializes the CSV File Creator application.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        master.title('CSV File Creator')
        
        # Set initial window size and center it, preventing resizing
        # Adjusted window size to accommodate new button
        self._center_window(master, 450, 260) 
        master.resizable(False, False) # Prevent window resizing

        # Configure styles for ttk widgets for a modern look
        self._configure_styles()

        # Initialize an attribute to store column data types
        # Default to all lowercase strings if not configured
        self.column_data_types = [] 

        # Create and place all GUI widgets
        self._create_widgets()

    def _configure_styles(self):
        """
        G
        Configures the styles for ttk widgets to give a modern look.
        """
        style = ttk.Style()
        style.theme_use('clam') # 'clam', 'alt', 'default', or 'vista' are common themes

        # Configure fonts and padding for labels and entries
        style.configure('TLabel', font=('Arial', 11))
        style.configure('TEntry', font=('Arial', 11))
        style.configure('TButton', font=('Arial', 11, 'bold'), padding=8) # Add padding to buttons
        # Add a hover effect for buttons
        style.map('TButton',
                  background=[('active', '#e0e0e0')], # Button background on hover
                  foreground=[('active', 'black')]) # Button text color on hover
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
        # Pack the frame with vertical padding and allow it to fill horizontal space
        input_frame.pack(pady=10, padx=20, fill='x', expand=True) 

        # Label and Entry for Number of columns
        ttk.Label(input_frame, text='Number of columns:').grid(
            row=0, column=0, padx=pad_x, pady=pad_y, sticky='w' # Align label to the west (left)
        )
        self.ent_col = ttk.Entry(input_frame, width=20)
        self.ent_col.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky='ew') # Expand entry horizontally

        # Label and Entry for Number of rows
        ttk.Label(input_frame, text='Number of rows:').grid(
            row=1, column=0, padx=pad_x, pady=pad_y, sticky='w' # Align label to the west (left)
        )
        self.ent_line = ttk.Entry(input_frame, width=20)
        self.ent_line.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky='ew') # Expand entry horizontally

        # Make the second column within the input_frame expand when the window expands
        input_frame.grid_columnconfigure(1, weight=1)

        # Frame for buttons to group them and manage their layout
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=5, padx=20)

        # Configure Column Data Types button - NEW
        ttk.Button(button_frame, text="Configure Column Types", command=self._open_column_config_window).pack(
            side=tk.TOP, pady=5, fill='x', expand=True
        )

        # Create CSV File button (placed to the left within the button_frame)
        ttk.Button(button_frame, text="Create CSV File", command=self._on_create_csv).pack(
            side=tk.LEFT, padx=(0, 5), pady=5 # Add some padding to the right of this button
        )

        # Exit button (placed to the left, which will put it right of the previous button)
        ttk.Button(button_frame, text="Exit", command=self.master.quit).pack(
            side=tk.LEFT, padx=(5, 0), pady=5 # Add some padding to the left of this button
        )

    def _open_column_config_window(self):
        """
        Opens a new Toplevel window to configure data types for each column.
        """
        try:
            nbr_coloumn = int(self.ent_col.get())
            if nbr_coloumn <= 0:
                messagebox.showwarning(
                    "Input Required", "Please enter a positive number of columns first."
                )
                return
        except ValueError:
            messagebox.showwarning(
                "Input Required", "Please enter a valid integer for number of columns first."
            )
            return

        config_window = tk.Toplevel(self.master)
        config_window.title(f"Configure {nbr_coloumn} Columns")
        # Adjusted window height for better button placement
        self._center_window(config_window, 400, min(100 + nbr_coloumn * 40, 600)) 
        config_window.transient(self.master) # Make it appear on top of the main window
        config_window.grab_set() # Make it modal

        # List to hold references to Combobox widgets
        self.config_comboboxes = []
        data_type_options = ["random_lowercase", "random_integer", "random_float"]

        # If column_data_types is empty or doesn't match current nbr_coloumn, re-initialize
        if not self.column_data_types or len(self.column_data_types) != nbr_coloumn:
            self.column_data_types = ["random_lowercase"] * nbr_coloumn

        for i in range(nbr_coloumn):
            frame_row = ttk.Frame(config_window, padding=(10, 5))
            frame_row.pack(fill='x', padx=10, pady=2)

            ttk.Label(frame_row, text=f"Column {i+1} Type:").pack(side=tk.LEFT, padx=(0,10))
            
            # Create a Combobox for each column
            col_combobox = ttk.Combobox(frame_row, values=data_type_options, state="readonly", width=20)
            
            # Set the current value from self.column_data_types if available
            col_combobox.set(self.column_data_types[i])
            
            col_combobox.pack(side=tk.LEFT, expand=True, fill='x')
            self.config_comboboxes.append(col_combobox) # Store reference

        # Save and Cancel buttons for the config window
        # Using a new frame for buttons to control their layout better
        button_frame_config = ttk.Frame(config_window, padding=(10, 10))
        button_frame_config.pack(pady=10) # Add more vertical padding here

        # Use grid for buttons to center them easily
        ttk.Button(button_frame_config, text="Save Settings", command=lambda: self._save_column_config(config_window)).grid(
            row=0, column=0, padx=5, pady=5
        )
        ttk.Button(button_frame_config, text="Cancel", command=config_window.destroy).grid(
            row=0, column=1, padx=5, pady=5
        )
        # Center the grid within its frame
        button_frame_config.grid_columnconfigure(0, weight=1)
        button_frame_config.grid_columnconfigure(1, weight=1)
        button_frame_config.grid_rowconfigure(0, weight=1)


        self.master.wait_window(config_window) # Wait for the config window to close


    def _save_column_config(self, config_window):
        """
        Saves the selected column data types from the configuration window.
        """
        self.column_data_types = [cb.get() for cb in self.config_comboboxes]
        messagebox.showinfo("Configuration Saved", "Column data types have been saved.")
        config_window.destroy()


    def _on_create_csv(self):
        """
        Handles the event when the 'Create CSV File' button is clicked.
        Validates user input and calls the CSV creation function.
        Includes robust error handling for user feedback.
        """
        try:
            # Attempt to convert input to integers
            nbr_coloumn = int(self.ent_col.get())
            nbr_line = int(self.ent_line.get())

            # Validate if numbers are positive
            if nbr_coloumn <= 0 or nbr_line <= 0:
                messagebox.showerror(
                    "Input Error", "Please enter positive integers for rows and columns."
                )
                return
            
            # Ensure column types are configured and match the number of columns
            if not self.column_data_types or len(self.column_data_types) != nbr_coloumn:
                # If not configured, default all columns to random_lowercase
                # or prompt the user to configure
                response = messagebox.askyesno(
                    "Configuration Missing", 
                    "Column data types are not configured or do not match the number of columns. "
                    "Do you want to proceed with 'random_lowercase' for all columns?"
                )
                if response:
                    self.column_data_types = ["random_lowercase"] * nbr_coloumn
                else:
                    messagebox.showinfo("Action Cancelled", "Please configure column types or adjust column count.")
                    return # Stop creation process

            # Call the external function to create the CSV file, passing column_types
            createaCSVFile(nbr_line, nbr_coloumn, self.column_data_types) 
            messagebox.showinfo("Success", "CSV file 'data.csv' created successfully!")
        except ValueError:
            # Handle cases where input is not a valid integer
            messagebox.showerror(
                "Input Error", "Invalid input. Please enter whole numbers for rows and columns."
            )
        except Exception as e: 
            # Catch any other unexpected errors during the file creation process
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
    # Create the root Tkinter window
    root = tk.Tk()
    # Instantiate the CSVApp class
    app = CSVApp(root)
    # Start the Tkinter event loop
    root.mainloop()
