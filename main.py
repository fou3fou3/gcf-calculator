#gcf calculator

print("you only input 2 numbers to extract the gcf from . \n\n")
print("Enter the biggest number first .\n\n")

num_1 = int(input("Enter the first number  : "))
num_2 = int(input("Enter the second number  : "))

def calculate(n1,n2):
    n1 = num_1
    n2 = num_2
    num_3 = n1%n2
    while num_3 > 0 :
        n1 = n2
        n2 = num_3
        num_3 = n1%n2
    print(f"the gcf for {num_1} and {num_2} is {n2}.")

calculate(num_1, num_2)