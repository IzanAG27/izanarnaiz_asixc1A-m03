import random

def help_command(command):
    if command == "fdisk":
        return "fdisk is a dialog-driven program for creation and manipulation of partition tables."
    else:
        return f"{command} command not found, 'User BACALAO'"

def version_command(command):
    if command == "fdisk":
        return "v0.1"
    else:
        return f"{command} command not found, 'User BACALAO'"

def invalid_option(command, option):
    return f"Value {option} is not valid option, 'User BACALAO'"

def no_option_provided(command):
    if command == "fdisk":
        return "fdisk needs one parameter. For instance -v or -h"
    else:
        return f"{command} command not found, 'User BACALAO'"

def welcome_message():
    welcome_phrases = ["Welcome to our application!", "Glad to see you again!", "Let's get started!", "Ready for a new adventure?"]
    return random.choice(welcome_phrases)


print(welcome_message())

commands = {
    "touch": None,
    "grep": None,
    "cat": None,
    "fdisk": None,
    "cmp": None,
    "dmesg": None,
    "man": None,
    "top": None,
    "htop": None,
    "halt": None,
}

while True:
    user_input = input().split()
    command = user_input[0]
    option = user_input[1] if len(user_input) > 1 else None

    if command not in commands:
        print(f"{command} command not found, 'User BACALAO'")
    else:
        if option == "-h" or option == "--help":
            print(help_command(command))
        elif option == "-v" or option == "--version":
            print(version_command(command))
        elif option is None:
            print(no_option_provided(command))
        else:
            print(invalid_option(command, option))