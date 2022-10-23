price = 15.84
vat = round(0.23 * price, 2)
names=['Amount',"VAT 23%"]
print(f"{names[0]:8}: {price:6} zł")
print(f"{names[1]:8}: {vat:6} zł")