def leap_check(year):
    if year%4==0:
        return True
    else:
        return False
def main():
    while True:
        choice=int(input("1.to enter year \t2.to exit :"))
        if choice==1:
            year=int(input("enter year : "))
            if leap_check(year):
                print(f"{year} is leap year ")
            else:
                print(f"{year} is not leap ")
        elif choice>2:
            print("invalid input ")
        else :
            return False
main()
            