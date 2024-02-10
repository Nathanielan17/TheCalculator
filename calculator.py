from funcs import ops, add, subtract, multiply, division

def main():
    print("Welcome to TheCalculator!\nType in 'exit' to close out.")
    
    while True:
        statement = input("> ").strip().replace(" ", "") # takes in user input eg. 2+2
        num1,num2 = statement[0],statement[2]
        if statement == 'exit':
            break

        match statement[1]:
            case '+':
                print(">", add(num1,num2))
                continue
            case '-':
                print(">", subtract(num1,num2))
                continue
            case '*':
                print(">", multiply(num1,num2))
                continue
            case '/':
                print(">", division(num1,num2))
                continue
            case _:
                print(">", statement)
                continue
        

main()

