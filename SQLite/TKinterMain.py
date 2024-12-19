#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

import addFoodEntry as dbScript


class MainProgram(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Set visual data
        self.title("Tkinter Window Demo")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        
        # Set Frame container data
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create Vars for Frame Creation
        windowList = {MainPage, FoodEntry, DisplayValues}
        self.frames = {}
        
        # Create Window Frames
        for page in windowList:
            page_name = page.__name__
            frame = page(parent=container, controller= self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    
        

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create Buttons with text and functionality
        go_to_FoodEntry = tk.Button(
            self,
            text = "Make an entry to the database", 
            command=lambda: controller.show_frame("FoodEntry")
        )

        go_to_DisplayValues = tk.Button(
            self,
            text = "See the Database Values",
            command=lambda: [controller.show_frame("DisplayValues"),
                             controller.frames["DisplayValues"].update_values()]
        )
        
        exit_button = ttk.Button(
            self,
            text='Exit',
            command=lambda: self.quit()
        )

        # Set visual data of above buttons
        go_to_FoodEntry.pack(ipadx=5, ipady=5, expand=True)
        go_to_DisplayValues.pack(ipadx=10, ipady=10, expand=True)
        exit_button.pack( ipadx=20, ipady=20, expand=True)

class FoodEntry(tk.Frame):
    def __init__(self, parent, controller):
        # Call init of super Class
        tk.Frame.__init__(self, parent)
        
        # initialize vars
        self.controller = controller
        count = tk.DoubleVar(); protein = tk.DoubleVar(); food = tk.StringVar()
        
        # Create Entry fields and respective Labels
        food_name = ttk.Entry(self, textvariable=food)
        food_name_lbl = ttk.Label(self, text="Food Name")
        calories_count = ttk.Entry(self, textvariable=count)
        calories_count_lbl = ttk.Label(self, text="Calories Count")
        protein_count = ttk.Entry(self, textvariable=protein)
        protein_count_lbl = ttk.Label(self, text="Protein Count")
        
        # Create Button to enter an entry into the database
        add_food_entry_button = ttk.Button(
            self,
            text="Enter",
            command=lambda: dbScript.add_entry({"Count": count.get(), "Protein": protein.get(), "Food": food.get()})
        )
        
        # Create Button to go back to Main the program
        exit_button = create_back_button(self, controller)
        
        # Set visual data of Buttons, Labels and Entries
        # Labels and Entries:
        food_name_lbl.pack()
        food_name.pack(fill="x", expand=True)
        calories_count_lbl.pack()
        calories_count.pack(fill="x", expand=True)
        protein_count_lbl.pack()
        protein_count.pack(fill="x", expand=True)
        
        # Buttons:
        add_food_entry_button.pack( ipadx=5, ipady=5, expand=True)
        exit_button.pack(ipadx=20, ipady=20, expand=True)
        
class DisplayValues(tk.Frame):
    def __init__(self, parent, controller):
        
        # Call init of super Class
        tk.Frame.__init__(self, parent)
        
        # initialize vars
        self.controller = controller

        # Create Button to go back to Main the program
        exit_button = create_back_button(self, controller)
        
        # Create Text Widgets
        self.calories_today = tk.Text(self)
        self.protein_today = tk.Text(self)
        
        # Set visual data of Buttons
        exit_button.pack(ipadx=20, ipady=20, expand=True)
        
        # Set visual data of Text Widgets
        self.calories_today.pack()
        self.protein_today.pack()
        
    calories = 0
    def update_values(self):
        self.calories_today.insert(tk.END, dbScript.get_count())
        self.protein_today.insert(tk.END, dbScript.get_protein())
    
def create_back_button(self, controller):
    return ttk.Button(
        self,
        text='Back',
        command=lambda: controller.show_frame("MainPage")
    )

# Initialize the program and keep it running until manually closing
if __name__ == "__main__":
    main_page = MainProgram()
    main_page.mainloop()
