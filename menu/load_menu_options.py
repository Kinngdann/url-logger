
def load_menu_options(options: dict):
    while True:
        for i, option in enumerate(options.keys()):
            print(i, option)

        response = input("\nEnter a response: ")
        if response in range(len(options)):
            return options[response]
