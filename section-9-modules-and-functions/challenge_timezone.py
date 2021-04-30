# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import datetime
import pytz

all_list = []
for x in pytz.all_timezones:
    all_list.append(x)

all_timezones = all_list[:(50 * 10):60]

menu_dict = {(i + 1) : all_timezones[i] for i in range(0, len(all_timezones))}

# print(menu_dict)

# while True:
#     print("Choose a timezone from the list:")
#     for number, time_zone in enumerate(all_timezones):
#         print("\t{}. {}".format(number + 1, time_zone))

while True:
    print("Choose a timezone from the list:")
    for zone in menu_dict.items():
        print("{}: {}".format(zone[0], zone[1]))

    user_input = int(input("Your choice: "))
    if user_input == 0:
        break
    else:
        tz_to_display = pytz.timezone(menu_dict[user_input])
        tz_current_time = datetime.datetime.now(tz=tz_to_display)

        print("The time in {} is {} {}".format(all_timezones[user_input -1], tz_current_time.strftime('%A %x %X %z'), tz_current_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X %z')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X %z')))
        print()
        #print("{} Time: {}".format(time_zone, tz_current_time))
        # print("{} Time: {}, Local Time: {}, UTC Time: {}".format(tz_to_display, tz_current_time, local_time, utc_time))