import math
def get_input():
    first = int(input("Enter start number: "))
    second = int(input("Enter end number: "))
    return first, second
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def display(n):
    print(n)
def main():
    first, second = get_input()
    for n in range(first, second + 1):
        if prime(n):
            display(n)
main()