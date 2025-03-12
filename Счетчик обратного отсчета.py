start_time = int(input("Enter a number to begin a countdown: "))
if start_time < 0:
    print("You should enter a positive number")

while start_time > -1:
    print(start_time)
    start_time -= 1
