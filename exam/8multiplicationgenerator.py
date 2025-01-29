def get_input():
    number=int(input("enter the number want to generate the table "))
    range_upto=int(input("enter range upto table can display "))
    return(number,range_upto)
def display(number,i):
    print(f"{number} x {i} = {number*i}")


def main():
    (number,range_upto)=get_input()
    for i in range(1,range_upto+1):
        display(number,i)

main()