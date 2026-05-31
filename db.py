import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="foodapp",
    password="food123",
    database="food_safety_system"
)

cursor = conn.cursor()