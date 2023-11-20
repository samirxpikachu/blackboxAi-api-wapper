from termcolor import colored

def display_input(query):
    print(colored(f"Input: {query}", "red"))

def display_output(answer):
    print(colored(f"Output: {answer}", "green"))
  