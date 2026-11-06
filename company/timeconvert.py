import time
from company.branches import BRANCHES, get_branch

TIME_FORMAT = "%A, %d %B %Y  %I:%M:%S %p"

def get_local_time(offset):
    """Return the local time for the given UTC offset."""
    return time.gmtime(time.time() + offset * 3600)

def format_time(t):
    """Return a formatted string representation of the given time tuple."""
    return time.strftime(TIME_FORMAT, t)

def get_branch_time(code):
    """Return the current time at the branch with the given code."""
    branch = get_branch(code) 

    if branch is None:
        return None 

    local_time = get_local_time(branch["offset"])
    return format_time(local_time) 

def hour_difference(from_code, to_code):
    """Return the hour difference between two branches."""
    from_branch = get_branch(from_code) 
    to_branch = get_branch(to_code) 

    if from_branch is None or to_branch is None:
        return None 

    return to_branch["offset"] - from_branch["offset"] 


def convert_time(hour, minute, from_code, to_code):
    """Return the converted hour, minute, and day change."""
    difference = hour_difference(from_code, to_code)

    if difference is None:
        return None

    total = hour * 60 + minute + difference * 60
    day_change = total // 1440
    total = total % 1440

    new_hour = total // 60
    new_minute = total % 60

    return new_hour, new_minute, day_change

def describe_day_change(day_change):
    """Return a string describing the day change."""
    if day_change > 0:
        day_change_text = "(next day)"
    elif day_change < 0:
        day_change_text = "(previous day)"
    else:
        day_change_text = "(same day)"
    return day_change_text