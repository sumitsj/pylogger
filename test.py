from pylogger import PyLogger

# Using SQLite
logger = PyLogger(table_name='Logs')
logger.log(message="This is first message.", stacktrace="This is stacktrace")