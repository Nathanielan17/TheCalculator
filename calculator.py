from funcs import Operate

def main():
    print("Welcome to TheCalculator!\nType in 'exit' to close out.\n")
    
    while True:
        statement = input("> ").strip() # takes in user input eg. 2+2
        if statement == 'exit':
            break
        result = Operate(statement)
        if result == "Error":
            print("> please enter a proper statement to be calculated")
            continue
        print(">", result)


main()

