# Expense Tracker Project

# 1. Create an empty list to store expenses
expenses = []

# 2. Define the function for main menu
def show_menu():
	print('\n---Expense Tracker Menu---')
	print('1. Add an Expense')
	print('2. View expenses')
	print('3. Calculate total expenses')
	print('4. Exit')

# 3. Define the function to add an expense
def add_exp():
	item = input('Enter the item: ')
	cost = input('The cost of the item is: ')

	try:
		cost = float(cost)
		expenses.append({"item": item, "cost": cost})
		print(f'Added: {item} - Rs. {cost:.2f}')
	except ValueError:
		print('Invalid cost. Please enter a number')

# 4. Define the function to view expenses
def view_exp():
	if not expenses:
		print('No expenses recorded.')
	else:
		print('\n---List of expenses---')
		for i, expense in enumerate(expenses, start=1):
			print(f'{i}. {expense['item']} - Rs. {expense['cost']:.2f}')

#5. Define the function to calculate the total expenses
def total_exp():
	total = sum(expense['cost'] for expense in expenses)
	print(f'\nTotal Expenses: Rs. {total:.2f}')

#6 Main program loop
while True:
	show_menu()
	choice = input('Enter your choice(1-4): ')

	if choice == '1':
		add_exp()
	elif choice == '2':
		view_exp()
	elif choice == '3':
		total_exp()
	elif choice == '4':
		print('Exiting the program. Goodbye.')
		break
	else:
		print('Invalid choice. Please choose a valid option.')
