def monthly():
    monthly_paycheck = int(input("What is your mothly income? ")) #user enters income
   

    total_income = monthly_paycheck
    print(f"Total monthly income is ${round(total_income):,.2f}\n")

    bills = {
    'rent': int(input("How much is this month's rent? ")),
    "utilities": int(input("How much did you spend on utilities? ")),
    "groceries": int(input("What did you spend on groceries? ")),
    "transportation": int(input("Enter your transportation expenses:")),
    "healthcare": int(input("Any Healthcare fees this month?")),
    "personal care": int(input("How much did you spend on personal care? ")),
    "clothing": int(input("Clothing fees this month? ")),
    "debt": int(input("How much are you paying towards debt? ")),

}
    bills_list = [(a,b) for a, b in bills.items()] # this converts the dictionary to a list of tuple so user sees the values for every expense.
    print("Here is a list of each expense for the month. \n", bills_list)
   
    total_bills2 = sum(bills.values())

    def bills_ana():
        if total_bills2 > total_income:
            print(f'You are living above your means\n Your Monthly Income is ${round(total_income):,.2f} and Total expense for the month is ${round(total_bills2):,.2f}')
        else:
            print(f"Total money spent on bills and expenses is ${round(total_bills2):,.2f}")
        return

    bills_ana()

    after_col = total_income - total_bills2
    savings = after_col * 0.4

    def savings_res():
        if savings > 0:
            print(f"You have saved ${round(savings):,.2f}, Good Job!")
        else:
            print("You need to cut down on your expenses or spending")
        return
    savings_res()
    # print(f"Total savings for a month is ${round(savings):,.2f}")


    return

monthly()