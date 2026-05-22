def count_total_expense(expenses):
    total_expense = 0
    for expense in expenses:
        total_expense += float(expense)

    return total_expense


def count_average_expense(expenses):
    average_expense = count_total_expense(expenses) / len(expenses)

    return average_expense
    

print("Welcome to the Daily Expense Tracker!")

print("""
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")

expenses_list = []

while True:
    menu_choice = input()

    if menu_choice == "1":
        expense = float(input())
        expenses_list.append(expense)
        
        if expenses_list:
            print("Expense added successfully!")

    elif menu_choice == "2":
        if not expenses_list:
            print("No expenses recorded yet.")
        
        else:
            print("Your expenses:")
            # output in seperate lines 1. x, 2. y, 3. z
            for indx in range(len(expenses_list)):
                print(f"{indx + 1}. {expenses_list[indx]}")

    elif menu_choice == "3":
        if not expenses_list:
            print("No expenses recorded yet.")
        
        else:
            print(f"Total expense: {count_total_expense(expenses_list)}")
            print(f"Average expense: {count_average_expense(expenses_list)}")

    elif menu_choice == "4":
        expenses_list.clear()
        print("All expenses cleared.")

    elif menu_choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")