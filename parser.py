import requests
from bs4 import BeautifulSoup


class Day:
    def __init__(self, day_week, day_true):
        self.year = day_true
        self.week = day_week


res = requests.get("https://ssau.ru/rasp?groupId=531874228")


soup = BeautifulSoup(res.text, 'lxml')

box = soup.find('div', class_="schedule__items")
dates = box.find_all('div', class_="schedule__item schedule__head")
days = []

for date in dates:
    day_of_week = date.find('div', class_="schedule__head-weekday")
    date_true = date.find('div', class_="caption-text schedule__head-date")
    days.append(Day(day_of_week.text, date_true.text)) if (
        day_of_week and date_true) is not None else None

subjects_soup = soup.find_all('div', class_="schedule__item")
subjects = []
for sub in subjects_soup[7:]:
    txt = sub.text + '\n'
    subjects.append(sub.text)

subjects_week = {
    "monday": subjects[0::6],
    "tuesday": subjects[1::6],
    "wednesday": subjects[2::6],
    "thursday": subjects[3::6],
    "friday": subjects[4::6],
    "saturday": subjects[5::6],
}
