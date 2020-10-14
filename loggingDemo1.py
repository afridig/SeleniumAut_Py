import logging

#to save the messages in a particular location instead of displaying it in the console
logging.basicConfig(filename="C:\\seleniumLogs\\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG) #by adding the logging.DEBUG, the warning messages are printed from debug onwards

#by default the debug and info messages are not printed as they are not serious enough.. printing starts from warning message onwards
logging.debug("This is a debug message.")
logging.info("This is an info message.")

#the following messages are printed due to their severity level
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")