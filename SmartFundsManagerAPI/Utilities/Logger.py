"""
 # Title: Smart Fund Manager
 # File: Logger.py
 # Description: Define the logger methods to log to log file
 # Author: Mèhdi Ben Hamida
 # Company: **************
"""

import os
import pkg_resources
from SmartFundsManagerAPI.Utilities.Settings import settings
from datetime import datetime
from SmartFundsManagerAPI.Utilities.Colors import Colors

# set the constant values from the settings object
MAX_LOG_FILE_SIZE = settings["logger"]["maxLogFileSize"]
LOG_FILE_NAME = settings["logger"]["logFileName"]
LOG_FILE_EXTENSION = settings["logger"]["logFileExtension"]
LOG_LEVEL = settings["logger"]["logLevel"]
LOG_FILE_PATH = settings["logger"]["logFilePath"]


def log_file_head():
    header = "========================================================================\n" +\
             "==                         Smart Funds Manager                        ==\n" + \
             "========================================================================\n" + \
             "==                       version: "+pkg_resources.require("SmartFundsManagerAPI")[0].version+" " \
                                                  "                              ==\n" + \
             "========================================================================\n" + \
             "==                   Licenced to: Mèhdi Ben Hamida                    ==\n" + \
             "==                         2019-"+str(datetime.now().year)+"               " \
                                                  "                   ==\n" + \
             "========================================================================\n"
    return header


def log_info(msg, code):
    """
    Log an info message to the log file and the application console (colored with blue)
    :param msg: Message that will be logged
    :param code: Method code that generates the log message
    :return: void
    """
    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st = '[' + time + ']:[INFO]:[' + code + ']:' + msg
        i = 0
        while True:
            log_file_path = os.path.join(LOG_FILE_PATH, LOG_FILE_NAME+"("+str(i)+")." + LOG_FILE_EXTENSION)
            if os.path.exists(log_file_path):
                if os.path.getsize(log_file_path)/(1024.0*1024.0) > MAX_LOG_FILE_SIZE:
                    i = i + 1
                else:
                    if "INFO" in LOG_LEVEL:
                        print(Colors.INFO + st + Colors.ENDC)
                        f = open(log_file_path, 'a')
                        f.write("\n" + st)
                        break
                    else:
                        break
            else:
                if not os.path.exists(LOG_FILE_PATH):
                    os.makedirs(LOG_FILE_PATH)
                if "INFO" in LOG_LEVEL:
                    print(Colors.INFO + st + Colors.ENDC)
                    f = open(log_file_path, 'a')
                    f.write(log_file_head())
                    f.write("\n" + st)
                    break
                else:
                    break
    except Exception as e:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Colors.ERROR+'['+time+']:[ERROR]:[local]:(not in log file)'+str(e)+Colors.ENDC)


def log_error(msg, code):
    """
    Log an error message to the log file and the application console (colored with red)
    :param msg: Message that will be logged
    :param code: Method code that generates the log message
    :return: void
    """
    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st = '[' + time + ']:[ERROR]:[' + code + ']:' + msg
        i = 0
        while True:
            log_file_path = os.path.join(LOG_FILE_PATH, LOG_FILE_NAME+"("+str(i)+")." + LOG_FILE_EXTENSION)
            if os.path.exists(log_file_path):
                if os.path.getsize(log_file_path)/(1024.0*1024.0) > MAX_LOG_FILE_SIZE:
                    i = i + 1
                else:
                    if "ERROR" in LOG_LEVEL:
                        print(Colors.ERROR + st + Colors.ENDC)
                        f = open(log_file_path, 'a')
                        f.write("\n" + st)
                        break
                    else:
                        break
            else:
                if not os.path.exists(LOG_FILE_PATH):
                    os.makedirs(LOG_FILE_PATH)
                if "ERROR" in LOG_LEVEL:
                    print(Colors.ERROR + st + Colors.ENDC)
                    f = open(log_file_path, 'a')
                    f.write(log_file_head())
                    f.write("\n" + st)
                    break
                else:
                    break
    except Exception as e:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Colors.ERROR+'['+time+']:[ERROR]:[local]:(not in log file)'+str(e)+Colors.ENDC)


def log_warning(msg, code):
    """
    Log a warning message to the log file and the application console (colored with yellow)
    :param msg: Message that will be logged
    :param code: Method code that generates the log message
    :return: void
    """
    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st = '[' + time + ']:[WARN]:[' + code + ']:' + msg
        i = 0
        while True:
            log_file_path = os.path.join(LOG_FILE_PATH, LOG_FILE_NAME+"("+str(i)+")." + LOG_FILE_EXTENSION)
            if os.path.exists(log_file_path):
                if os.path.getsize(log_file_path)/(1024.0*1024.0) > MAX_LOG_FILE_SIZE:
                    i = i + 1
                else:
                    if "WARN" in LOG_LEVEL:
                        print(Colors.WARNING + st + Colors.ENDC)
                        f = open(log_file_path, 'a')
                        f.write("\n" + st)
                        break
                    else:
                        break
            else:
                if not os.path.exists(LOG_FILE_PATH):
                    os.makedirs(LOG_FILE_PATH)
                if "WARN" in LOG_LEVEL:
                    print(Colors.WARNING + st + Colors.ENDC)
                    f = open(log_file_path, 'a')
                    f.write(log_file_head())
                    f.write("\n" + st)
                    break
                else:
                    break
    except Exception as e:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Colors.ERROR+'['+time+']:[ERROR]:[local]:(not in log file)'+str(e)+Colors.ENDC)

# TODO: dix the log file header when first
