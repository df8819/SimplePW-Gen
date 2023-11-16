import tkinter as tk
from tkinter import messagebox
import secrets
import string


# Function to generate a random password
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if characters:
        # Using secrets.choice instead of random.choice for better security
        return ''.join(secrets.choice(characters) for _ in range(length))
    else:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return ""


# Function to update the password entry with a new password
def update_password():
    length = int(length_scale.get())
    use_uppercase = var_upper.get()
    use_lowercase = var_lower.get()
    use_digits = var_digit.get()
    use_specials = var_special.get()

    new_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, new_password)


# Center the window on the screen
def center_window(width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


# Reset the UI to the initial dimensions
def reset_ui():
    center_window(400, 300)


# Create the main window
root = tk.Tk()
root.title("Password Generator")
center_window(400, 300)  # Width x Height

# Allow window resizing
root.resizable(True, True)

# Create the password entry
password_entry = tk.Entry(root, width=24)
password_entry.pack(fill='x', padx=10, pady=10)

# Create a scale for password length
length_scale = tk.Scale(root, from_=6, to_=128, orient='horizontal', label='Password length')
length_scale.set(24)  # default length
length_scale.pack(fill='x', padx=10)

# Create checkboxes for password options
var_upper = tk.BooleanVar(value=True)
check_upper = tk.Checkbutton(root, text="Uppercase Letters", variable=var_upper, anchor='w')
check_upper.pack(fill='x', padx=10)

var_lower = tk.BooleanVar(value=True)
check_lower = tk.Checkbutton(root, text="Lowercase Letters", variable=var_lower, anchor='w')
check_lower.pack(fill='x', padx=10)

var_digit = tk.BooleanVar(value=True)
check_digit = tk.Checkbutton(root, text="Digits", variable=var_digit, anchor='w')
check_digit.pack(fill='x', padx=10)

var_special = tk.BooleanVar(value=True)
check_special = tk.Checkbutton(root, text="Special Characters", variable=var_special, anchor='w')
check_special.pack(fill='x', padx=10)

# Create buttons for generating and resetting the UI
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

reset_button = tk.Button(button_frame, text="Reset Window Size", command=reset_ui)
reset_button.pack(side='left', padx=5)

generate_button = tk.Button(button_frame, text="Generate Password", command=update_password)
generate_button.pack(side='left', padx=5)

# Start the GUI loop
root.mainloop()
