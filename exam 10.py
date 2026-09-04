correct_password = 2468
attempt = 1

while attempt <= 3:
    password = int(input("Enter password: "))

    if password == correct_password:
        print(" Login successful")
        break
    else:
        print(" Incorrect password")

    attempt += 1

if attempt > 3:
    print("Account locked")


secret = 37
count = 0

while True:
    guess = int(input("Enter guess: "))
    count += 1

    if guess < secret:
        print(" Too low")
    elif guess > secret:
        print(" Too high")
    else:
        print(" Correct")
        break

print(f"Total guesses: {count}")



total = 0
items = 0
while True:
    price = int(input("Enter item price (or 0 to finish): "))
    if price == 0:
        break
    total += price
    items += 1

balance = 5000
while True:
    print("menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds")
    elif choice == 3:
        print(f"Balance: {balance}")
    elif choice == 4:
        break
    else:
         print("atm closed")


passengers = 0

while True:
    command = input("Enter command (in/out/stop): ")

    if command == "in":
        if passengers < 40:
            passengers += 1
        else:
            print("Bus is full!")

    elif command == "out":
        if passengers > 0:
            passengers -= 1
        else:
            print("Bus is empty!")
    elif command == "stop":
        break
    else:
        print("Invalid command!")

print("Final passenger count:", passengers)


num = int(input("Enter a positive integer: "))
target = int(input("Enter target digit: "))

count = 0

while num > 0:
    digit = num % 10

    if digit == target:
        count += 1

    num = num // 10

print("Digit", target, "occurred", count, "times")

num = int(input("Enter a positive integer: "))
steps = 0

while num != 1:
    print(num, end=" -> ")

    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

    steps += 1

print(1)
print("Steps required:", steps)

correct_username = "admin"
correct_password = "python123"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username:
        print("Unknown user")
    elif password != correct_password:
        print("Wrong password")
    else:
        print("Welcome")
        break

    attempts += 1

if attempts == 3:
    print("Account locked")

score = 0
question = 1

while question <= 5:

    if question == 1:
        answer = input("1. What is the capital of India? ")
        if answer.lower() == "delhi":
            score += 1
    elif question == 2:
        answer = input("2. How many days are there in a week? ")
        if answer == "7":
            score += 1
    elif question == 3:
        answer = input("3. What is 5 + 3? ")
        if answer == "8":
            score += 1
    elif question == 4:
        answer = input("4. who is hero for movie salaar? ")
        if answer.lower() == "prabhas":
            score += 1
    elif question == 5:
        answer = input("5. at what time did the python class begins everyday? ")
        if answer == "3.45":
            score += 1

    question += 1

print("\nYour score:", score, "/ 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
elif score >= 1:
    print("Needs Practice")
else:
    print("Try Again")

stock = 20
while True:
    command = input("Enter add/sell/stop: ")

    if command == "stop":
        break

    qty = int(input("Enter quantity: "))

    if qty <= 0:
        print("Invalid quantity")
    elif command == "add":
        stock += qty
    elif command == "sell":
        if qty <= stock:
            stock -= qty
        else:
            print("Not enough stock")

print("Final stock:", stock)

health = 100
while health > 0:
    action = input("Enter action: ")
    if action == "damage":
        health -= 20
    elif action == "heal":
        health = min(100, health + 15)
    elif action == "potion":
        health = min(100, health + 30)
    elif action == "quit":
        break
    else:
        print("Invalid action!")
        continue
    health = max(0, health)
    print("Health:", health)

balance = 8000
deposit = withdrawal = failed = 0
while True:
    amount = float(input("Enter amount: "))
    if amount == 0:
        break
    elif amount > 0:
        balance += amount
        deposit += 1
    elif -amount <= balance:
        balance += amount
        withdrawal += 1
    else:
        failed += 1
print("Balance:", balance)
print("Deposits:", deposit)
print("Withdrawals:", withdrawal)
print("Failed:", failed)


state = "OFF"

while True:
    command = input("Enter command: ").lower()

    if command == "start" and state == "OFF":
        state = "RUNNING"
    elif command == "pause" and state == "RUNNING":
        state = "PAUSED"
    elif command == "resume" and state == "PAUSED":
        state = "RUNNING"
    elif command == "shutdown" and state != "OFF":
        state = "OFF"
        print("Machine shut down.")
        break
    else:
        print("Invalid command.")

    print("Current state:", state)

total = 0
largest = 0
while True:
    expense = float(input("Enter expense: "))
    if expense == 0:
        break
    elif expense < 0:
        print("Invalid expense")
        continue
    total += expense
    largest = max(largest, expense)

    if expense < 500:
        print("Small expense")
    elif expense < 2000:
        print("Medium expense")
    else:
        print("Large expense")
print("Total expense:", total)
print("Largest expense:", largest)

score = 0
while True:
    command = input("Command: ").lower()
    if command == "quit":
        break
    elif command == "win":
        score += 10
    elif command == "bonus":
        score += 25
    elif command == "miss":
        score = max(0, score - 5)
    else:
        print("Invalid command")
        continue
    if score < 20:
        level = "Beginner"
    elif score < 50:
        level = "Intermediate"
    elif score < 80:
        level = "Advanced"
    else:
        level = "Expert"
    print(score, level)