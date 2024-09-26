# import tkinter as tk
# from tkinter import messagebox  # Import messagebox here
# import re

# screen = tk.Tk()

# screen.title("Tops Technologies")
# screen.geometry("400x400")

# logo_path = "img/logo.ico"
# screen.iconbitmap(logo_path)

# title = tk.Label(screen, text="Register", font=("Arial", 20, "bold"), fg="red")
# title.pack()

# # Create a frame as the underline
# underline = tk.Frame(screen, height=2, width=title.winfo_reqwidth(), bg="red")
# underline.pack()

# # Adjust underline width after the label is displayed
# def adjust_underline():
#     underline.config(width=title.winfo_width())

# screen.after(10, adjust_underline)

# # Entry fields
# username_label = tk.Label(screen, text="Username:", font=("Arial", 15))
# username_label.pack()
# username_entry = tk.Entry(screen, font=("Arial", 15))
# username_entry.pack()

# email_label = tk.Label(screen, text="Email:", font=("Arial", 15))
# email_label.pack()
# email_entry = tk.Entry(screen, font=("Arial", 15))
# email_entry.pack()

# password_label = tk.Label(screen, text="Password:", font=("Arial", 15))
# password_label.pack()
# password_entry = tk.Entry(screen, font=("Arial", 15), show="*")
# password_entry.pack()

# confirm_password_label = tk.Label(screen, text="Confirm Password:", font=("Arial", 15))
# confirm_password_label.pack()
# confirm_password_entry = tk.Entry(screen, font=("Arial", 15), show="*")
# confirm_password_entry.pack()

# def validate_fields():
#     username = username_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     confirm_password = confirm_password_entry.get()

#     def validate_email(email):
#         pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         return re.match(pattern, email) is not None
    
#     def validate_password(password):
#         pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#         return re.match(pattern, password) is not None

#     if not username:
#         messagebox.showerror("Error", "Username cannot be empty.")
#         return False
#     if not email:
#         messagebox.showerror("Error", "Email cannot be empty.")
#         return False
    
#     if not validate_email(email):
#         messagebox.showerror("Error", "Invalid email address.")
#         return False
    
#     if not password:
#         messagebox.showerror("Error", "Password cannot be empty.")
#         return False
    
#     if not validate_password(password):
#         messagebox.showerror("Error", "Password does not meet the requirements.")
#         return False
    
#     if password != confirm_password:
#         messagebox.showerror("Error", "Password and confirm password do not match.")

#     return True

# def submit_handler():
#     if validate_fields():
#         username = username_entry.get()
#         email = email_entry.get()
#         password = password_entry.get()
#         confirm_password = confirm_password_entry.get()

#         print(f"Username: {username}")
#         print(f"Email: {email}")
#         print(f"Password: {password}")
#         print(f"Confirm Password: {confirm_password}")

#         print("Form submitted successfully")

# submit_button = tk.Button(screen, text="Submit", font=("Arial", 15), command=submit_handler)
# submit_button.pack()

# screen.mainloop()


# Style for chat GPT

import tkinter as tk
from tkinter import messagebox
import re

# Function to create a stylish frame
def create_stylish_frame(parent):
    frame = tk.Frame(parent, bg="#f0f0f0", padx=20, pady=20)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    return frame

# Main application window
screen = tk.Tk()
screen.title("Tops Technologies")
screen.geometry("400x500")
screen.configure(bg="#f0f0f0")

# Logo (if available, uncomment this line if you have an icon)
# logo_path = "img/logo.ico"
# screen.iconbitmap(logo_path)

# Title Label
title = tk.Label(screen, text="Register", font=("Arial", 24, "bold"), fg="#FF5733", bg="#f0f0f0")
title.pack(pady=(20, 10))

# Stylish Frame
frame = create_stylish_frame(screen)

# Entry fields
username_label = tk.Label(frame, text="Username:", font=("Arial", 14), bg="#f0f0f0")
username_label.pack(anchor='w')
username_entry = tk.Entry(frame, font=("Arial", 14), bd=2, relief="groove")
username_entry.pack(fill=tk.X, pady=(0, 10))

email_label = tk.Label(frame, text="Email:", font=("Arial", 14), bg="#f0f0f0")
email_label.pack(anchor='w')
email_entry = tk.Entry(frame, font=("Arial", 14), bd=2, relief="groove")
email_entry.pack(fill=tk.X, pady=(0, 10))

password_label = tk.Label(frame, text="Password:", font=("Arial", 14), bg="#f0f0f0")
password_label.pack(anchor='w')
password_entry = tk.Entry(frame, font=("Arial", 14), show="*", bd=2, relief="groove")
password_entry.pack(fill=tk.X, pady=(0, 10))

confirm_password_label = tk.Label(frame, text="Confirm Password:", font=("Arial", 14), bg="#f0f0f0")
confirm_password_label.pack(anchor='w')
confirm_password_entry = tk.Entry(frame, font=("Arial", 14), show="*", bd=2, relief="groove")
confirm_password_entry.pack(fill=tk.X, pady=(0, 20))

# Validation functions
def validate_fields():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_password(password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password) is not None

    if not username:
        messagebox.showerror("Error", "Username cannot be empty.")
        return False
    if not email:
        messagebox.showerror("Error", "Email cannot be empty.")
        return False
    
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address.")
        return False
    
    if not password:
        messagebox.showerror("Error", "Password cannot be empty.")
        return False
    
    if not validate_password(password):
        messagebox.showerror("Error", "Password does not meet the requirements.")
        return False
    
    if password != confirm_password:
        messagebox.showerror("Error", "Password and confirm password do not match.")

    return True

def submit_handler():
    if validate_fields():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}")

        print("Form submitted successfully")

# Submit Button
submit_button = tk.Button(frame, text="Submit", font=("Arial", 16), command=submit_handler, bg="#FF5733", fg="white", bd=0, relief="raised")
submit_button.pack(pady=(10, 0))

screen.mainloop()
