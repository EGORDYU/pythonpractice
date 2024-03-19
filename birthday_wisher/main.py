import smtplib
import datetime as dt
import random


def send_inspirational_message():
    now = dt.datetime.now()
    weekday = now.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    my_email = "egordyuzhev@gmail.com"
    password = "hycwdqpxsrhhacne"

    with open("quotes.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()

    random_line = random.choice(lines).strip()

    message = f"Subject:Automated {days[weekday]} Inspiration Message\n\n" \
              f"This is your {days[weekday]} inspirational message. Be inspired. \n{random_line}"
    encoded_message = message.encode('utf-8')  # Explicitly encode the message in UTF-8

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="kristina.manukyan1998@gmail.com", msg=encoded_message)

send_inspirational_message()