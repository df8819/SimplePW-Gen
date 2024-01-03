import tkinter as tk
from tkinter import messagebox, ttk
import secrets
import string
import random


# Function to generate a random password
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_specials):
    characters = ""
    guaranteed_characters = []

    # Adding at least one character from each selected category
    if use_uppercase:
        characters += string.ascii_uppercase
        guaranteed_characters.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        characters += string.ascii_lowercase
        guaranteed_characters.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        guaranteed_characters.append(secrets.choice(string.digits))
    if use_specials:
        characters += string.punctuation
        guaranteed_characters.append(secrets.choice(string.punctuation))

    # Check if there are enough characters to fill the password length
    if characters and length >= len(guaranteed_characters):
        # Fill the rest of the password length with random choices from all selected categories
        remaining_length = length - len(guaranteed_characters)
        random_characters = ''.join(secrets.choice(characters) for _ in range(remaining_length))

        # Combine guaranteed characters with random characters and shuffle them
        final_password = guaranteed_characters + list(random_characters)
        random.shuffle(final_password)

        return ''.join(final_password)
    else:
        messagebox.showwarning("Warning",
                               "Please select at least one character type, and ensure password length is sufficient!")
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


# Function to generate a random number with a given number of digits
def generate_random_number(digits):
    try:
        # Convert the input to an integer
        digits = int(digits)

        # Check if the number of digits is greater than 0
        if digits > 0:
            first_digit = str(random.randint(1, 9))
            remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(digits - 1))
            return first_digit + remaining_digits
        else:
            messagebox.showwarning("Warning", "The number of digits must be greater than 0!")
            return ""

    except ValueError:
        # If the conversion to an integer fails, it means the input is not a number
        messagebox.showwarning("Warning", "Please enter a numeric value!")
        return ""


# Function to update the random number entry with a new number
def update_random_number():
    digits_str = digits_entry.get()

    # Check if the entry field is empty or not a number
    if not digits_str.isdigit() or not digits_str:
        messagebox.showinfo("Error", "Please enter a number.")
        return

    digits = int(digits_str)

    if digits > 0:
        random_number = generate_random_number(digits)
        number_entry.delete(0, tk.END)
        number_entry.insert(0, random_number)
    else:
        messagebox.showinfo("Error", "Number must be greater than 0.")


# Function to let the user copy the generated content to the clipboard
def copy_to_clipboard(entry_widget):
    root.clipboard_clear()
    root.clipboard_append(entry_widget.get())


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
center_window(400, 300)

# Create Tab Control
tab_control = ttk.Notebook(root)

# Tab1 - Password Generator
password_tab = ttk.Frame(tab_control)
tab_control.add(password_tab, text='Password Generator')

# Tab2 - Random Number Generator
number_tab = ttk.Frame(tab_control)
tab_control.add(number_tab, text='Random Number Generator')
tab_control.pack(expand=1, fill='both')

# Password Generator Widgets (add within password_tab)
password_entry = tk.Entry(password_tab, width=24)
password_entry.pack(fill='x', padx=10, pady=10)

length_scale = tk.Scale(password_tab, from_=6, to_=128, orient='horizontal', label='Password length')
length_scale.set(16)  # default length
length_scale.pack(fill='x', padx=10)

var_upper = tk.BooleanVar(value=True)
check_upper = tk.Checkbutton(password_tab, text="Uppercase Letters", variable=var_upper, anchor='w')
check_upper.pack(fill='x', padx=10)

var_lower = tk.BooleanVar(value=True)
check_lower = tk.Checkbutton(password_tab, text="Lowercase Letters", variable=var_lower, anchor='w')
check_lower.pack(fill='x', padx=10)

var_digit = tk.BooleanVar(value=True)
check_digit = tk.Checkbutton(password_tab, text="Digits", variable=var_digit, anchor='w')
check_digit.pack(fill='x', padx=10)

var_special = tk.BooleanVar(value=True)
check_special = tk.Checkbutton(password_tab, text="Special Characters", variable=var_special, anchor='w')
check_special.pack(fill='x', padx=10)

button_frame_password = tk.Frame(password_tab)
button_frame_password.pack(pady=20)

reset_button = tk.Button(button_frame_password, text="Reset UI", command=reset_ui, bg='grey', fg='white')
reset_button.pack(side='left', padx=5)

spacer1_label = tk.Label(button_frame_password, text="")
spacer1_label.pack(side='left', padx=(25, 25), pady=(0, 0))

generate_button = tk.Button(button_frame_password, text="Generate Password", command=update_password, bg='light blue')
generate_button.pack(side='right', padx=5)

copy_password_button = tk.Button(button_frame_password, text="Copy Password", command=lambda: copy_to_clipboard(password_entry))
copy_password_button.pack(side='right', pady=5)

# Random Number Generator Widgets (add within number_tab)
number_entry_label = tk.Label(number_tab, text="Random Number:")
number_entry_label.pack(side='top', pady=(10, 0))

number_entry = tk.Entry(number_tab, width=24)
number_entry.pack(fill='x', padx=10, pady=5)

digits_label = tk.Label(number_tab, text="Amount of Digits:")
digits_label.pack(side='top', pady=(10, 0))

digits_entry = tk.Entry(number_tab, width=12)
digits_entry.pack(padx=10, pady=5)

# Create a frame in the number_tab for the buttons
button_frame_number = tk.Frame(number_tab)
button_frame_number.pack(pady=20)

reset_button = tk.Button(button_frame_number, text="Reset UI", command=reset_ui, bg='grey', fg='white')
reset_button.pack(side='left', padx=5)

spacer2_label = tk.Label(button_frame_number, text="")
spacer2_label.pack(side='left', padx=(25, 25), pady=(0, 0))

generate_number_button = tk.Button(button_frame_number, text="Generate Number", command=update_random_number, bg='light blue')
generate_number_button.pack(side='right', padx=5)

copy_number_button = tk.Button(button_frame_number, text="Copy Number", command=lambda: copy_to_clipboard(number_entry))
copy_number_button.pack(side='right', pady=5)

# Allow window resizing
root.resizable(True, True)

# Start the GUI loop
root.mainloop()
