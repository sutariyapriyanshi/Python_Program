import time
timestamp = time.strftime('%I:%M:%S')
print(timestamp)
timestamp = time.strftime('%I')
print("Hour is      ->",timestamp)
timestamp = time.strftime('%M')
print("Minutes is   ->",timestamp)
timestamp = time.strftime('%S')
print("Seconds is   ->",timestamp)
if(timestamp > '3:00:00' and timestamp <= '12:00:00'):
    print("Good Morning Sir")
elif(timestamp > '12:00:00' and timestamp <= '6:00:00'):
    print("Good Afternoon sir")
elif(timestamp > '6:00:00' and timestamp <= '9:00:00'):
    print("Good Evening sir")
else:
    print("Good Night")
# https://docs.python.org/3/library/time.html#time.strftime