# 1. Get input from the user
age = int(input("Enter your age: "))

# 2. Check if age is great or equal to 18
if (age >= 18):
    print("You are eligable to vote")
else:
    print("You are not eligible to vote.")
    print(f"You will be eligible in {18 - age} years.")
    print("Countdown from your age:")

    while (age >= 0):
        if (age != 0):
            print(age, end=", ")
        else:
            print(age)
        age = age - 1