# firstNumber = 10
# secondNumber = 20

# print("The sum of the first and second number is", firstNumber + secondNumber)

# def addtion (firstNumber, secondNumber):
#     print(firstNumber + secondNumber)

# addtion(10,20)

# firstNumber = int(input("Enter first number: "))
# secondNumber = int(input("Enter first number: "))
# print("The sum of the first and second number is", firstNumber + secondNumber)

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter first number: "))
# print("The sum of the first and second number is", first_number * second_number)

# Convert from naira to dollar
# amount_naira = float(input("Enter amount in naira: "))
# amount_dollar = amount_naira / 415
# print(amount_naira,"naira is equivalent to", amount_dollar, "dollars")

def naira_to_dollar ():
    amount_naira = float(input("Enter amount in naira: "))
    amount_dollar = amount_naira / 415.90                                                
    amount_dollar = float("{:.2f}".format(amount_dollar))                          # Change the precision
    print(amount_naira,"naira is equivalent to", amount_dollar, "dollars")

naira_to_dollar()

# Convert kilometer to meter
# kilo_value = float(input("Enter value in kilometer: "))
# meter_value = kilo_value * 1000
# print(kilo_value,"kilometers is equivalent to", meter_value,"meters.")
