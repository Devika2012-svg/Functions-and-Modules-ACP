print("--------IS YOUR AGE EVEN OR ODD!?--------")
print("\n 1. Only numbers can be entered.")
print(" 2. No decimals, letters, or special chracters are allowed. If entered an error message will be shown.")

try:
    age = input("\n Enter your age: ")
    age = int(age)

    if age < 0:
        print("Age cannot be negative.")
    elif age % 2 == 0:
        print("Your age is an even number.")
    else:
        print("Your age is an odd number.")

except ValueError:
    print("Please enter a valid whole number (no decimals, letters, or special characters are allowed).")
