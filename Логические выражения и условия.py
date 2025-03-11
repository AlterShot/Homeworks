import sys

try:
    age = int(input("How old are you? "))
    if age >= 18 and age < 100:
        permission = True
    else:
        permission = False
except ValueError:
    print("What you\'ve entered is not a number. Try again later")
    permission = False
    sys.exit()

answer = input("Are you a citizen of Russia? (yes/no) ").lower()
if answer == "yes":
    citizenship = True
elif answer == "no":
    citizenship = False
else:
    print("Data is not correct")
    sys.exit()

law = str(input("Were you involved in crime? (yes/no) "))
if law.lower() == "no":
    allowed = True
elif law == "yes":
    allowed = False
else:
    print("Data is not correct")
    sys.exit()

if permission and citizenship and allowed:
    print("You are able to vote")
else:
    print("You are not able to vote")