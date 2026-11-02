from application.salary import calculate_salary
from application.db.people import get_employees
import emoji
import datetime
data = datetime.datetime.now()
print(data)
print(emoji.emojize('Python is :thumbs_up:'))
calculate_salary()
get_employees()
if __name__ == '__main__':
    print("Hello World")