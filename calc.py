def add():
	sum = int(input("Enter the first number: ")) + int(input("Enter the second number:"))
	print("the addition of two numbers is:", sum)
def sub():
	diff = int(input("Enter the first number: ")) - int(input("Enter the second number:"))
	print("the subtraction of two numbers is:", diff)

def mult():
	mul = int(input("Enter the first number: ")) * int(input("Enter the second number:"))
	print("the multiplication of two numbers is:", mul)

if __name__ == "__main__":
	add()
	sub()
	mult()
