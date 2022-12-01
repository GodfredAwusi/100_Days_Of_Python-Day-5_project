import random
# Write a program that generates a random password based on the user's preference of how many letters, numbers and symbols they want in the password

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '(', ')', '*', '+']

# print(random.choice(alphabets))

print("Welcome to the Cosby Password Generator!")
no_letters = int(input("How many letters would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your password?\n"))

password = []
for l in range(no_letters):
    password += random.choice(alphabets)

for n in range(no_numbers):
    password += random.choice(numbers)

for s in range(no_symbols):
    password += random.choice(symbols)

# password = random.sample(password, len(password))
# print(password)
random.shuffle(password)
# print(password)

generated_password = ""
for char in password:
    generated_password += char

print(f"Your generated password is: {generated_password}")






