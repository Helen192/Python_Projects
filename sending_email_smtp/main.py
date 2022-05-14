##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import random
import smtplib
import datetime as dt

# check the current day and month
now = dt.datetime.now()
current_month = now.month
current_day = now.day

MY_EMAIL = "phuonghuongnguyen192@gmail.com"
PASSWORD = "huong192"

# reading .csv file
dataset = pd.read_csv("birthdays.csv")
list_dict_birthdays = dataset.to_dict(orient="records")


for person in list_dict_birthdays:
    # find peoples in the list of birthdays who have birthday today and create automatic emails for them
    if person['month'] == current_month and person['day'] == current_day:
        name = person['name']
        # choosing a letter at random
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as letter:
            content_letter = letter.read()
            final_letter = content_letter.replace('[NAME]', name)

        #with open(f"letter_{name}.txt", 'w') as sending:
            #sending.writelines(final_letter)

    # sending created email to them
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person['email'],
            msg=f"Subject: Happy Birthday\n\n{final_letter}"
        )





