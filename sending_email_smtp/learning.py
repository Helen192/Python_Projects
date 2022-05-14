import smtplib

#my_email = "phuonghuongnguyen192@gmail.com"
#password = "    "
#
#connection = smtplib.SMTP("smtp.gmail.com", port=587)
#connection.starttls()
#connection.login(user=my_email, password=password)
#connection.sendmail(
#    from_addr=my_email,
#    to_addrs="huongpng192@yahoo.com",
#    msg="Subject:Testing email\n\nHello Helen. This is the body of the email")
#connection.close()

# using with
#with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(
#        from_addr=my_email,
#        to_addrs="huongpng192@yahoo.com",
#        msg="Subject:Testing email\n\nHello Helen. This is the body of the email")

import smtplib
import random
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "phuonghuongnguyen192@gmail.com"
password = "huong192"
if day_of_week == 4:
    with open("quotes.txt", "r") as file:
        quote = random.choice(file.readlines())

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="huongpng192@yahoo.com",
            msg=f"Subject: Quote of day\n\n{quote}")


