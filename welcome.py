def welcome_student(name="Student"):
	return f"Welcome to PLP, {name}!"


# Call the function with a name
message = welcome_student("Bahati")
print(message)

# Call the function using the default value
message = welcome_student()
print(message)
