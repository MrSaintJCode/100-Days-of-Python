import sqlite3
dbName = "Checklist"
tableContent = ["itemID", "item"]
newTable = f"""
CREATE TABLE IF NOT EXISTS Lists(
    {tableContent[0]} INTEGER PRIMARY KEY,
    {tableContent[1]} VARCHAR(20) NOT NULL
)
"""
database = sqlite3.connect(f"{dbName}.db")
db = database.cursor()
db.execute(newTable)