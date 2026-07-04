print("""
         ***Welcome to the password Generator!***
        """)
#The length of your password
numbers=int(input("Enter the total number of characters in the password: "))
num_letters=int(input("Enter the number of letters in the password:  "))
num_numbers=int(input("Enter the number of numbers in the password:  "))
num_symbols=int(input("Enter the number of symbols in the password:  "))
#The necessary and sufficient condition for a valid password
if numbers==num_letters+num_numbers+num_symbols:
#Imports
    import random 
    import string
    #To choose random password
    random_letters=random.choices(string.ascii_letters,k=num_letters)
    random_numbers=random.choices(string.digits,k=num_numbers)
    random_symbols=random.choices(string.punctuation,k=num_symbols)
    random_password=random_letters+random_numbers+random_symbols
    random.shuffle(random_password)
#creating your password
    your_password=("".join(random_password))
    print(f"Generated Password: {your_password}")
else:
    print("Invalid input.The sum of letters,numbers,and symbols doesn't match the total number of characters in the password ")    
