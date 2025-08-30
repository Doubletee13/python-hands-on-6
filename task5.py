""""
Employee Shift Manager
You are asked to build a small program to help manage employee work shifts in a company.  
Create a dictionary `shifts` where each key is an employee's name, and the value is a list of the days they are scheduled to work.  
     shifts = {
       "Alice": ["Monday", "Wednesday"],
       "Bob": ["Tuesday", "Thursday"],
       "Charlie": ["Monday", "Friday"]
   }


fucntion signature function add_shift(employee, day):
The  function should 
1. Checks if the employee exists in the dictionary.

 - If they exist, add the new day to their list (only if it’s not already there).

-  If they don’t exist, create a new key for them with the day inside a list.

-  Return the updated dictionary.


2. Write another function get_schedule(day) that:

Returns a list of employees working on that day.
"""



shifts = {
    "Alice": ["Monday", "Wednesday"],
     "Bob": ["Tuesday", "Thursday"],
     "Charlie": ["Monday", "Friday"]
     }


def add_shift(employee, day):
	if len(employee) != 0 and len(day) != 0:
		if employee in shifts and day not in shifts[employee]:
			shifts[employee].append(day)
		elif employee not in shifts:
			shifts[employee] = [day]
		else:
			print(f"{employee} You are already scheduled to work on {day}")
		return shifts
	else:
		print("Input field cannot be empty")



def get_schedule(day):
	names = []
	if len(day) != 0:
		for employee in updated_shifts:
			if day not in updated_shifts[employee]:
				print(f"{employee} is not scheduled to work on {day}")
			else:
				names.append(employee)
		if len(names) != 0:
			print(f"List of employees working on {day} : {result}")
	else:
		print("Input field cannot be empty")
	

employee = input("enter name of employee: ").capitalize()
day = input("enter days employee is scheduled to work: ").capitalize()



updated_shifts = add_shift(employee, day)
print(updated_shifts)

day = input("enter day to get a list of employees working on that day: ").capitalize()
get_schedule(day)


