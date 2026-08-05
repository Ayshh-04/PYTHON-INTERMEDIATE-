# import smtplib
# my_email="ayushjaju8@gmail.com"
# password="jrtc lirn dxmd jbur"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() #this makes connection secure
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="ayushjaju9@gmail.com",
#                         msg="subject:thi is suject\n\n this is message")

import datetime as dt
import smtplib
from random import choice
# now=dt.datetime.now()
# # print(now)
# year=now.year # can do same for onth da time 
# print(year)

# # for particular date as per you
# my_birthday=dt.datetime(year=2006,month=8,day=4)


now=dt.datetime.now()
day_of_week=now.weekday()
print(day_of_week)

if day_of_week==5:
    with open("quotes.txt") as quotes:
       list_quotes= quotes.readlines()
       print(list_quotes)
    random_quote=choice(list_quotes)
    my_email="ayushjaju8@gmail.com"
    password="jrtc lirn dxmd jbur"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #this makes connection secure
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ayushjaju9@gmail.com",
                            msg=f"subject:Quote of Day\n\n{random_quote} ")