import logging

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ]
)

# Display different logging messages
logging.debug("Debugging the program")
logging.info("Program executed successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("Critical error detected")

'''
Output:
2026-11-20 11:00:00 - DEBUG - Debugging the program
2026-11-20 11:00:00 - INFO - Program executed successfully
2026-11-20 11:00:00 - WARNING - This is a warning message
2026-11-20 11:00:00 - ERROR - An error has occurred
2026-11-20 11:00:00 - CRITICAL - Critical error detected
'''
