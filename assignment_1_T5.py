hours_total = int(input("Please type your working hour for one month\n> "))
if hours_total <= 160:
    payment_total = hours_total*10
else:
    hours_extra = hours_total - 160
    payment_total = hours_extra*40 + 160*10

print(f"Your payment for one month is {payment_total}$.")

