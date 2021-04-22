# write code for pizza slices price
print("Enter the number of pizza slices you want: ")
sli = int(input())
price = 0.0
if (sli % 2) == 0:
    price = sli*120.0

else:
    price = sli*123.0

print("You have to pay Rs", price)


