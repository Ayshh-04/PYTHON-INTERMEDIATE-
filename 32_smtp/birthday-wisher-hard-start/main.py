import datetime
import pandas
from random import randint
import smtplib
today=datetime.datetime.now()
today_tuple=(today.month,today.day)

data=pandas.read_csv("birthdays.csv")
my_email="ayushjaju8@gmail.com"
password="jrtc lirn dxmd jbur"

new_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in new_dict:
    birthday_person=new_dict[today_tuple]
    file_path=f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content=letter_file.read()
        content=content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as  connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"subject:HAPPY BIRTHDAY\n\n {content}")

