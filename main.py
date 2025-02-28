# Simple Tip Calculator

print("Welcome to the tip Calculator")
Bill = float(input("What is the total bill?\n$"))
Tip = int(input("What percentage tip would like to give? 10, 12, 15:\n"))
People = int(input("How many people to split bill?\n"))
Tip_as_percent =Tip / 100
Total_tip_amount = Bill * Tip_as_percent
Total_bill = Bill + Total_tip_amount
Bill_per_person = Total_bill / People
Final_Amount = round(Bill_per_person,2)
print(f"Each person should pay:\n${Final_Amount}")