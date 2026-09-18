print("Hello, World!")
age = int(input("What is your age? =====>"))
credit_score = int(input("What is your credit score? =====>"))
is_employed = bool(input("Are you employed? =====>"))
annual_income = float(input("What is your annual income? =====>"))
has_collateral = bool(input("Do you have collateral? =====>"))
base_rate = 0.0


if age >= 21 and is_employed == True: 
    print("You are eligible for a loan.")
    if credit_score >= 750:
        if annual_income >= 100000:
            base_rate = 4.5
            print("Your base rate is now", base_rate)
        else:
            base_rate = 5.0
            print("Your base rate is now", base_rate )
    elif credit_score >= 600 and credit_score < 750: 
        print("Your credit score is less than 750")
        if has_collateral == True:
            base_rate = 7.0
            print("Your base rate is now", base_rate)
        elif annual_income <= 40000:
            base_rate = 9.5
            print("Your base rate is now ", base_rate)
        else: 
            base_rate = 8.0
            print("Your base rate is now", base_rate)    
    elif  credit_score <= 600:
      print("credit score is to low") 
else:
    print("invalid")
