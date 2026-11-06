import time
from company.branches import BRANCHES, get_branch

TIME_FORMAT = "%A, %d %B %Y  %I:%M:%S %p".

#get the offset and return local time
def get_local_time(offset):
    return time.gmtime(time.time() + offset * 3600)

#get local time and returns formatted
def format_time(t):
    return time.strftime(TIME_FORMAT, t)

#get branch, get offset in the branch dictionary, get local time and formats it
def get_branch_time(code):
    branch = get_branch(code) #get branch dictionary

    if branch is None:
        return None #returns none if branch code is invalid and not in the branch dictionary

    local_time = get_local_time(branch["offset"]) #get offset in the branch dictionary and return local_time
    return format_time(local_time) #get local_time and return it as formatted time

#get hour difference between two branches
def hour_difference(from_code, to_code):
    from_branch = get_branch(from_code) #get branch dictionary of the given code
    to_branch = to_branch(to_code) #get branch dictionary of the given code

    if from_branch or to_branch is None:
        return None #returns none if from/to branch code is invalid and not in the branch dictionary

    return to_branch["offset"] - from_branch["offset"] #returns the difference from to difference to - from

#convert formatted time into hour, minute
def convert_time(hour, minute, from_code, to_code):
    difference = hour_diffrence(from_code, to_code)

    if difference is None:
        return None

    total = hour * 60 + minute + difference * 60
    day_change = total // 1440
    total = total % 1440 
    new_hour = total // 60
    new_minute = total % 60
    return new_hour, new_minute, day_change

def describe_day_change(day_change):
    if day_change > 0:
        day_change_text = "(next day)"
    elif day_change < 0:
        day_change_text = "(previous day)"
    else:
        day_change_text = "(same day)"
    return day_change_text