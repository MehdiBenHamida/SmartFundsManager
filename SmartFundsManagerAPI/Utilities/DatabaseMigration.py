"""
 # Title: Smart Fund Manager
 # File: DatabaseMigration.py
 # Description: Create the database file (suggested solution: sqlite)
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

from SmartFundsManagerAPI import db

# create the database from sql_alchemy definition
db.create_all()
