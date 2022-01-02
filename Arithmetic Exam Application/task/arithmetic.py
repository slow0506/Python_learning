import random
one_two = True
while one_two:
    level = input("1 - simple operations with numbers 2-9\n2 - integral squares 11-29\n")
    if int(level) == 1 or int(level) == 2:
        choice = int(level)
        one_two = False
    else:
        print("re-enter")

time = 0
count = 0
while time < 5:
    if choice == 1:
        sign = random.choice(["+", "-", "*"])
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        print(x, sign, y)
        if sign == "+":
            result = x + y
        if sign == "-":
            result = x - y
        if sign == "*":
            result = x * y
    elif choice == 2:
        x = random.randint(11, 29)
        print(x)
        result = x * x


    go_on = True
    while go_on == True:
        answer = input()
        if answer.strip("-").isdigit():
            go_on = False
            answer = int(answer)
            if answer == result:
                print("Right!")
                count +=1
            else:
                print("Wrong!")
            time +=1
        else:
            print("Incorrect format.")

print(f"Your mark is {count}/5")

record = input("Would you like to save your result to the file? Enter yes or no.")
if record in ["yes", "YES", "y", "Yes"]:

    name = input("What's your name?")
    print("The results are saved in 'results.txt'")
    file = open("results.txt", "a", encoding='utf-8')
    if choice == 1:
        file.write(f"{name}: {count}/5 in level {choice} (simple operations with numbers 2-9).")
    elif choice == 2:
        file.write(f"{name}: {count}/5 in level {choice} (integral squares 11-29).")
    file.close()
else:
    exit()



