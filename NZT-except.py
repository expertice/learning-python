count = 0

while count < 5:
    try:
        age = int(input("Enter your age: "))
        print(f"Your age is {age}")
        break
    except ValueError as e:
        print(f"You entered wrong age {e} detected")
    finally:
        print(f"It's ok anyway")

    count += 1


