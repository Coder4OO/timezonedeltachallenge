#Time zone challenge by Coder400
#Task: Calculate time difference between two dates and timezones.
#Time library is banned in this challenge >:)
import c400date
import c400timezones

running = False

def start():
    global running
    if not running:
        running = True

def stop():
    global running
    if running:
        running = False

def take_int(prompt):
    err = True
    while err:
        try:
            ans = int(input(prompt))
            err = False
        except ValueError:
            print("Please enter a number.")
    return ans

def create_date():
    sec = take_int("Please Enter number of seconds: ")%60
    mins = take_int("Please Enter number of minutes: ")%60
    hrs = take_int("Please Enter number of hours: ")%24
    day = take_int("Please Enter number of day in the month: ")%12
    month = take_int("Please Enter the number of the month: ")
    year = take_int("Please Enter the year of the date: ")
    err = True
    while err:
        timezone = input("Please Enter name of timezone: ")
        timezone = c400timezones.retrieve_timezone_by_name(timezone, "timezones.json")
        if isinstance(timezone, c400timezones.Timezone):
            err = False
        else:
            print("Please enter valid timezone name.")
    return c400date.Date(sec, mins, hrs, day, month, year, timezone)

start()
while True:
    menu = input("\t\t Delta in seconds of two dates\n\n\t\tMenu:\n1.Calculate Delta\n2. Quit")
    if menu == "1":
        d1 = create_date()
        d2 = create_date()
        delta = d1.delta_time(d2)
        print("The difference is %s seconds." % delta)
    elif menu == "2":
        print("Exiting program...")
        stop()
    else:
        print("Enter a number between 1 and 2.")