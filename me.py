def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

def calculate_total(bill_amount, tip_amount):
    return bill_amount + tip_amount

def main():
    bill_amount = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage: "))
    payment_method = input("Enter payment method (bank/cash): ").lower()
    payment_type = input("Enter payment type (single/joint): ").lower()

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_total(bill_amount, tip_amount)

    print("\nTip Amount: ${:.2f}".format(tip_amount))
    print("Total Amount: ${:.2f}".format(total_amount))

    if payment_method == "bank":
        if payment_type == "single":
            print("Please pay ${:.2f} using your bank account.".format(total_amount))
        elif payment_type == "joint":
            print("Please pay ${:.2f} jointly using your bank account.".format(total_amount))
        else:
            print("Invalid payment type. Please enter 'single' or 'joint'.")
    elif payment_method == "cash":
        if payment_type == "single":
            print("Please pay ${:.2f} in cash.".format(total_amount))
        elif payment_type == "joint":
            print("Please pay ${:.2f} jointly in cash.".format(total_amount))
        else:
            print("Invalid payment type. Please enter 'single' or 'joint'.")
    else:
        print("Invalid payment method. Please enter 'bank' or 'cash'.")

if __name__ == "__main__":
    main()
