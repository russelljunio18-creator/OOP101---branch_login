import time
from company import auth, timeconvert
from company.branches import EMPLOYEES, get_branch, get_branch_codes

def show_all_branch_times():
    """Display the current time at every branch."""
    print("\n--- Current time at all branches ---")

    for code in get_branch_codes():
        branch = get_branch(code)
        current_time = timeconvert.get_branch_time(code)
        offset_text = timeconvert.format_utc_offset(branch["offset"])

        print(
            f'{branch["city"]:7s} '
            f'({branch["tz"]}, {offset_text}): {current_time}'
        )

def read_time():
    """Return the entered hour and minute, or None if invalid."""
    text = input("Enter a time in 24-hour format (HH:MM): ")

    if len(text) != 5 or text[2] != ":":
        return None

    hour_text, minute_text = text.split(":")

    if not hour_text.isdecimal() or not minute_text.isdecimal():
        return None

    try:
        hour = int(hour_text)
        minute = int(minute_text)
    except ValueError:
        return None

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        return None

    return hour, minute

def convert_meeting_time(my_code):
    """Display a meeting time at the other two branches."""
    meeting_time = read_time()

    if meeting_time is None:
        print("Invalid time. Use HH:MM, for example 09:30 or 17:45.")
        return

    hour, minute = meeting_time
    my_branch = get_branch(my_code)

    print(f'\n{hour:02d}:{minute:02d} in {my_branch["city"]} is:')

    for code in get_branch_codes():
        if code == my_code:
            continue

        branch = get_branch(code)
        new_hour, new_minute, day_change = timeconvert.convert_time(
            hour, minute, my_code, code
        )
        day_text = timeconvert.describe_day_change(day_change)
        difference = timeconvert.hour_difference(my_code, code)

        print(
            f'  {new_hour:02d}:{new_minute:02d} in {branch["city"]} '
            f'{day_text}  [{difference:+g} h]'
        )

def employee_menu(username):
    """Show the employee menu and report session length on logout."""
    employee = EMPLOYEES[username]
    my_code = employee["branch"]
    branch = get_branch(my_code)
    start = time.time()

    print(
        f'\nWelcome, {employee["name"]}! '
        f'({branch["city"]}, {branch["country"]} branch)'
    )
    print(
        f'Logged in at {timeconvert.get_branch_time(my_code)} '
        f'{branch["tz"]}'
    )

    while True:
        print("\n[1] Show all branch times")
        print("[2] Convert a meeting time")
        print("[3] Logout")
        choice = input("Choose: ").strip()

        if choice == "1":
            show_all_branch_times()
        elif choice == "2":
            convert_meeting_time(my_code)
        elif choice == "3":
            minutes, seconds = divmod(int(time.time() - start), 60)
            print(
                f'Goodbye, {employee["name"]}. '
                f'Session length: {minutes} min {seconds} sec.'
            )
            break
        else:
            print("Invalid choice.")


def main():
    """Run the login system until the user chooses to exit."""
    print("=" * 45)
    print("   GLOBALTECH SOLUTIONS - EMPLOYEE LOGIN")
    print("=" * 45)

    while True:
        username = auth.login()

        if username is not None:
            employee_menu(username)

        while True:
            answer = input("\nLog in again? (y/n): ").strip().lower()

            if answer in ("y", "n"):
                break

            print("Please enter y or n.")

        if answer == "n":
            print("System closed.")
            break


if __name__ == "__main__":
    main()