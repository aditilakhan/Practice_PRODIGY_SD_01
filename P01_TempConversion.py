import tkinter as tk
from tkinter import messagebox
import random

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            show_output(f"{temp}°C = {fahrenheit:.2f}°F\n{temp}°C = {kelvin:.2f} K")
        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = (temp - 32) * 5/9 + 273.15
            show_output(f"{temp}°F = {celsius:.2f}°C\n{temp}°F = {kelvin:.2f} K")
        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (temp - 273.15) * 9/5 + 32
            show_output(f"{temp} K = {celsius:.2f}°C\n{temp} K = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature.")

# Function to display output in a separate window
def show_output(message):
    output_window = tk.Toplevel(root)
    output_window.title("Converted Temperatures")
    output_window.geometry("300x150")  # Increased size for better readability
    output_window.resizable(False, False)  # Making window non-resizable

    output_label = tk.Label(output_window, text=message, font=("Arial", 14))
    output_label.pack(expand=True, fill='both')

# Main tkinter window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x450")
root.resizable(False, False)  # Making window non-resizable

# Set a dynamic background color
bg_color = "#%06x" % random.randint(0, 0xFFFFFF)
root.configure(bg=bg_color)

# Title
title_label = tk.Label(root, text="Temperature", font=("Arial", 24, "bold"), bg=bg_color, fg="white")
title_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# Temperature entry
entry_temp = tk.Entry(root, font=("Arial", 20))
entry_temp.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# Unit selection dropdown
units = ["Celsius", "Fahrenheit", "Kelvin"]
combo_unit = tk.StringVar()
combo_unit.set(units[0])
unit_menu = tk.OptionMenu(root, combo_unit, *units)
unit_menu.config(font=("Arial", 15))
unit_menu.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 15))
convert_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

root.mainloop()
