##1. datetime ბიბლიოთეკის გამოყენება

import datetime

def calculate_days_to_birthday(birthdate):
    today = datetime.date.today()
    
    naw = today.year
    birthday_this_year = birthdate.replace(year=naw)
    
    if today > birthday_this_year:
        birthday_this_year = birthday_this_year.replace(year=naw + 1)
    
    days_until_birthday = (birthday_this_year - today).days
    return days_until_birthday

##2. დეკორატორის შექმნა

def two_times(func):
    def any(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return any

##მაგალითი:
@two_times
def add_numbers(a, b):
    return a + b

print(add_numbers(34, 45))

##3. დეკორატორის შექმნა datetime-ის გამოყენებით

import datetime

def log_function_call(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()

##4. მარტივი Qt ინტერფეისი კლასთან

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple PyQt5 App')
        self.setGeometry(50, 50, 100, 100)

        self.layout = QVBoxLayout() 

        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText('text')
        self.layout.addWidget(self.text_input)  

        self.button = QPushButton('on', self)
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleApp()
    sys.exit(app.exec_())        