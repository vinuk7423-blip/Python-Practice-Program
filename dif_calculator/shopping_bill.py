customer = input("Enter customer name: ")
rice_price = float(input("Enter rice price: "))
rice_quantity = int(input("Enter rice quantity: "))
milk_price = float(input("Enter milk price: "))
milk_quantity = int(input("Enter milk quantity: "))
bread_price = float(input("Enter bread price: "))
bread_quantity = int(input("Enter bread quantity: "))
fruit_price = float(input("Enter fruit price: "))
fruit_quantity = int(input("Enter fruit quantity: "))
rice_total = rice_price * rice_quantity
milk_total = milk_price * milk_quantity
bread_total = bread_price * bread_quantity
fruit_total = fruit_price * fruit_quantity
subtotal = rice_total + milk_total + bread_total + fruit_total
if subtotal >= 2000:
    discount = subtotal * 0.20
elif subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0
taxable_amount = subtotal - discount
gst = taxable_amount * 0.05
final_bill = taxable_amount + gst
print("\n----- BILL -----")
print("Customer:", customer)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final Bill:", final_bill)
