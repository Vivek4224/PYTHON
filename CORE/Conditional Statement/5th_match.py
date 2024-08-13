"""
match variable:
    case pattern1:
        # action if variable matches pattern1
    case pattern2:
        # action if variable matches pattern2
    case _:
        # action if no pattern matches
"""

# day=int(input("please enter 0 to 6 no."))

import datetime

day = datetime.datetime.now().weekday()

match day:
    case 0:
        print("Today is Monday")
    case 1:
        print("Today is Tuesday")
    case 2:
        print("Today is Wednesday")
    case 3:
        print("Today is Thursday")
    case 4:
        print("Today is Friday")
    case 5:
        print("Today is Saturday")
    case 6:
        print("Today is Sunday")
    case _:
        print("Today is Invalid day")