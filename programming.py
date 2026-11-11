print("=== Parking Garage Calculator ===")
print("Enter day type: weekday, weekend, or holiday")
print("Type 'done' when finished entering hours\n")

total = 0.0

while True:
    day_type = input("Enter day type for 1 hour: ").lower()
    
    if day_type == "done":
        break
    elif day_type == "weekday":
        price = 8.00
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    elif day_type == "weekend":
        price = 6.00
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    elif day_type == "holiday":
        price = 5.00
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    else:
        print("Invalid day type! Please enter weekday, weekend, holiday, or done.\n")

print("\n=== Parking Summary ===")
print(f"Subtotal: ${total:.2f}")

# Chegirma sharti ($50.00 yoki undan ko'p bo'lsa $7.00 chegirma)
if total >= 50.00:
    discount = 7.00
    final_total = total - discount
    print(f"Frequent Parker Discount: -${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")
else:
    print(f"Final Total: ${total:.2f}")

print("Thank you for parking with us!")