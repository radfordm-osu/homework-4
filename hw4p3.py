def NameGen(first, last):
    if (isinstance(first, str) and isinstance(last, str)):
        name = first + " " + last
        return name
    else:
        return "Error!"
