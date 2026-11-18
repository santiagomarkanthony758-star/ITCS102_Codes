
#String formatting

loan_amt = float(input("Enter the loan amount --->"))
years = int(input("Enter the number of years --->"))

month = years * 12
principal = loan_amt / month
remaining_balance = loan_amt

#for loop
print(f"{'MONTH':<10}{'PAYMENT':<15}{'INTEREST':<15}{'PRINCIPAL':<15}{'BALANCE':<15}")

for count in range(1, month + 1):
    rem_bal = principal
    interest = rem_bal * 0.00256
    pay = interest + principal

    print(f"{count:<10}{round(pay, 2):<15}{round(interest, 2):<15}{round(principal, 2):<15}{round(rem_bal, 2):<15}")

print("total")
