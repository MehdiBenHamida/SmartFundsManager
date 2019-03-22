"""
 # Title: Smart Funds Manager
 # File: SmartFundsManager.py
 # Description: Main file.
 # Author: Mèhdi Ben Hamida
 # Copyright: Copyright (c) 2019
 # Company: *********
"""

from SmartFundsManagerAPI.Utilities.Logger import *
from SmartFundsManagerAPI.Utilities.settings import settings
from SmartFundsManagerAPI import app

if __name__ == '__main__':
    try:
        log_info("Application running at on \"http://" + settings["application"]["host"] + ":" +
                 str(settings['application']['port']) + "/\"", "local")
        app.run(host=settings['application']['host'], port=settings['application']['port'],
                debug=settings['application']['debug'])
    except Exception as e:
        log_error(str(e), "local")
