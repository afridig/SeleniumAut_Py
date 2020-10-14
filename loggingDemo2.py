import logging

#to save the messages in a particular location instead of displaying it in the console
logging.basicConfig(filename="C:\\seleniumLogs\\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p') #set time and date format

logger=logging.getLogger() #creating this variable will allow us to use it instead of logging object
logger.setLevel(logging.DEBUG) #an alternative method to set message level

#by default the debug and info messages are not printed as they are not serious enough.. printing starts from warning message onwards
logger.debug("This is a debug message.")
logger.info("This is an info message.")

#the following messages are printed due to their severity level
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")