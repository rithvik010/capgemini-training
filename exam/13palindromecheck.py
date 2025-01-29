def get_input():
    return input("Enter a string or number \n(type 'exit' to quit): ")
def is_palindrome(s):
    s = str(s)
    return s == s[::-1]
def main():
    while True:
        user_input = get_input()
        if user_input.lower() == 'exit':
            print("Thank you")
            break
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"{user_input} is not palindrome")
main()