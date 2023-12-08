

def format_name(first, last):
    """Take a first and last name and format it to return the title case version of the name."""
    if first == "" or last == "":
        return
    f_name = first.title()
    l_name = last.title()
    return f"{f_name} {l_name}"



print(format_name(input("What is your first name?"), input("What is your last name? ")))

