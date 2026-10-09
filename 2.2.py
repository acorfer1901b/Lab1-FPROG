"""Write a program that asks the user for their full name (which they may type using any mix of upperand lower-case letters) and then prints it three times: once fully in lower case, once fully in upper case,
and once with only the first letter of each word capitalised."""

full_name = input("Enter your full name: ")

print(full_name.lower())
print(full_name.upper())
print(full_name.title())