# --------------------------------------------------------------------------------------------------------
# Project Title: Allowance Budget Planner
# Group members: Darmi Chloe O. Dumago, Jazzrell Lou De Gracia, Zhaina Guinevere P. Erbito
# The Allowance Budget Planner is a simple Python program that helps a student track their
# allowance, record expenses, and check their remaining balance using a menu until they choose to exit.
# --------------------------------------------------------------------------------------------------------

# Function 1: Get a valid number from the user
def GetNumber(prompt):
    while True:
        user_input = input(prompt)

        if user_input == "":
            print("Input cannot be empty. Try again.")
        else:
            try:
                value = float(user_input)
                if value < 0:
                    print("Please enter a positive number.")
                else:
                    return value
            except:
                print("Invalid input. Please enter a number.")


# Function 2: Show budget summary
def ShowSummary(allowance, expenses):
    total_expense = sum(expenses)
    savings = allowance - total_expense

    print("\n--- Budget Summary ---")
    print("Total Allowance:", allowance)
    print("Total Expenses:", total_expense)

    # Decision structure
    if savings > 0:
        print("Savings:", savings)
    elif savings == 0:
        print("You used all your money.")
    else:
        print("You overspent by:", savings * -1)


# MAIN PROGRAM

print("--- Allowance Budget Planner ---")

# Input allowance
allowance = GetNumber("Enter your allowance: ")

expenses = []

# Loop to add expenses
while True:
    print("\n1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        expense = GetNumber("Enter expense amount: ")
        expenses.append(expense)
        print("Expense added.")

    elif choice == "2":
        ShowSummary(allowance, expenses)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
