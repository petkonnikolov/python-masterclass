import time

print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
print("The current timezone is {0} with an offset 0f {1}".format(time.tzname[0], time.timezone))

