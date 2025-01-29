def get_input():
    salary=int(input("enter your monthly salary : "))
    age=int(input("enter your age : "))
    credit_score=int(input("enter your credit score : "))
    return (salary,age,credit_score)
def main():
    (salary,age,credit_score)=get_input()
    if credit_score<800:
        print("loan rejected due to low credit score")
    elif age<20 and age>60:
        print(" loan rejected age must be between 20 to 60 years to applay loan")
    elif salary<=10000:
        print("loan rejected salary must be greater than 10000 per month to apply loan")
    elif salary>10000 and credit_score>800 and age>20 and age<60:
        print("loan approved")
main()
    