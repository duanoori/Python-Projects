import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter import messagebox

# ----- Function to calculate age ----- #
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calculate_age():
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    month_dict = {
        "January":1, "February":2, "March":3, "April":4, "May":5, "June":6, 
        "July":7,"August":8, "September":9, "October":10, "November":11, "December":12
        }
    
    try:
        day_str = day_entry.get()
        month_str = month_combobox.get()
        year_str = year_entry.get()

        if not day_str or not month_str or not year_str:
            raise ValueError("All fields are required.")
        
        try:
            day = int(day_str)
            year = int(year_str)
        except ValueError:
            raise ValueError("Day and Year must be numbers.")
        else:
            month = month_dict[month_str]

            
        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        if day < 1 or day > months[month]:
            raise ValueError("Invalid day")
        if month == 2 and day == 29 and not is_leap_year(year):
            raise ValueError("February 29 is only valid in leap years")
        
        birth_date = dt.datetime(year, month, day)
        today = dt.datetime.now()
        
        if birth_date > today:
            raise ValueError("Birth date cannot be in the future.")

        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        if age_days < 0:
            age_months -= 1
            age_days += (months[birth_date.month] if birth_date.month != 2 else (29 if is_leap_year(birth_date.year) else 28))
        
        if age_months < 0:
            age_years -= 1
            age_months += 12
        
        messagebox.showinfo("Age Result", f"You are {age_years} years, {age_months} months, and {age_days} days old.")

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {str(ve)}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))
       


# ----- Create the age calculation window ----- #
window = tk.Tk()
window.title("Age Calculator")
window.geometry("500x350")
window.resizable(False, False)
window.config(bg="#FFF3E4")

month_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

#Getting current date
today = dt.datetime.now()
label_today = tk.Label(window, text=f"Today's Date: {today.strftime('%d-%m-%Y')}", 
                       font=("times new roman", 12), bg="#FFF3E4", fg="#333333")
label_today.pack(pady=10)

birth_label = tk.Label(window, text="Enter your birth date:", 
                       font=("times new roman", 12), bg="#FFF3E4", fg="#333333")
birth_label.pack(pady=15)
birth_frame = tk.Frame(window, bg="#FFF3E4")
birth_frame.pack(pady=15)

# Day Entry
day_label = tk.Label(birth_frame, text="Day:", 
                     font=("times new roman", 12), bg="#FFF3E4", fg="#333333")
day_label.grid(row=0, column=0, padx=5)
day_entry = tk.Entry(birth_frame, width=5, font=("times new roman", 12))
day_entry.grid(row=0, column=1, padx=5)

# Month Combobox
month_label = tk.Label(birth_frame, text="Month:",
                       font=("times new roman", 12), bg="#FFF3E4", fg="#333333")
month_label.grid(row=0, column=2, padx=5)
month_combobox = ttk.Combobox(birth_frame, values=month_list, width=10, font=("times new roman", 12), state="readonly")
month_combobox.grid(row=0, column=3, padx=5)

# Year Entry
year_label = tk.Label(birth_frame, text="Year:", 
                      font=("times new roman", 12), bg="#FFF3E4", fg="#333333")
year_label.grid(row=0, column=4, padx=5)
year_entry = tk.Entry(birth_frame, width=5, font=("times new roman", 12))
year_entry.grid(row=0, column=5, padx=5)

calculate_button = tk.Button(window, text="Calculate Age", bg="#F9A826", fg="#333333", 
                             font=("times new roman",12,"bold"), width=30, command=calculate_age).place(x = 120, y=180)

window.mainloop()
