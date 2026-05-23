import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2027, 4, 25)
time_difference = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {time_difference.days} days away.")