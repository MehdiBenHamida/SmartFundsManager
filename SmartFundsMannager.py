"""
 # Title: Smart Funds Manager
 # File: SmartFundsManager.py
 # Description: Main file.
 # Author: Mèhdi Ben Hamida
 # Copyright: Copyright (c) 2019
 # Company: *********
"""

from SmartFundsManagerAPI.Utilities.Logger import *
from settings import settings

if __name__ == '__main__':
    try:
        log_info("Application running at on \"http://" + settings.host + ":" + str(settings.port) + "/\"")
    except Exception as e:
        log_error(str(e), '00000')
