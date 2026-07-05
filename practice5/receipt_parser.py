import re
import json

# Read the receipt
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Find all product names
product_pattern = r"\d+\.\s*\n(.*?)\n\d+,\d{3}\s*x"

products = re.findall(product_pattern, text, re.DOTALL)

products = [product.replace("\n", " ").strip() for product in products]


# Find all prices
price_pattern = r"\d+,\d{3}\s*x\s*[\d ]+,\d{2}\n([\d ]+,\d{2})"

prices = re.findall(price_pattern, text)

prices = [price.replace(" ", "") for price in prices]


# Calculate total price
total = 0

for price in prices:
    number = float(price.replace(",", "."))
    total += number


# Find receipt total
receipt_total_pattern = r"ИТОГО:\s*\n([\d ]+,\d{2})"

receipt_total = re.search(receipt_total_pattern, text)

if receipt_total:
    receipt_total = receipt_total.group(1)
else:
    receipt_total = "Not found"


# Find date
date_pattern = r"\d{2}\.\d{2}\.\d{4}"

date = re.search(date_pattern, text)

if date:
    date = date.group()
else:
    date = "Not found"


# Find time
time_pattern = r"\d{2}:\d{2}:\d{2}"

time = re.search(time_pattern, text)

if time:
    time = time.group()
else:
    time = "Not found"


# Find payment method
payment_pattern = r"(Банковская карта|Наличные)"

payment = re.search(payment_pattern, text)

if payment:
    payment = payment.group()
else:
    payment = "Not found"


# Save all data
receipt = {
    "Date": date,
    "Time": time,
    "Payment Method": payment,
    "Receipt Total": receipt_total,
    "Calculated Total": f"{total:.2f}",
    "Products": []
}


# Add products and prices
for product, price in zip(products, prices):
    receipt["Products"].append({
        "Product": product,
        "Price": price
    })


# Print result
print(json.dumps(receipt, indent=4, ensure_ascii=False))