correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("\nEnter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

message = "Hi %s %s, you are logged in" %(name, surname)
print(message)
