from datetime import datetime


class CustomException(Exception):
    def __init__(self, error_m):
        self.add_log_msg(error_m)

    def add_log_msg(self, error_m):
        with open("logs.txt", "a") as logs:
            logs.write(f"{datetime.today()}: {error_m} \n")
        print(f"The log message '{error_m}' was added.")


first_exception = CustomException("Error#1")
second = CustomException("Error#2")
CustomException.add_log_msg(first_exception, "Custom")
