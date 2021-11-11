# PROBLEM 1

value1 = 444
value2 = 333
mod1 = 444 % 333
quot1 = 444 / 333

print("The remainder of " + str(value1) + "/" + str(value2) + " is \"" + str(mod1) + "\" and the quotient of " + str(value1) + "/" + str(value2) + " is \"" + str(round(quot1, 2)) + "\"")

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 2

hours_worked = 40
pay_rate = 20
pay_rate2 = "%0.2f" % pay_rate
pay1 = hours_worked * pay_rate
pay2 = "%0.2f" % pay1

print("Hours worked: " + str(hours_worked) + "\nPay rate: $" + str(pay_rate2) + "\nPaycheck amount will be: $" + str(pay2))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 3

hours_worked = int(input("Enter how many hours you worked: "))
pay_rate = float(input("What is your pay rate per hour?: "))
pay_rate2 = "%0.2f" % pay_rate

pay1 = hours_worked * pay_rate
pay2 = "%0.2f" % pay1

print("Hours worked: " + str(hours_worked) + "\nPay rate: $" + str(pay_rate2) + "\nPaycheck amount will be: $" + str(pay2))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 4

hours_worked = int(input("Enter how many regular hours you worked: "))
overtime_worked = int(input("Enter how many overtime hours you worked: "))
pay_rate = float(input("What is your pay rate per hour?: "))
pay_rate2 = "%0.2f" % pay_rate

pay_calc1 = hours_worked * pay_rate
pay_calc2 = overtime_worked * (pay_rate * 1.5)
pay1 = pay_calc1 + pay_calc2
pay2 = "%0.2f" % pay1

print("Hours worked: " + str(hours_worked) + "\nOvertime hours worked: " + str(overtime_worked) + "\nPay rate: $" + str(pay_rate2) + "\nPaycheck amount will be: $" + str(pay2))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 5

hours_worked = int(input("Enter how many regular hours you worked: "))
pay_rate = float(input("What is your pay rate per hour?: "))
pay_rate2 = "%0.2f" % pay_rate
overtime_worked = 0

if hours_worked > 40:
    overtime_worked = hours_worked - 40
    pay_calc1 = hours_worked * pay_rate
    pay_calc2 = overtime_worked * (pay_rate * 1.5)
    pay1 = pay_calc1 + pay_calc2
    pay2 = "%0.2f" % pay1
    print("Hours worked: " + str(hours_worked) + "\nOvertime hours worked: " + str(overtime_worked) + "\nPay rate: $" + str(pay_rate2) + "\nPaycheck amount will be: $" + str(pay2))
else:
    pay3 = hours_worked * pay_rate
    pay4 = "%0.2f" % pay3
    print("Hours worked: " + str(hours_worked) + "\nOvertime hours worked: " + str(overtime_worked) + "\nPay rate: $" + str(pay_rate2) + "\nPaycheck amount will be: $" + str(pay4))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 6

net_bill = 54.32
gross_bill = (54.32*0.075) + 54.32
tip_total = gross_bill + (net_bill * 0.25)
share = tip_total / 2.0

print("Each person owes: " + str(round(share, 2)))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 7

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list contains " + str(len(list1)) + " items which are " + str(list1))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 8

import statistics

invoice_list = [1, 2, 3, 4, 5]
description_list = ["hand warmer", "red polka dot jar", "jam making set", "red coat rack", "yellow coat rack"]
quantity_list = [6, 6, 6, 3, 3]
price_list = [1.85, 1.85, 4.25, 4.95, 4.95]
customerID_list = ["C1", "C2", "C3", "C4", "C5"]
dictionary1 = {}

index_value = 0
tuple1 = (invoice_list[index_value], description_list[index_value], quantity_list[index_value], price_list[index_value], customerID_list[index_value])
dictionary1[invoice_list[index_value]] = tuple1

index_value = 1
tuple1 = (invoice_list[index_value], description_list[index_value], quantity_list[index_value], price_list[index_value], customerID_list[index_value])
dictionary1[invoice_list[index_value]] = tuple1

index_value = 2
tuple1 = (invoice_list[index_value], description_list[index_value], quantity_list[index_value], price_list[index_value], customerID_list[index_value])
dictionary1[invoice_list[index_value]] = tuple1

index_value = 3
tuple1 = (invoice_list[index_value], description_list[index_value], quantity_list[index_value], price_list[index_value], customerID_list[index_value])
dictionary1[invoice_list[index_value]] = tuple1

index_value = 4
tuple1 = (invoice_list[index_value], description_list[index_value], quantity_list[index_value], price_list[index_value], customerID_list[index_value])
dictionary1[invoice_list[index_value]] = tuple1

print("All keys in the dictionary are: " + str(dictionary1.keys()))
print("All values in the dictionary are: " + str(dictionary1.values()))
print("Price mean: $" + str(round(statistics.mean(price_list), 2)))

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 9

user_input = int(input("Please enter an invoice number: "))

if (user_input in dictionary1):
    print("Invoice " + str(user_input) + " data includes: " + str((dictionary1[user_input])))
else:
    print("The invoice does not exist")

#------------------------------------------------------------------------------------------------------------------------------------------

# PROBLEM 10

user_input = int(input("Please enter an invoice number: "))
price_list_mean = float(round(statistics.mean(price_list), 2))

if (user_input in dictionary1):
    print("Invoice " + str(user_input) + " data includes: " + str((dictionary1[user_input])))
    if dictionary1[user_input][-2] > price_list_mean:
        print("Price (" + str(dictionary1[user_input][-2]) + ") is greater than the mean (" + str(price_list_mean) + ")")
    elif dictionary1[user_input][-2] == price_list_mean:
        print("Price (" + str(dictionary1[user_input][-2]) + ") is equal to the mean (" + str(price_list_mean) + ")")
    elif dictionary1[user_input][-2] < price_list_mean:
        print("Price (" + str(dictionary1[user_input][-2]) + ") is less than the mean (" + str(price_list_mean) + ")")
    else:
        print("The invoice does not exist")
else:
    print("The invoice does not exist")








