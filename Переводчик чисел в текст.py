a = int(input("Введите число от 1 до 5: "))
text = "Соотвестствующее слово: "

if a <1 or a > 5:
    print("Число вне допустимого диапазона")
elif a == 1:
    print(text, "one")
elif a == 2:
    print(text, "two")
elif a == 3:
    print(text, "three")
elif a == 4:
    print(text, "four")
else:
    print(text, "five")