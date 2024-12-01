#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

import addFoodEntry


# Create Vars


class MainProgram(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Tkinter Window Demo")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        windowList = {MainPage, FoodEntry}
        self.frames = {}
        # Create Button to enter an entry into the database
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
        go_to_FoodEntry = tk.Button(self, text = "Make an entry to the database", 
                                    command=lambda: controller.show_frame("FoodEntry"))

        # Set visual data of above button
        go_to_FoodEntry.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        
        # Create Button to exit the program
        exit_button = ttk.Button(
            self,
            text='Exit',
            command=lambda: self.quit()
        )

        # Set visual data of above button
        exit_button.pack(
            ipadx=20,
            ipady=20,
            expand=True
        )
        
        go_to_FoodEntry.pack()

class FoodEntry(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller


        count = tk.DoubleVar(); protein = tk.DoubleVar(); food = tk.StringVar()
        
        # Create Entry fields
        food_name = ttk.Entry(self, textvariable=food)
        calories_count = ttk.Entry(self, textvariable=count)
        protein_count = ttk.Entry(self, textvariable=protein)
        
        # Put Entry fields on the layout
        food_name.pack(fill="x", expand=True)
        calories_count.pack(fill="x", expand=True)
        protein_count.pack(fill="x", expand=True)
        
        # Create Button to enter an entry into the database
        add_food_entry_button = ttk.Button(
            self,
            text="Enter",
            command=lambda: addFoodEntry.add_entry({"Count": count.get(), "Protein": protein.get(), "Food": food.get()})
        )
        
        # Set visual data of above button
        add_food_entry_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        
        # Create Button to go back to Main the program
        exit_button = ttk.Button(
            self,
            text='Back',
            command=lambda: controller.show_frame("MainPage")
        )
        
        # Set visual data of above button
        exit_button.pack(
            ipadx=20,
            ipady=20,
            expand=True
        )
    

# Initialize the program and keep it running until manually closing
if __name__ == "__main__":
    main_page = MainProgram()
    main_page.mainloop()
