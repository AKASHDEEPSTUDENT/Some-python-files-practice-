import datetime

current_time = datetime.datetime.now()
hour = current_time.hour

if 6 <= hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 18:
    greeting = "Good afternoon"
elif 21 <= hour <24:
    greeting= "Good night"
else:
    greeting = "Good evening"

print(greeting + "!")
