#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from typing import Dict

import addFoodEntry


root = tk.Tk()
# Create Vars
count = tk.DoubleVar(); protein = tk.DoubleVar(); food = tk.StringVar()
def init_ui():
    root.title("Tkinter Window Demo")
    message = tk.Label(root, text="GoodBye, Cruel World?")
    message.pack()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    # root.iconphoto(False, tk.PhotoImage(file='Burn.png'))
    create_input_fields()
    create_buttons()

def create_input_fields():
    # Create Input fields
    food_name = ttk.Entry(root, textvariable=food)
    food_name.pack(fill="x", expand=True)
    calories_count = ttk.Entry(root, textvariable=count)
    calories_count.pack(fill="x", expand=True)
    protein_count = ttk.Entry(root, textvariable=protein)
    protein_count.pack(fill="x", expand=True)
    
def create_buttons():
    add_food_entry_button = ttk.Button( # Create Button to enter an entry into the database
        root,
        text="addFoodEntry",
        command=lambda: addFoodEntry.add_entry(update_data())
    )
    
    add_food_entry_button.pack( # Set visual data of above button
        ipadx=5,
        ipady=5,
        expand=True
    )
    
    exit_button = ttk.Button( # Create Button to exit the program
        root,
        text='Exit',
        command=lambda: root.quit()
    )
    
    exit_button.pack( # Set visual data of above button
        ipadx=20,
        ipady=20,
        expand=True
    )
    
# Take the data from the input and put it into an array for easier sql comprehension
def update_data():
    data: dict[str, float | str] = {"Count": count.get(), "Protein": protein.get(), "Food": food.get()}
    return data

# Initialize complete UI
init_ui()

# Here to keep the program running indefinitely
root.mainloop()
