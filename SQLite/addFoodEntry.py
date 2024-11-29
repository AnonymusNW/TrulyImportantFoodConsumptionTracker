#!/usr/bin/env python3
import sqlite3
import argparse
from tkinter import *
from tkinter import ttk


#parser = argparse.ArgumentParser()
#parser.add_argument('count', type = float )
#parser.add_argument('protein', type = float )
#parser.add_argument('--food', default = "Air", type = str)
#args = parser.parse_args()
kalorienDB = sqlite3.connect("Kalorien.db")

cursor = kalorienDB.cursor()
#dataInput = {"Count": args.count, "Protein": args.protein, "Food": args.food}
def add_entry(data):
    print(data["Count"])
    cursor.execute("INSERT INTO Kalorien(count, protein, date, food) VALUES (:Count, :Protein, current_date, :Food )", data)
    kalorienDB.commit()
    cursor.execute("SELECT SUM(count) FROM Kalorien WHERE date=current_date")
    print(f"Amount of calories consumed today\n{cursor.fetchall()}")
    cursor.execute("SELECT SUM(protein) FROM Kalorien WHERE date=current_date")
    print(f"Amount of proteins consumed today:\n{cursor.fetchall()}")
