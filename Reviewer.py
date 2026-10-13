# INPUTS
owner_age = int(input("Enter owner age: "))
monthly_revenue = float(input("Enter monthly revenue: "))
credit_score = int(input("Enter credit score: "))
years_in_business = float(input("Enter years in business: "))
has_defaults = input("Has defaults? (True/False): ")
collateral_name = input("Enter collateral name: ")
collateral_value = float(input("Enter collateral value: "))


# BASELINE CHECK
if owner_age >= 21 and years_in_business >= 2.0 and has_defaults == "False":

    # TIER 1
    if credit_score >= 720:
        max_loan = 3 * monthly_revenue

        if monthly_revenue >= 50000:
            base_fee = 0.015
        else:
            base_fee = 0.025

        # COLLATERAL CHECK
        if collateral_value >= max_loan:
            # Continue with the remaining fee rules here
            pass
        else:
            print("Rejected: Insufficient collateral value")

    # TIER 2
    elif credit_score >= 620:
        max_loan = 1.5 * monthly_revenue

        if years_in_business >= 5.0:
            base_fee = 0.02
        else:
            base_fee = 0.035

        # COLLATERAL CHECK
        if collateral_value >= max_loan:
            # Continue with the remaining fee rules here
            pass
        else:
            print("Rejected: Insufficient collateral value")

    # TIER 3
    else:
        print("Rejected: Credit score below requirement")

else:
    print("Rejected: High Risk Application or Ineligible Owner")