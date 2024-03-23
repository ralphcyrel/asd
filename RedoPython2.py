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
name = input("Enter your name: ")
# will ask the user to input his/her name
dream_job = input("Enter your dream job: ")
# will ask the user to input his/her address
address = input("Enter your address: ")
# will ask the user to input his/her email address
email_address = input("Enter your email address: ")

#printing of input value
print_color(f"Hello, My name is {name}", 'cyan')
print_color(f"My dream job is {dream_job}", 'magenta')
print_color(f"my address is {address}", 'red')
print_color(f"my email address is {email_address}", 'yellow')

if __name__ == '__main__':
    main()
