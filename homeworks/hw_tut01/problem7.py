price = float(input('Enter the amount of a purchase: '))
stateSaleTax = price * 5 / 100
countySaleTax = price * 2.5 / 100
totalTax = stateSaleTax + countySaleTax
totalSale = price + totalTax

print('Amount of the purchase: {:.2f}'.format(price))
print('The state sales tax: {:.2f}'.format(stateSaleTax))
print('The county sales tax: {:.2f}'.format(countySaleTax))
print('The total sales tax: {:.2f}'.format(totalTax))
print('The total of the sale: {:.2f}'.format(totalSale))