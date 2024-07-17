from datetime import date

def calculate_age(birthday):
    today = date.today()

    # Check if the birthdate is in the future
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    year_diff = today.year - birthday.year

    # Adjust the year difference if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthday.month, birthday.day):
        year_diff -= 1

    # Calculate remaining months and days
    if today.month >= birthday.month:
        remaining_months = today.month - birthday.month
    else:
        remaining_months = 12 - (birthday.month - today.month)

    if today.day >= birthday.day:
        remaining_days = today.day - birthday.day
    else:
        remaining_days = (date(today.year, today.month, 1) - date(today.year, birthday.month, birthday.day)).days

    
    return f"Age: {year_diff} years, {remaining_months} months, and {remaining_days} days"

if __name__ == "__main__":
    print("Age Calculator By Python")

    try:
        birthYear = int(input("Enter the birth year: "))
        birthMonth = int(input("Enter the birth month: "))
        birthDay = int(input("Enter the birth day: "))
        dateOfBirth = date(birthYear, birthMonth, birthDay)
        age = calculate_age(dateOfBirth)
        print(age)
    except ValueError:
        print("Invalid input. Please enter valid integers for the year, month, and day.")
