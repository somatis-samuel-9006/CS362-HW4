def full_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    if(first_name == "" or last_name == ""):
        return "Full name cannot be generated as 1 or more names were not entered"
    else:
        return f"Your full name is {first_name} {last_name}"
