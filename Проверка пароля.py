origin_password = "Qwerty1234"

count_to_try = 3

while count_to_try != 0:

    user_password = input("Enter your password: ")
    count_to_try -= 1

    if user_password == origin_password:
        print("Password is correct")
        break
    else:
        if count_to_try > 0:
            print(f"Password is incorrect. You have {count_to_try} more attempts.")
        else:
            print("No more attempts left. Good luck next time.")