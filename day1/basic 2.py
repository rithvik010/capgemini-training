def display(data):
    print(f"the area is {data}")
def get_input():
    length=int(input("length "))    
    width=int(input("width "))

    return (length,width)
def compute(length , width):
    return length*width
def main():
    (length,width)=get_input()
    area=compute(length,width)
    display(area)
