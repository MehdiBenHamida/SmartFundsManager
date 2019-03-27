"""
 # Title: Smart Fund Manager
 # File: Settings.py
 # Description: Define the logger methods to log to log file
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

settings = {
    'application': {
        'name': "Smart Funds Manager",
        'host': "127.0.0.1",
        'port': 5000,
        'debug': True,
    },
    'logger': {
        'logFilePath': "/home/mehdi/",
        'logFileName': "SFMLog",
        'logFileExtension': "log",
        'maxLogFileSize': 1,
        'logLevel': ["INFO", "ERROR", "WARN"],
    },
    'database': {
        'host': "localhost",
        'user': "user",
        'password': "12345",
        'name': "PythonMySQL"
    }
}