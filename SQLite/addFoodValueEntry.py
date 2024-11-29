#!/usr/bin/env python3
import sqlite3
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('foodName', type = str)
parser.add_argument('caloriesCount', type = float )
parser.add_argument('protein', type = float )
args = parser.parse_args()
kalorienDB = sqlite3.connect("Kalorien.db")

cursor = kalorienDB.cursor()
data = {"FoodName": args.foodName, "CaloriesCount": args.caloriesCount, "Protein": args.protein}
