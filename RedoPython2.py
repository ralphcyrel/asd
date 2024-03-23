#the color of the text
def print_color(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
    end_color = '\033[0m'
    print_color = f"{colors[color]}{'*' * len(text)}\n{text}\n{'*' * len(text)}{end_color}"
    print(print_color)
def main ():
# will ask the user to input his/her name
# will ask the user to input his/her name
# will ask the user to input his/her address
# will ask the user to input his/her email address
