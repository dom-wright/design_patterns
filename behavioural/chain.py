'''
Chain of Responsibility

A behavioural design pattern that allows an object to pass a request along a chain of potential handlers until the request is handled or reaches the end of the chain. Each step can either handle the request itself, do nothing and pass it on, or handle and pass it on.

Examples:
- The pattern is commonly seen in logging, whereby an event can be handled by multiple handlers (each logging the event in its own way), depending on its severity.
'''


class Logger:
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger

    def log(self, message, level):
        if self.level <= level:
            self.write_message(message)

        if self.next_logger is not None:
            self.next_logger.log(message, level)

    def write_message(self, message):
        raise NotImplementedError


class ConsoleLogger(Logger):
    def write_message(self, message):
        print("ConsoleLogger: " + message)


class FileLogger(Logger):
    def __init__(self, level, filename):
        super().__init__(level)
        self.filename = filename

    def write_message(self, message):
        with open(self.filename, 'a') as file:
            file.write("FileLogger: " + message + "\n")


class EmailLogger(Logger):
    def __init__(self, level, email):
        super().__init__(level)
        self.email = email

    def write_message(self, message):
        # Send an email with the log message
        print("EmailLogger: Sending email to " + self.email)


# Create the chain of log handlers
console_logger = ConsoleLogger(1)
file_logger = FileLogger(2, 'app.log')
email_logger = EmailLogger(3, 'admin@example.com')

console_logger.set_next_logger(file_logger)
file_logger.set_next_logger(email_logger)

# Usage example
console_logger.log("Debug message", 1)  # ConsoleLogger: Debug message
# ConsoleLogger: Info message\nFileLogger: Info message
console_logger.log("Info message", 2)
# ConsoleLogger: Error message\nFileLogger: Error message\nEmailLogger: Sending email to admin@example.com
console_logger.log("Error message", 3)
