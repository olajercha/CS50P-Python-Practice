"""In a file called camel.py, implement a program that prompts the user
for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case."""


def camel_to_snake(camel_str):
    snake_list = []

    for char in camel_str:
        if char.isupper():
            if snake_list:
                snake_list.append("_")
            snake_list.append(char.lower())
        else:
            snake_list.append(char)

    snake_str = "".join(snake_list)
    return snake_str


def main():
    print("Enter a variable name in camelCase. Type 'exit' to quit or press Ctrl+C to stop.")

    while True:
        camel_input = input("camelCase: ")

        if camel_input.lower() == "exit" or camel_input.lower() == "quit":
            print("Program terminated.")
            break

        snake_output = camel_to_snake(camel_input)

        print("snake_case:", snake_output)


if __name__ == "__main__":
    main()
