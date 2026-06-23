def return_amount(total_amount, paid_amount):

    if paid_amount > total_amount:
        return paid_amount - total_amount

    elif total_amount > paid_amount:
        return total_amount - paid_amount

    else:
        return 0

total_amount = float(input("Enter the total bill amount: "))
paid_amount = float(input("Enter the amount you gave: "))

if paid_amount > total_amount:
    change = return_amount(total_amount, paid_amount)
    print("💰 Change to return:", change)

elif total_amount > paid_amount:
    due = return_amount(total_amount, paid_amount)
    print("⚠️ Customer still owes:", due)

else:
    print("✅ Exact amount has been paid!")
