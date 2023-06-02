import re
def check_passw(passw):
    pattern=r"(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]{8,}"
    x=re.match(pattern,passw)
    if x:
        print("correct password")
    else:
        print("No match")

passw= input('Enter your password:')
check_passw(passw)