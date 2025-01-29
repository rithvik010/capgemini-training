total_bill=float(input("Enter total bill amount "))
total_persons=int(input("enter total number of people "))
tip_percentage=float(input("Enter tip percent "))
final_bill=total_bill*(tip_percentage/100)+total_bill
print(f"Each person has to pay {final_bill/total_persons}")