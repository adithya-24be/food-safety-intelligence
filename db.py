import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

MYSQLHOST = os.getenv("MYSQLHOST")
MYSQLUSER = os.getenv("MYSQLUSER")
MYSQLPASSWORD = os.getenv("MYSQLPASSWORD")
MYSQLDATABASE = os.getenv("MYSQLDATABASE")
MYSQLPORT = os.getenv("MYSQLPORT")

if MYSQLHOST:
    print("Using Render/Railway MySQL")

    conn = mysql.connector.connect(
        host=MYSQLHOST,
        user=MYSQLUSER,
        password=MYSQLPASSWORD,
        database=MYSQLDATABASE,
        port=int(MYSQLPORT)
    )
else:
    print("Using Local MySQL")

    conn = mysql.connector.connect(
        host="localhost",
        user="foodapp",
        password="food123",
        database="food_safety_system",
        port=3306
    )

cursor = conn.cursor(dictionary=True)